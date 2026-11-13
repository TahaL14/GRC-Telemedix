# Annexe : points à vérifier et sources

Ce dossier est un exercice sur un cas fictif. Il ne constitue ni un avis juridique ni un audit. Les points ci-dessous doivent être contrôlés sur les textes officiels avant toute présentation.

## A. Points à vérifier

Confiance : **forte** (fait établi et recoupé), **moyenne** (raisonnement défendable, à confirmer), **faible** (hypothèse de travail).

| # | Sujet | Ce que le dossier affirme | Confiance | Où vérifier |
|---|---|---|---|---|
| 1 | Transposition de NIS2 | Loi non promulguée au 11/11/2026 ; examen à l'Assemblée du 9 au 13 novembre 2026 | Forte à la date indiquée, périssable | Dossier législatif sur assemblee-nationale.fr ; Légifrance ; cyber.gouv.fr |
| 2 | Qualification NIS2 d'un éditeur SaaS | Probable « fournisseur de services d'informatique en nuage », donc entité importante à 52 salariés | Moyenne | Directive (UE) 2022/2555 : art. 2, 3, 6 et annexe I ; loi française promulguée et décrets ; outil d'auto-qualification de l'ANSSI |
| 3 | Seuils de taille | Petite entreprise : moins de 50 personnes et chiffre d'affaires ou bilan ≤ 10 M€ | Forte | Recommandation 2003/361/CE ; prise en compte des entreprises liées |
| 4 | Règlement d'exécution (UE) 2024/2690 | S'applique aux fournisseurs de services numériques, dont l'informatique en nuage | Moyenne | EUR-Lex ; articulation avec le référentiel de l'ANSSI |
| 5 | Référentiel Cyber France (ReCyF) | Publié par l'ANSSI le 17 mars 2026 en document de travail | Moyenne (sources secondaires) | cyber.gouv.fr |
| 6 | Activités HDS | Six activités ; chaque acteur est certifié pour celles qu'il réalise | Forte | Code de la santé publique, art. L.1111-8 et R.1111-9 ; référentiel de certification HDS v2 |
| 7 | Activité 5 pour un éditeur qui administre ses VM | L'éditeur doit être certifié | Moyenne | FAQ de l'ANS sur l'activité 5 ; travaux pédagogiques de l'ANS (sessions d'octobre et novembre 2026) ; avis juridique |
| 8 | Activité 4 | Sans objet quand l'éditeur exploite sa propre plateforme sur des VM | Faible | Référentiel HDS v2, chapitre sur le périmètre |
| 9 | Référentiel HDS v2 | Publié en 2024 ; seule version valide depuis le 16 mai 2026 ; exigences de localisation dans l'EEE et de transparence sur les accès hors UE | Forte | esante.gouv.fr ; arrêté de publication au Journal officiel |
| 10 | Numéros d'exigence HDS | Non cités dans le dossier | Sans objet | À reporter depuis le référentiel officiel ; une révision v2.1 est en concertation |
| 11 | Prestataire visio et HDS | Un flux en transit non conservé ne constitue pas un hébergement | Faible | FAQ de l'ANS ; avis juridique |
| 12 | Rôles RGPD | Clients responsables de traitement, éditeur sous-traitant ; éditeur responsable pour le compte patient | Moyenne | Lignes directrices 07/2020 du CEPD ; guide du sous-traitant de la CNIL ; DPO |
| 13 | AIPD obligatoire | Oui (santé, grande échelle, personnes vulnérables) | Forte | Liste de la CNIL des traitements soumis à AIPD ; lignes directrices WP 248 |
| 14 | Base légale | Art. 6.1.b, c ou e et art. 9.2.h ; pas le consentement | Forte | RGPD ; référentiel de la CNIL pour les cabinets médicaux |
| 15 | Consentement à l'acte de télémédecine | Prévu par le code de la santé publique, distinct du consentement RGPD | Moyenne | Code de la santé publique, art. R.6316-2 |
| 16 | Durée de conservation du dossier | 20 ans ; 28e anniversaire pour un mineur ; 10 ans après le décès | Forte pour les établissements ; recommandation en libéral | Code de la santé publique, art. R.1112-7 ; Conseil national de l'Ordre des médecins ; référentiels de la CNIL |
| 17 | Durée des journaux | 6 mois à 1 an | Moyenne | Recommandation de la CNIL sur la journalisation ; PGSSI-S (traces d'accès aux données de santé) |
| 18 | Données de paiement | 13 mois ; pièces comptables 10 ans | Moyenne | Recommandation de la CNIL sur les données de carte ; code de commerce |
| 19 | Identifiant national de santé | Usage limité au référencement des données de santé ; obtenu par le téléservice INSi | Moyenne | Référentiel INS (ANS) |
| 20 | Référentiel des SI de téléconsultation | Opposable ; certificat de conformité délivré par l'ANS ; calendrier d'extension à tous les éditeurs incertain | Moyenne | esante.gouv.fr ; arrêté du 9 février 2024 |
| 21 | Intitulés de l'Annexe A | 93 mesures (37, 8, 14, 34) ; titres français usuels | Forte pour la structure, moyenne pour la lettre des titres | NF EN ISO/IEC 27001:2022 (AFNOR) |
| 22 | Formule du niveau de menace | (dépendance × pénétration) / (maturité × confiance) | Forte | Guide EBIOS Risk Manager de l'ANSSI, atelier 3 |
| 23 | Délais de notification NIS2 | 24 heures, 72 heures, un mois | Forte | Directive, art. 23 |

## B. Sources consultées (novembre 2026)

**Transposition de NIS2**
- Le Monde Informatique, « NIS 2 : la loi Résilience arrive enfin à l'Assemblée », 10 novembre 2026 : https://www.lemondeinformatique.fr/cybersecurite-conformite/nis-2-la-loi-resilience-arrive-enfin-a-l-assemblee
- InformatiqueNews, « NIS 2 : ce que la loi Résilience change pour les DSI, RSSI et dirigeants », novembre 2026 : https://www.informatiquenews.fr/nis2-loi-resilience-obligations-entreprises-251585
- Leto, « Transposition NIS 2 : examen à l'Assemblée le 9 novembre 2026 » : https://www.leto.legal/news/nis-2-projet-loi-resilience-assemblee-nationale-9-novembre-2026
- Phinasoft, « Loi résilience : où en est la transposition de NIS 2 en France ? », 8 octobre 2026 : https://phinasoft.com/fr/blog/loi-resilience-transposition-nis-2-france/

**HDS**
- ANS, communiqué du 16 mai 2024 sur la publication du référentiel HDS : https://esante.gouv.fr/index%2ephp/espace-presse/publication-au-journal-officiel-du-referentiel-de-certification-hds-souverainete-des-donnees-et-ameliorations-du-referentiel
- ANS, webinaire HDS du 15 octobre 2025 (transition v2, activité 5) : https://industriels.esante.gouv.fr/sites/default/files/media/document/Webinaire-HDS_20251015_vf.pdf
- ANS, session collective HDS du 7 octobre 2026 : https://esante.gouv.fr/sites/default/files/media/document/20261007_ANS_SessionCollective_HDS%20v1.0.pdf
- ANS, travaux pédagogiques sur l'activité 5, session du 4 novembre 2026 : https://esante.gouv.fr/sites/default/files/media/document/20261104_ANS_SessionCollective_HDS%20v0.7.pdf
- ANS, page HDS : https://esante.gouv.fr/produits-services/hds

**Téléconsultation**
- ANS, « Le référentiel d'interopérabilité, de sécurité et d'éthique des SI de téléconsultation désormais opposable », 14 février 2024 : https://esante.gouv.fr/actualites/toutes-les-actualites/le-referentiel-d-interoperabilite-de-securite-et-d-ethique-des-systemes-d-informations-de
- HAS, référentiel de bonnes pratiques applicable aux sociétés de téléconsultation : https://has-sante.fr/jcms/p_3470126/fr/teleconsultation-referentiel-de-bonnes-pratiques-professionnelles-applicable-aux-societes-de-teleconsultation

**Protection des données**
- Conseil national de l'Ordre des médecins, FAQ sur la protection des données (durées de conservation) : https://www.conseil-national.medecin.fr/medecin/exercice/protection-donnees-faq

## C. Textes de référence à consulter à la source

| Texte | Éditeur |
|---|---|
| Guide EBIOS Risk Manager et fiches méthodes | ANSSI (cyber.gouv.fr) |
| Guide d'hygiène informatique | ANSSI |
| Directive (UE) 2022/2555 et règlement d'exécution (UE) 2024/2690 | EUR-Lex |
| Règlement (UE) 2016/679 (RGPD) | EUR-Lex |
| Guides AIPD, guide du sous-traitant, guide de la sécurité des données personnelles | CNIL (cnil.fr) |
| Référentiel de certification HDS, PGSSI-S, référentiel INS, Pro Santé Connect | ANS (esante.gouv.fr) |
| Code de la santé publique | Légifrance |
| ISO/IEC 27001:2022 et 27002:2022 | ISO, AFNOR |
