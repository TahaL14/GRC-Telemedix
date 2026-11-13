# 5. Applicabilité et matrices d'écarts HDS et NIS2

> État du droit arrêté au **11 novembre 2026**. Les deux sujets évoluent : chaque affirmation datée est à revérifier avant un entretien (liste en annexe).

## 5.1 HDS : à qui s'applique l'obligation ?

### Règle

L'article L.1111-8 du code de la santé publique impose une certification à toute personne qui héberge, **pour le compte d'un tiers**, des données de santé recueillies à l'occasion d'activités de prévention, de diagnostic, de soins ou de suivi. Le code liste six activités d'hébergement ; chaque acteur doit être certifié pour les activités qu'il réalise effectivement.

| N° | Activité | Qui la réalise dans le cas Télémédix | Certifié ? |
|---|---|---|---|
| 1 | Mise à disposition et maintien en condition opérationnelle des sites physiques | Hébergeur | Oui |
| 2 | Mise à disposition et maintien en condition opérationnelle de l'infrastructure matérielle | Hébergeur | Oui |
| 3 | Mise à disposition et maintien en condition opérationnelle de l'infrastructure virtuelle | Hébergeur | Oui |
| 4 | Mise à disposition et maintien en condition opérationnelle de la plateforme d'hébergement d'applications | Non fournie comme service : Télémédix installe et exploite elle-même systèmes et intergiciels sur les VM | Sans objet, à confirmer |
| 5 | Administration et exploitation du système d'information contenant les données de santé | **Télémédix** (équipe SRE) | **Non** |
| 6 | Sauvegarde des données de santé | Hébergeur (service de sauvegarde), piloté par Télémédix | Oui |

### Argumentation

1. **Les clients sont les « tiers » protégés par le texte.** Médecins et structures de santé confient les données de leurs patients à Télémédix : Télémédix héberge pour leur compte, même si elle s'appuie sur un hébergeur.
2. **« L'exigence HDS porte sur l'hébergeur » est une demi-vérité.** Elle porte sur chaque acteur qui réalise une des six activités. Le certificat de l'hébergeur couvre les activités 1, 2, 3 et 6. Il ne couvre pas ce que fait Télémédix.
3. **Télémédix réalise l'activité 5.** Ses SRE disposent d'accès d'administration aux systèmes et aux bases qui contiennent les données de santé, déploient, supervisent et interviennent en production. Le référentiel v2 définit l'activité 5 comme la maîtrise des interventions sur les ressources mises à disposition du client.
4. **Conclusion : écart majeur.** Télémédix doit soit obtenir la certification HDS pour l'activité 5 (ce qui suppose un SMSI certifié ISO 27001 sur ce périmètre), soit confier l'administration et l'exploitation à un infogérant certifié et ne conserver aucun accès aux données.
5. **Le prestataire visio.** Les flux ne sont pas conservés ; un simple transit ne semble pas constituer un hébergement, mais la question mérite une vérification, surtout tant que le flux est déchiffré sur ses serveurs. Le chiffrement de bout en bout (A24) règle le sujet sur le fond.

**Réserve.** La frontière de l'activité 5 pour les éditeurs fait l'objet de travaux pédagogiques de l'ANS en cours (FAQ, cas d'usage types). La qualification retenue ici est la lecture prudente ; elle doit être confirmée sur la FAQ de l'ANS et, pour un cas réel, par un avis juridique (action A03).

### Trajectoire recommandée

| Option | Avantages | Inconvénients | Décision proposée |
|---|---|---|---|
| A. Certification HDS activité 5 par Télémédix | Maîtrise de l'exploitation ; argument commercial fort ; réutilise le SMSI ISO 27001 | 12 à 18 mois ; coût d'audit et de maintien ; effort documentaire | **Retenue** (A02) |
| B. Infogérance par un prestataire certifié activité 5 | Mise en conformité plus rapide | Perte d'agilité (les développeurs ne touchent plus la production) ; coût récurrent ; dépendance | Solution de repli ou transitoire |
| C. Statu quo | Aucun coût immédiat | Non-conformité à une obligation légale ; perte d'appels d'offres hospitaliers | Écartée |

## 5.2 Matrice d'écarts HDS

Les exigences sont regroupées par thème. Les numéros d'exigence du référentiel v2 sont à reporter depuis le texte officiel lors de la revue : ils ne sont volontairement pas reproduits de mémoire.

### Volet 1 : ce que Télémédix doit vérifier chez son hébergeur

