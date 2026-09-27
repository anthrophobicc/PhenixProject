-- Phenix : ce que la communauté envoie (fiches, idées de fiches, corrections, messages) et les signalements.
-- Tout le monde peut envoyer, depuis le site, une story Instagram ou l'application, sans compte.
-- Tout arrive en privé : on le lit dans le tableau de bord Supabase (Table Editor > propositions).
-- Cocher « visible » publie la proposition pour tout le monde (page Communauté du site).
-- Le public ne touche jamais les tables : il passe par deux fonctions (proposer, signaler) et une vue (propositions_publiques).

drop table if exists public.propositions cascade;
drop function if exists public.propositions_garde() cascade;
create sequence if not exists public.numero_proposition start 1;

create table public.propositions (
  id           uuid primary key default gen_random_uuid(),
  reference    text unique not null default
               'SUB-' || to_char(now(), 'YYYY') || '-' || lpad(nextval('public.numero_proposition')::text, 4, '0'),
  type         text not null default 'fiche' check (type in ('fiche', 'idee', 'correction', 'message')),

  -- contenu proposé
  titre        text not null check (char_length(titre) between 3 and 140),
  contenu      text not null check (char_length(contenu) between 3 and 120000),
  resume       text check (char_length(resume) <= 400),
  axe          smallint check (axe between 1 and 3),
  categorie    text check (char_length(categorie) <= 80),
  langue       text not null default 'en' check (char_length(langue) between 2 and 12),
  urgence      boolean not null default false,
  sources      text check (char_length(sources) <= 8000),
  note_editeur text check (char_length(note_editeur) <= 8000),
  fiche_liee   text check (char_length(fiche_liee) <= 40),   -- pour une correction : la fiche concernée
  origine      text check (char_length(origine) <= 40),      -- story, site, app, reddit…

  -- auteur, tout est facultatif ; le contact n'est jamais public
  auteur       text check (char_length(auteur) <= 60),
  contact      text check (char_length(contact) <= 120),

  -- suivi éditorial (rempli par nous dans le tableau de bord)
  statut       text not null default 'submitted'
               check (statut in ('submitted', 'under_review', 'changes_requested', 'rejected', 'community', 'verified', 'official')),
  visible      boolean not null default false,             -- coché : tout le monde la voit sur le site
  motif        text,                                        -- pourquoi refusée, ou quoi corriger
  fiche_id     text,                                        -- identifiant Phenix attribué à l'intégration
  commentaire  text,                                        -- notes internes, jamais publiques

  empreinte    text,                                        -- anti-rafale : empreinte du jour, jamais l'adresse IP
  cree_le      timestamptz not null default now(),
  modifie_le   timestamptz not null default now()
);
create index on public.propositions (statut, cree_le desc);
create index on public.propositions (empreinte, cree_le);

create table if not exists public.signalements (
  id        uuid primary key default gen_random_uuid(),
  fiche_id  text not null check (char_length(fiche_id) <= 40),
  motif     text not null check (motif in ('erreur', 'qualite', 'dangereux', 'illegal', 'spam', 'hors_sujet', 'droits')),
  detail    text check (char_length(detail) <= 4000),
  source    text check (char_length(source) <= 1000),
  traite    boolean not null default false,
  empreinte text,
  cree_le   timestamptz not null default now()
);
create index if not exists signalements_suivi on public.signalements (traite, cree_le desc);

-- Horodatage des modifications faites dans le tableau de bord.
create or replace function public.touch_modifie_le() returns trigger language plpgsql as $$
begin new.modifie_le = now(); return new; end $$;
drop trigger if exists t_touch on public.propositions;
create trigger t_touch before update on public.propositions for each row execute function public.touch_modifie_le();

-- Tables fermées au public : sécurité par ligne activée, aucun droit, aucune politique.
alter table public.propositions enable row level security;
alter table public.signalements enable row level security;
revoke all on public.propositions, public.signalements from anon, authenticated;
revoke all on sequence public.numero_proposition from anon, authenticated;

