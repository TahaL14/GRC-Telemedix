# Dossier de conformité cybersécurité d'une plateforme de téléconsultation

Étude de cas **fictive** en gouvernance, risques et conformité (GRC) appliquée à la e-santé en France : analyse de risques EBIOS Risk Manager, AIPD, déclaration d'applicabilité ISO 27001:2022, matrices d'écarts HDS et NIS2, plan d'actions et PSSI.

> **Avertissement.** Télémédix SAS, ses clients et ses fournisseurs sont inventés. Ce travail est un exercice de formation : il ne constitue ni un audit ni un avis juridique. 

## Le cas en bref

| | |
|---|---|
| Organisme | Télémédix SAS, éditeur SaaS de téléconsultation, 52 salariés |
| Volumétrie | 150 000 patients, 2 000 professionnels de santé, 30 000 téléconsultations par mois |
| Hébergement | Hébergeur certifié HDS (France) ; l'éditeur administre lui-même ses machines virtuelles |
| Sous-traitants | Visio, paiement, notifications |

## Résultats clés

| Livrable | Résultat |
|---|---|
| Analyse de risques | 10 risques, dont 6 élevés ; après traitement : 8 moyens, 2 faibles, aucun élevé |
| AIPD | Obligatoire ; gravité maximale pour l'accès illégitime ; avis du DPO favorable sous réserve |
| Déclaration d'applicabilité | 93 mesures : 89 retenues, 4 exclues ; 10 en place, 60 partielles, 19 à faire |
| HDS | Hébergeur conforme ; **éditeur non certifié pour l'activité 5** (administration et exploitation) : 7 écarts majeurs |
| NIS2 | Directive non transposée en France à la date du dossier ; qualification la plus probable : **entité importante** ; 7 écarts majeurs sur 13 exigences |
| Plan d'actions | 28 actions sur 18 mois : 17 gains rapides, 7 projets structurants, 4 compléments |

## Contenu

| Fichier | Contenu |
|---|---|
| [01-cadrage.md](01-cadrage.md) | Périmètre, acteurs, flux, données, cadre réglementaire, état initial, hypothèses |
| [02-ebios-rm.md](02-ebios-rm.md) | Ateliers 1 à 5 : valeurs métier, sources de risque, écosystème, scénarios, traitement |
| [03-aipd-registre.md](03-aipd-registre.md) | AIPD (base légale, minimisation, durées, risques) et registres des traitements |
| [04-dda-iso27001.md](04-dda-iso27001.md) | Déclaration d'applicabilité : 93 mesures de l'Annexe A justifiées par les risques |
| [05-ecarts-hds-nis2.md](05-ecarts-hds-nis2.md) | Argumentation d'applicabilité et matrices d'écarts HDS et NIS2 |
| [06-plan-actions.md](06-plan-actions.md) | 28 actions priorisées (impact, effort), feuille de route |
| [07-pssi.md](07-pssi.md) | Politique de sécurité en deux pages |
| [annexes/sources-et-points-a-verifier.md](annexes/sources-et-points-a-verifier.md) | Niveau de confiance de chaque affirmation et sources |
| [pdf/dossier-complet.pdf](pdf/dossier-complet.pdf) | Export PDF de l'ensemble |

## Fil conducteur : la traçabilité

Chaque élément renvoie au suivant par un identifiant stable :

```
Événement redouté (ER) → Scénario stratégique (SS) → Risque (R01 à R10)
        → Mesure de l'Annexe A (5.1 à 8.34) → Action (A01 à A28) → Indicateur
```

Exemple : la divulgation massive de données (ER1) peut résulter d'un défaut de contrôle d'accès de l'API (SS2, risque R02). Ce risque justifie notamment les mesures 8.3, 8.26 et 8.28, mises en œuvre par l'action A14, dont l'indicateur est la couverture des points d'accès par des tests d'autorisation.

Le script `outils/verifier_coherence.py` contrôle cette chaîne : identifiants existants, niveaux de risque conformes à la matrice, calcul des niveaux de menace, décomptes de la déclaration d'applicabilité, cohérence entre le traitement des risques et le plan d'actions.

```bash
python3 outils/verifier_coherence.py   # contrôle de cohérence
bash outils/generer_pdf.sh             # export PDF (pandoc + Chrome)
```


## Référentiels utilisés

EBIOS Risk Manager (ANSSI) ; RGPD et guides AIPD de la CNIL ; ISO/IEC 27001:2022 ; référentiel de certification HDS v2 et PGSSI-S (ANS) ; directive (UE) 2022/2555 dite NIS2.

## Limites

Cas fictif : aucune donnée réelle, aucun entretien, aucune preuve d'audit.