| Thème | Attendu | Constat | Écart | Actions |
|---|---|---|---|---|
| Validité du certificat | Certificat en cours de validité, délivré selon le référentiel v2 | Certificat présenté à la signature, jamais recontrôlé | Mineur | A25 |
| Périmètre du certificat | Les activités certifiées couvrent tous les services réellement utilisés (VM, stockage, sauvegarde) | Activités 1, 2, 3 et 6 ; correspondance avec les services consommés non vérifiée ligne à ligne | Mineur | A25 |
| Localisation | Données stockées dans l'Espace économique européen | Deux sites en France | Aucun | - |
| Accès depuis un pays tiers et législations extra-européennes | Information du client sur les accès distants hors EEE et sur les législations étrangères applicables à l'hébergeur | Information non demandée | Mineur | A25 |
| Contrat d'hébergement | Clauses imposées par le code de la santé publique (périmètre, localisation, réversibilité, sous-traitants, qualité de service) | Contrat standard de l'hébergeur ; revue juridique non faite | Mineur | A03, A25 |
| Sous-traitants de l'hébergeur | Liste communiquée ; sous-traitants eux-mêmes couverts | Liste non demandée | Mineur | A25 |
| Réversibilité | Restitution des données dans un format exploitable, puis destruction | Clause présente, jamais testée | Mineur | A23 |

### Volet 2 : ce que Télémédix doit satisfaire pour l'activité 5

| Thème | Attendu | Constat | Écart | Actions |
|---|---|---|---|---|
| Certification | Certificat HDS couvrant l'activité 5 | Absent | **Majeur** | A02, A03 |
| Système de management | SMSI conforme à l'ISO 27001 sur le périmètre d'hébergement ; déclaration d'applicabilité | Pas de SMSI ; déclaration d'applicabilité en version 0.1 (dossier 4) | **Majeur** | A01, A02 |
| Analyse de risques | Appréciation des risques couvrant les données de santé | Étude EBIOS RM réalisée (dossier 2) | Aucun | - |
| Maîtrise des accès d'administration | Comptes nominatifs, authentification forte, traçabilité des interventions | MFA partiel, traces non centralisées | **Majeur** | A05, A18 |
| Accès aux données par le personnel | Accès limités au strict nécessaire, justifiés et revus | Connexion « en tant que » sans contrôle | **Majeur** | A08, A09 |
| Chiffrement | Protection des données de santé en transit et au repos | Disques chiffrés ; pas de chiffrement applicatif | Mineur | A10 |
| Sauvegarde et continuité | Sauvegardes testées ; plan de continuité | Restauration jamais testée ; PRA non testé | **Majeur** | A11, A23 |
| Gestion des incidents | Procédure, information du client sans délai | Pas de procédure formalisée | **Majeur** | A22 |
| Relations avec les clients | Contrat conforme : description des prestations, localisation, sous-traitants ultérieurs, réversibilité, engagements de service | Conditions générales incomplètes sur ces points | Mineur | A03, A04 |
| Sous-traitance ultérieure | Chaîne de sous-traitance maîtrisée et transparente | Trois sous-traitants sous contrat ; pas d'évaluation périodique | Mineur | A25 |
| Souveraineté | Aucun accès aux données depuis un pays tiers sans encadrement ; transparence | Équipes en France ; outils SaaS de support et de CI/CD à qualifier | Mineur | A25 |
| Audit et amélioration | Audits internes, revue de direction | Absents | **Majeur** | A02 |

**Bilan HDS.** 7 écarts majeurs, tous sur le volet 2. Le choix de l'hébergeur n'est pas le problème : c'est l'activité propre de l'éditeur qui n'est pas couverte.

---

## 5.3 NIS2 : Télémédix est-elle concernée ?

### État de la transposition en France

| Date | Fait |
|---|---|
| 17 octobre 2024 | Échéance de transposition fixée par la directive (UE) 2022/2555 |
| 12 mars 2025 | Adoption par le Sénat du projet de loi « résilience des infrastructures critiques et renforcement de la cybersécurité » |
| 10 septembre 2025 | Adoption du texte par la commission spéciale de l'Assemblée nationale |
| 17 mars 2026 | Publication par l'ANSSI du Référentiel Cyber France (ReCyF), en document de travail |
| 8 juillet 2026 | Saisine de la Cour de justice de l'UE par la Commission pour défaut de transposition |
| 9 au 13 novembre 2026 | Examen du projet de loi en séance publique à l'Assemblée nationale |
| **11 novembre 2026** | **Loi non promulguée, aucun décret d'application** |