-- Empreinte de l'appareil pour le jour : sert seulement à freiner les envois en rafale.
create or replace function public.empreinte_requete() returns text
language plpgsql stable security definer set search_path = public as $$
declare
  h json := coalesce(nullif(current_setting('request.headers', true), ''), '{}')::json;
  ip text := trim(split_part(coalesce(h->>'cf-connecting-ip', h->>'x-real-ip', h->>'x-forwarded-for', ''), ',', 1));
begin
  return case when ip = '' then null else md5(ip || to_char(now(), 'YYYY-MM-DD') || 'phenix') end;
end $$;

-- Envoyer une proposition. Renvoie sa référence (SUB-2026-0001) à montrer à la personne.
create or replace function public.proposer(p jsonb) returns text
language plpgsql security definer set search_path = public as $$
declare
  emp text := public.empreinte_requete();
  n int;
  ref text;
begin
  if emp is not null then
    select count(*) into n from public.propositions where empreinte = emp and cree_le > now() - interval '10 minutes';
    if n >= 5 then raise exception 'Too many submissions, try again in a few minutes.'; end if;
  end if;
  select count(*) into n from public.propositions where cree_le > now() - interval '1 hour';
  if n >= 200 then raise exception 'Too many submissions right now, try again later.'; end if;
  insert into public.propositions (type, titre, contenu, resume, axe, categorie, langue, urgence, sources, note_editeur,
                                   fiche_liee, origine, auteur, contact, empreinte)
  values (coalesce(nullif(p->>'type', ''), 'fiche'),
          trim(p->>'titre'),
          trim(p->>'contenu'),
          nullif(trim(p->>'resume'), ''),
          nullif(p->>'axe', '')::smallint,
          nullif(trim(p->>'categorie'), ''),
          coalesce(nullif(p->>'langue', ''), 'en'),
          coalesce((p->>'urgence')::boolean, false),
          nullif(trim(p->>'sources'), ''),
          nullif(trim(p->>'note_editeur'), ''),
          nullif(trim(p->>'fiche_liee'), ''),
          nullif(trim(p->>'origine'), ''),
          nullif(trim(p->>'auteur'), ''),
          nullif(trim(p->>'contact'), ''),
          emp)
  returning reference into ref;
  return ref;
end $$;

-- Signaler un problème sur une fiche publiée.
create or replace function public.signaler(p jsonb) returns boolean
language plpgsql security definer set search_path = public as $$
declare
  emp text := public.empreinte_requete();
  n int;
begin
  if emp is not null then
    select count(*) into n from public.signalements where empreinte = emp and cree_le > now() - interval '10 minutes';
    if n >= 5 then raise exception 'Too many reports, try again in a few minutes.'; end if;
  end if;
  insert into public.signalements (fiche_id, motif, detail, source, empreinte)
  values (trim(p->>'fiche_id'), p->>'motif', nullif(trim(p->>'detail'), ''), nullif(trim(p->>'source'), ''), emp);
  return true;
end $$;

revoke all on function public.empreinte_requete() from public, anon, authenticated;
revoke all on function public.proposer(jsonb), public.signaler(jsonb) from public;
grant execute on function public.proposer(jsonb), public.signaler(jsonb) to anon, authenticated;

-- Ce que tout le monde voit : seulement les propositions cochées « visible », sans contact ni notes internes.
create or replace view public.propositions_publiques as
  select reference, type, titre, resume, contenu, axe, categorie, langue, urgence, sources, fiche_liee, auteur, statut, cree_le
  from public.propositions
  where visible;
revoke all on public.propositions_publiques from anon, authenticated;
grant select on public.propositions_publiques to anon, authenticated;

-- Images jointes : dossier privé, 5 Mo au plus, seulement dans le quart d'heure qui suit une proposition, 6 par proposition.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('propositions', 'propositions', false, 5242880, array['image/png', 'image/jpeg', 'image/webp'])
on conflict (id) do update set public = false, file_size_limit = 5242880, allowed_mime_types = array['image/png', 'image/jpeg', 'image/webp'];

create or replace function public.depot_image_permis(chemin text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.propositions
                 where reference = split_part(chemin, '/', 1) and cree_le > now() - interval '15 minutes')
     and (select count(*) from storage.objects
          where bucket_id = 'propositions' and split_part(name, '/', 1) = split_part(chemin, '/', 1)) < 6;
