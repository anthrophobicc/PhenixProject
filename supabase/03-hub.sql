-- À COLLER DANS SUPABASE > SQL Editor > Run (une seule fois). Contient aussi 02-lab-public.sql : inutile de lancer 02.
--
-- 1. Phenix Lab public : une proposition apparaît tout de suite pour tout le monde, on vote, on commente,
--    et l'équipe modère après coup (décocher « visible » masque une proposition).
-- 2. Phenix Hub : les versions de la bibliothèque que publie la communauté (une langue, une région, un club…).
--    La version officielle n'est pas ici : elle est construite depuis le dépôt et servie par le site (site/hub/).
--    Une version envoyée reste invisible tant qu'on ne coche pas « visible » dans Table Editor > versions.

-- ---------------------------------------------------------------- 1. Lab public (identique à 02)
alter table public.propositions alter column visible set default true;
-- Ce qui a été envoyé avant ce changement (dont la fiche de test envoyée depuis le téléphone) devient visible aussi.
update public.propositions set visible = true where not visible and statut <> 'rejected';

create or replace view public.propositions_publiques as
  select p.reference, p.type, p.titre, p.resume, p.contenu, p.axe, p.categorie, p.langue, p.urgence, p.sources,
         p.fiche_liee, p.auteur, p.statut, p.cree_le,
         coalesce(v.n, 0) as votes,
         coalesce(c.n, 0) as commentaires
  from public.propositions p
  left join (select cible, count(*)::int as n from public.votes group by cible) v on v.cible = p.reference
  left join (select cible, count(*)::int as n from public.commentaires where visible group by cible) c on c.cible = p.reference
  where p.visible and p.statut <> 'rejected';

-- ---------------------------------------------------------------- 2. Phenix Hub : les versions
create sequence if not exists public.numero_version start 1;

create table if not exists public.versions (
  id              uuid primary key default gen_random_uuid(),
  reference       text unique not null default
                  'VER-' || to_char(now(), 'YYYY') || '-' || lpad(nextval('public.numero_version')::text, 3, '0'),
  genre           text not null default 'version' check (genre in ('version', 'calque', 'carte')),  -- une version de fiches, un calque de repères ou une carte
  nom             text not null check (char_length(nom) between 3 and 80),
  langue          text not null check (char_length(langue) between 2 and 12),
  communaute      text check (char_length(communaute) <= 80),     -- « Communauté chinoise », « Bretagne », « Club de voile »…
  description     text check (char_length(description) <= 1200),
  base            text check (char_length(base) <= 40),            -- version officielle de départ, ex. 2026.09.27
  nb_fiches       int check (nb_fiches between 0 and 20000),
  taille          int check (taille between 1 and 26214400),
  fichier         text unique,                                     -- chemin du fichier dans le dossier « versions »
  auteur          text check (char_length(auteur) <= 60),
  contact         text check (char_length(contact) <= 120),        -- jamais public
  visible         boolean not null default false,                  -- coché : elle apparaît dans Phenix Hub
  telechargements int not null default 0,
  commentaire     text,                                            -- notes internes, jamais publiques
  empreinte       text,
  cree_le         timestamptz not null default now(),
  modifie_le      timestamptz not null default now()
);
-- Si la table existait déjà sans calques ni cartes.
alter table public.versions add column if not exists genre text not null default 'version';
alter table public.versions drop constraint if exists versions_nb_fiches_check;
alter table public.versions add constraint versions_nb_fiches_check check (nb_fiches between 0 and 20000);
create index if not exists versions_suivi on public.versions (visible, cree_le desc);

drop trigger if exists t_touch on public.versions;
create trigger t_touch before update on public.versions for each row execute function public.touch_modifie_le();

alter table public.versions enable row level security;
revoke all on public.versions from anon, authenticated;
revoke all on sequence public.numero_version from anon, authenticated;

-- Annoncer une version avant d'envoyer son fichier. Renvoie sa référence et le chemin où déposer le fichier.
create or replace function public.publier_version(p jsonb) returns jsonb
language plpgsql security definer set search_path = public as $$
declare
  emp text := public.empreinte_requete();
  n int;
  ref text;
  ident uuid;
  chemin text;