**Conséquence.** À la date du dossier, aucune obligation NIS2 n'est opposable à une entreprise privée en France. Le raisonnement ci-dessous s'appuie donc sur la directive ; il devra être repris sur la loi promulguée et ses décrets, qui peuvent préciser les catégories et les seuils.

### Raisonnement d'applicabilité

| Étape | Question | Analyse pour Télémédix | Résultat |
|---|---|---|---|
| 1. Taille | L'entité atteint-elle la taille d'une entreprise moyenne (recommandation 2003/361/CE) ? | Une petite entreprise compte moins de 50 personnes **et** un chiffre d'affaires ou un bilan n'excédant pas 10 M€. Avec 52 salariés, Télémédix n'est plus une petite entreprise | **Entreprise moyenne** |
| 2a. Secteur « santé » (annexe I) | Télémédix est-elle un prestataire de soins de santé ? | Non : elle n'emploie aucun professionnel de santé et ne dispense aucun soin. Ses clients, eux, en sont | Non |
| 2b. Secteur « infrastructure numérique » (annexe I) | Télémédix est-elle un fournisseur de services d'informatique en nuage ? | La directive définit ce service comme l'accès à la demande à un ensemble modulable de ressources informatiques partageables. Un logiciel fourni en mode SaaS peut entrer dans cette définition | **Probable, à confirmer** |
| 2c. Secteur « gestion des services TIC » (annexe I) | Télémédix est-elle un fournisseur de services gérés ? | Non : elle exploite sa propre plateforme, pas les systèmes de ses clients | Non |
| 3. Catégorie | Essentielle ou importante ? | Une entité de l'annexe I de taille moyenne est **importante** ; elle devient essentielle au-delà des seuils de l'entreprise moyenne (250 personnes ou plus, ou plus de 50 M€ de chiffre d'affaires et plus de 43 M€ de bilan) | **Entité importante** |
| 4. Effet indirect | Les clients sont-ils concernés ? | Le centre hospitalier client est un prestataire de soins : il devra maîtriser sa chaîne d'approvisionnement (art. 21.2.d) et répercutera des exigences par contrat | **Oui, dans tous les cas** |

### Conclusion argumentée

| Hypothèse | Qualification | Probabilité estimée |
|---|---|---|
| Le SaaS de Télémédix est qualifié de service d'informatique en nuage | **Entité importante** | La plus probable au regard de la directive |
| Le SaaS n'est pas qualifié ainsi par le droit français | Hors périmètre direct, mais soumise aux exigences contractuelles de ses clients | Possible |
| Entité essentielle | Écartée : Télémédix n'est ni un prestataire de soins, ni une grande entreprise | Très faible |

**Position retenue : se préparer comme une entité importante.** Trois raisons : la qualification la plus probable y conduit ; les clients hospitaliers l'exigeront par contrat de toute façon ; les mesures attendues recoupent presque entièrement l'ISO 27001 et le référentiel HDS, déjà visés.

**Sensibilité au seuil.** Avec 48 salariés, Télémédix serait une petite entreprise et sortirait du périmètre direct, sauf désignation particulière. Le calcul de l'effectif intègre les entreprises liées et partenaires : une filiale ou un actionnaire majoritaire peut faire franchir le seuil.

**Texte complémentaire.** Pour les fournisseurs de services numériques, dont l'informatique en nuage, la Commission a adopté le règlement d'exécution (UE) 2024/2690, qui détaille les mesures techniques attendues et les critères d'incident important. Son articulation avec le référentiel de l'ANSSI est à vérifier.

## 5.4 Matrice d'écarts NIS2

Référence : directive (UE) 2022/2555, articles 20, 21 et 23. Correspondance indicative avec l'Annexe A de l'ISO 27001:2022.

| Exigence | Attendu | Constat | Écart | Mesures ISO liées | Actions |
|---|---|---|---|---|---|
| Art. 20 : gouvernance | Les dirigeants approuvent les mesures, en supervisent la mise en œuvre et se forment | Sécurité non portée en comité de direction | **Majeur** | 5.1, 5.4 | A01, A26 |
| Art. 21.2.a : politiques d'analyse des risques et de sécurité | Analyse de risques et politique formalisées | Étude EBIOS RM réalisée ; PSSI rédigée, non approuvée | Mineur | 5.1 | A01 |
| Art. 21.2.b : gestion des incidents | Détection, traitement, retour d'expérience | Pas de procédure ni de détection centralisée | **Majeur** | 5.24 à 5.28, 8.15, 8.16 | A18, A22 |
| Art. 21.2.c : continuité, sauvegardes, gestion de crise | Sauvegardes, reprise, cellule de crise testées | Sauvegardes non testées ; PRA non testé ; pas d'exercice | **Majeur** | 5.29, 5.30, 8.13, 8.14 | A11, A22, A23 |
| Art. 21.2.d : sécurité de la chaîne d'approvisionnement | Évaluation et encadrement contractuel des fournisseurs | Contrats signés, pas de suivi | **Majeur** | 5.19 à 5.23 | A15, A24, A25 |
| Art. 21.2.e : sécurité de l'acquisition, du développement et de la maintenance ; vulnérabilités | Développement sécurisé, gestion et divulgation des vulnérabilités | Revue de code ; pas d'outillage ni de délais de correction | **Majeur** | 8.8, 8.25 à 8.29 | A14, A15, A16, A20 |
| Art. 21.2.f : évaluation de l'efficacité des mesures | Indicateurs, audits, tests | Test d'intrusion annuel seulement | Mineur | 5.35, 5.36 | A02, A16 |
| Art. 21.2.g : cyberhygiène et formation | Pratiques de base et formation régulière | Session d'accueil uniquement | Mineur | 6.3, 8.1, 8.7 | A19, A26 |
| Art. 21.2.h : cryptographie et chiffrement | Politique de chiffrement et de gestion des clés | Chiffrement en place, pas de politique ; pas de chiffrement applicatif | Mineur | 8.24 | A10, A24 |
| Art. 21.2.i : ressources humaines, contrôle d'accès, gestion des actifs | Habilitations, revues, inventaire | Revue des droits absente ; inventaire partiel | Mineur | 5.9, 5.15 à 5.18, 6.1 à 6.6 | A08, A09 |
| Art. 21.2.j : authentification multifacteur, communications sécurisées | MFA et canaux de secours sécurisés | MFA partiel ; pas de canal de crise hors bande | **Majeur** | 5.14, 8.5 | A05, A06, A07, A22 |
| Art. 23 : notification des incidents importants | Alerte sous 24 heures, notification sous 72 heures, rapport final sous un mois | Aucune procédure | **Majeur** | 5.5, 5.24, 5.26 | A22 |
| Enregistrement auprès de l'autorité | Déclaration de l'entité selon les modalités nationales | Sans objet tant que la loi n'est pas en vigueur | En attente | 5.31 | A28 |

**Bilan NIS2.** 7 écarts majeurs sur 13 exigences. Tous sont déjà couverts par des actions issues de l'analyse de risques : NIS2 n'ajoute aucun chantier technique, elle ajoute la responsabilité des dirigeants (art. 20) et les délais de notification (art. 23).

## 5.5 Recouvrement des référentiels

| Sujet | RGPD | HDS | ISO 27001 | NIS2 |
|---|---|---|---|---|
| Analyse de risques | Art. 32, 35 | Oui | Clause 6.1 | Art. 21.2.a |
| Notification d'incident | CNIL sous 72 h (art. 33) ; le sous-traitant prévient le responsable sans délai | Information du client | 5.24 à 5.26 | 24 h, 72 h, un mois (art. 23) |
| Sous-traitance | Art. 28 | Chaîne certifiée et transparente | 5.19 à 5.23 | Art. 21.2.d |
| Responsabilité de la direction | Responsabilité (art. 5.2, 24) | Via le SMSI | Clause 5 | Art. 20 |
| Certification | Non | Oui | Oui (volontaire) | Non |

**Lecture.** Un seul système de management (ISO 27001) alimenté par une seule analyse de risques (EBIOS RM) permet de répondre aux quatre cadres. C'est la justification de l'action structurante A02.

## 5.6 Justification des choix (arguments d'entretien)

| Choix | Justification |
|---|---|
| Qualifier l'éditeur pour l'activité 5 | Lecture conforme à la règle « chaque acteur est certifié pour ce qu'il fait ». Soutenir l'inverse expose à un refus en appel d'offres et à un risque pénal |
| Ne pas citer les numéros d'exigence HDS | Citer de mémoire un numéro faux décrédibilise tout le dossier ; la colonne est à remplir texte en main |
| Raisonner sur la directive | Seul texte stable à la date du dossier ; la loi française pouvait encore être amendée |
| Conclure « entité importante probable » plutôt que trancher | La qualification du SaaS comme informatique en nuage est discutée ; un consultant annonce son niveau de certitude |
| Écarter « entité essentielle » | Confusion fréquente : la santé est un secteur hautement critique, mais l'éditeur n'est pas le prestataire de soins, et la taille compte |
