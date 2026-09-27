-- À COLLER DANS SUPABASE > SQL Editor > Run (une seule fois).
-- Phenix Lab devient un espace public : une proposition apparaît tout de suite pour tout le monde,
-- on vote et on commente, et l'équipe modère après coup (décocher « visible » masque une proposition).
-- Pour revenir à la relecture avant publication : alter table public.propositions alter column visible set default false;

alter table public.propositions alter column visible set default true;

-- La vue publique porte le nombre de votes et de commentaires, pour trier par « Top ».
create or replace view public.propositions_publiques as
  select p.reference, p.type, p.titre, p.resume, p.contenu, p.axe, p.categorie, p.langue, p.urgence, p.sources,
         p.fiche_liee, p.auteur, p.statut, p.cree_le,
         coalesce(v.n, 0) as votes,
         coalesce(c.n, 0) as commentaires
  from public.propositions p
  left join (select cible, count(*)::int as n from public.votes group by cible) v on v.cible = p.reference
  left join (select cible, count(*)::int as n from public.commentaires where visible group by cible) c on c.cible = p.reference
  where p.visible and p.statut <> 'rejected';