begin
  if emp is not null then
    select count(*) into n from public.versions where empreinte = emp and cree_le > now() - interval '1 hour';
    if n >= 3 then raise exception 'Too many versions sent, try again in an hour.'; end if;
  end if;
  select count(*) into n from public.versions where cree_le > now() - interval '1 hour';
  if n >= 30 then raise exception 'Too many versions right now, try again later.'; end if;
  insert into public.versions (genre, nom, langue, communaute, description, base, nb_fiches, taille, auteur, contact, empreinte)
  values (case when p->>'genre' in ('calque', 'carte') then p->>'genre' else 'version' end,
          trim(p->>'nom'),
          lower(trim(p->>'langue')),
          nullif(trim(p->>'communaute'), ''),
          nullif(trim(p->>'description'), ''),
          nullif(trim(p->>'base'), ''),
          nullif(p->>'nb_fiches', '')::int,
          nullif(p->>'taille', '')::int,
          nullif(trim(p->>'auteur'), ''),
          nullif(trim(p->>'contact'), ''),
          emp)
  returning reference, id into ref, ident;
  chemin := ref || '/' || ident::text || '.json';
  update public.versions set fichier = chemin where id = ident;
  return jsonb_build_object('reference', ref, 'fichier', chemin);
end $$;

-- Compter un téléchargement (seulement pour une version publiée). Renvoie le nouveau total.
create or replace function public.compter_telechargement(ref text) returns integer
language sql security definer set search_path = public as $$
  update public.versions set telechargements = telechargements + 1
  where reference = ref and visible
  returning telechargements;
$$;

revoke all on function public.publier_version(jsonb), public.compter_telechargement(text) from public;
grant execute on function public.publier_version(jsonb), public.compter_telechargement(text) to anon, authenticated;

-- Ce que tout le monde voit : les versions cochées « visible », avec leurs votes, sans contact ni notes.
create or replace view public.versions_publiques as
  select v.reference, v.nom, v.langue, v.communaute, v.description, v.base, v.nb_fiches, v.taille, v.fichier,
         v.auteur, v.telechargements, v.cree_le, v.modifie_le,
         coalesce(x.n, 0) as votes, v.genre
  from public.versions v
  left join (select cible, count(*)::int as n from public.votes group by cible) x on x.cible = v.reference
  where v.visible;
revoke all on public.versions_publiques from anon, authenticated;
grant select on public.versions_publiques to anon, authenticated;

-- Les fichiers : dossier privé, JSON seulement, 25 Mo au plus.
-- On dépose seulement dans la demi-heure qui suit l'annonce, au chemin donné par publier_version, une seule fois.
-- On lit seulement le fichier d'une version publiée : une version en attente ne se télécharge pas.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values ('versions', 'versions', false, 26214400, array['application/json'])
on conflict (id) do update set public = false, file_size_limit = 26214400, allowed_mime_types = array['application/json'];

create or replace function public.depot_version_permis(chemin text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.versions where fichier = chemin and cree_le > now() - interval '30 minutes')
     and not exists (select 1 from storage.objects where bucket_id = 'versions' and name = chemin);
$$;
create or replace function public.version_visible(chemin text) returns boolean
language sql stable security definer set search_path = public as $$
  select exists (select 1 from public.versions where fichier = chemin and visible);
$$;
revoke all on function public.depot_version_permis(text), public.version_visible(text) from public;
grant execute on function public.depot_version_permis(text), public.version_visible(text) to anon, authenticated;

drop policy if exists "deposer version" on storage.objects;
create policy "deposer version" on storage.objects
  for insert to anon, authenticated
  with check (bucket_id = 'versions' and public.depot_version_permis(name));

drop policy if exists "lire version publiee" on storage.objects;
create policy "lire version publiee" on storage.objects
  for select to anon, authenticated
  using (bucket_id = 'versions' and public.version_visible(name));