$$;
revoke all on function public.depot_image_permis(text) from public;
grant execute on function public.depot_image_permis(text) to anon, authenticated;

drop policy if exists "deposer image" on storage.objects;
create policy "deposer image" on storage.objects
  for insert to anon, authenticated
  with check (bucket_id = 'propositions' and public.depot_image_permis(name));

-- ---------------------------------------------------------------- votes et commentaires
-- La cible est une fiche (URG-INC-002) ou une proposition (SUB-2026-0001).
-- Un vote par appareil : l'appareil envoie un identifiant tiré au hasard, gardé chez lui ; on n'en garde qu'une empreinte.
create table if not exists public.votes (
  cible    text not null check (char_length(cible) between 3 and 40),
  appareil text not null,
  cree_le  timestamptz not null default now(),
  primary key (cible, appareil)
);
create table if not exists public.commentaires (
  id        uuid primary key default gen_random_uuid(),
  cible     text not null check (char_length(cible) between 3 and 40),
  auteur    text check (char_length(auteur) <= 40),
  texte     text not null check (char_length(texte) between 2 and 2000),
  visible   boolean not null default true,     -- décoché dans le tableau de bord : le commentaire disparaît du site
  empreinte text,
  cree_le   timestamptz not null default now()
);
create index if not exists commentaires_cible on public.commentaires (cible, cree_le);
alter table public.votes enable row level security;
alter table public.commentaires enable row level security;
revoke all on public.votes, public.commentaires from anon, authenticated;

-- Voter (ou retirer son vote) ; renvoie le nombre de votes de la cible.
create or replace function public.voter(cible text, appareil text, retirer boolean default false) returns integer
language plpgsql security definer set search_path = public as $$
declare
  a text := md5(coalesce(appareil, '') || 'phenix-vote');
  n int;
begin
  if char_length(coalesce(appareil, '')) < 16 then raise exception 'Invalid device id.'; end if;
  if retirer then
    delete from public.votes v where v.cible = voter.cible and v.appareil = a;
  else
    select count(*) into n from public.votes v where v.appareil = a and v.cree_le > now() - interval '1 minute';
    if n >= 20 then raise exception 'Too many votes, slow down.'; end if;
    insert into public.votes (cible, appareil) values (voter.cible, a) on conflict do nothing;
  end if;
  select count(*) into n from public.votes v where v.cible = voter.cible;
  return n;
end $$;

-- Commenter : visible tout de suite, sans lien (contre le spam), 5 par appareil en 10 minutes.
create or replace function public.commenter(p jsonb) returns uuid
language plpgsql security definer set search_path = public as $$
declare
  emp text := public.empreinte_requete();
  t text := trim(p->>'texte');
  n int;
  nouvel uuid;
begin
  if t ~* '(https?://|www\.|\.com/|\.ru/|t\.me/)' then raise exception 'Links are not allowed in comments.'; end if;
  if emp is not null then
    select count(*) into n from public.commentaires where empreinte = emp and cree_le > now() - interval '10 minutes';
    if n >= 5 then raise exception 'Too many comments, try again in a few minutes.'; end if;
  end if;
  select count(*) into n from public.commentaires where cree_le > now() - interval '1 hour';
  if n >= 300 then raise exception 'Too many comments right now, try again later.'; end if;
  insert into public.commentaires (cible, auteur, texte, empreinte)
  values (trim(p->>'cible'), nullif(trim(p->>'auteur'), ''), t, emp)
  returning id into nouvel;
  return nouvel;
end $$;

revoke all on function public.voter(text, text, boolean), public.commenter(jsonb) from public;
grant execute on function public.voter(text, text, boolean), public.commenter(jsonb) to anon, authenticated;

create or replace view public.votes_publics as
  select cible, count(*)::int as votes from public.votes group by cible;
create or replace view public.commentaires_publics as
  select id, cible, auteur, texte, cree_le from public.commentaires where visible;
revoke all on public.votes_publics, public.commentaires_publics from anon, authenticated;
grant select on public.votes_publics, public.commentaires_publics to anon, authenticated;
