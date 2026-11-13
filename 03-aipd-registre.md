# 3. Analyse d'impact relative à la protection des données et registre

Méthode : trame de la CNIL (contexte, principes fondamentaux, risques, validation). Les risques pour les personnes s'appuient sur l'étude EBIOS RM (dossier 2).

## 3.1 Qui doit réaliser l'AIPD ?

| Traitement | Responsable de traitement | Rôle de Télémédix | Conséquence |
|---|---|---|---|
| Téléconsultation et tenue du dossier | Chaque client (professionnel ou structure de santé) | Sous-traitant | L'obligation d'AIPD pèse sur le client. Télémédix doit l'**aider** (RGPD, art. 28.3.f) : elle fournit la présente analyse comme **AIPD type**, que chaque client adapte et valide |
| Compte utilisateur patient | Télémédix | Responsable de traitement | Télémédix réalise et valide elle-même l'AIPD |

**Pourquoi une AIPD est obligatoire.** Le traitement cumule plusieurs critères de risque élevé retenus par les lignes directrices européennes : données sensibles (santé), grande échelle (150 000 patients), personnes vulnérables (patients). Il correspond aussi aux types de traitements de données de santé que la CNIL soumet à AIPD. Deux critères suffisent.

## 3.2 Description du traitement

| Rubrique | Contenu |
|---|---|
| Finalité principale | Permettre la réalisation d'actes de téléconsultation et la tenue du dossier associé |
| Finalités secondaires | Prise de rendez-vous et rappels ; encaissement de l'acte ; authentification et sécurité ; assistance aux utilisateurs |
| Finalités exclues | Prospection auprès des patients, revente ou réutilisation des données de santé, profilage, entraînement de modèles sur les données de santé |
| Personnes concernées | Patients (dont mineurs représentés par un titulaire de l'autorité parentale), professionnels de santé |
| Données | Voir inventaire D1 à D8 du dossier 1, §1.5 |
| Destinataires | Le professionnel consulté et, le cas échéant, l'équipe de soins au sens du code de la santé publique ; le patient ; le personnel habilité de Télémédix dans la stricte limite du support et de l'exploitation |
| Sous-traitants ultérieurs | Hébergeur HDS (France), prestataire visio (UE), prestataire de paiement (UE), prestataire de notifications (UE) |
| Transferts hors UE | Aucun pour les données de santé. Notifications push via les services d'Apple et de Google : message sans contenu (« Vous avez une notification ») |
| Supports | Voir biens supports BS1 à BS10 du dossier 2 |

## 3.3 Principes fondamentaux

### Base légale

| Finalité | Responsable | Base légale (art. 6) | Exception pour les données de santé (art. 9) | Commentaire |
|---|---|---|---|---|
| Téléconsultation et dossier | Client | Professionnel libéral ou centre privé : exécution du contrat de soins (6.1.b) et obligation légale de tenir le dossier (6.1.c). Hôpital public : mission d'intérêt public (6.1.e) | 9.2.h : prise en charge sanitaire, par un professionnel soumis au secret (9.3) | Le **consentement n'est pas la base légale**. Le consentement du patient à l'acte de télémédecine, prévu par le code de la santé publique, est un consentement aux soins, distinct du consentement RGPD |
| Compte patient | Télémédix | Exécution des conditions d'utilisation (6.1.b) | 9.2.h pour les données liées aux rendez-vous, traitées sous l'autorité des professionnels | Point de qualification à valider (annexe) |
| Rappels de rendez-vous | Client | Exécution du contrat (6.1.b) | Sans objet si le message ne contient aucune donnée de santé | Dépend de l'action A12 |
| Encaissement | Client | Exécution du contrat (6.1.b) | Sans objet | Libellé bancaire neutre |
| Journalisation et sécurité | Télémédix et client | Obligation légale de sécurité (6.1.c ; RGPD art. 32 ; référentiels opposables) | Sans objet | |
| Statistiques d'usage | Télémédix | Intérêt légitime (6.1.f) | Sans objet : données agrégées, sans donnée de santé | Mise en balance documentée |

### Minimisation

| Donnée | Décision | Justification |
|---|---|---|
| Flux audio et vidéo | Jamais enregistrés | Aucune finalité ne l'exige ; supprime un stock de données très sensibles |
| Motif de consultation | Champ libre facultatif, visible du seul praticien | Utile à la préparation, non indispensable |
| Identifiant national de santé | Collecté par le téléservice INSi, uniquement pour référencer les documents de santé | Usage limité par le référentiel INS ; jamais utilisé comme identifiant de connexion |
| Notifications SMS et e-mail | Message générique, sans nom de praticien ni spécialité | La spécialité révèle l'état de santé (psychiatre, oncologue) |
| Tickets de support | Pièces jointes interdites pour les documents médicaux ; purge à 90 jours | Le support n'a pas à connaître le contenu médical |
| Environnements de test | Données synthétiques uniquement | Les développeurs n'ont pas besoin de données réelles |
| Libellé de paiement | Nom de l'éditeur, sans spécialité | Le relevé bancaire ne doit rien révéler |
| Géolocalisation, contacts, traceurs publicitaires | Non collectés | Aucune finalité |

### Durées de conservation

| Donnée | Durée | Fondement | Qui décide |
|---|---|---|---|
| Dossier de téléconsultation (compte rendu, ordonnance, documents) | 20 ans après la dernière prise en charge ; jusqu'au 28e anniversaire pour un mineur ; 10 ans après le décès | Code de la santé publique, art. R.1112-7 (établissements) ; même durée recommandée en exercice libéral | Le client. Télémédix applique ses instructions et restitue puis supprime les données en fin de contrat |
| Messages échangés pendant la consultation | Versés au dossier si le praticien le décide ; sinon supprimés 30 jours après l'acte | Minimisation | Le client |
| Flux audio et vidéo | Aucune conservation | Minimisation | Sans objet |
| Compte patient inactif | Suppression après 3 ans sans connexion, après avertissement ; les dossiers restent chez les praticiens | Proportionnalité | Télémédix |
| Traces d'accès aux dossiers | 12 mois en ligne ; durée plus longue à arbitrer | Recommandation de la CNIL sur la journalisation (6 mois à 1 an) ; exigences de traçabilité du secteur | Télémédix et client |
| Journaux techniques | 6 mois | Recommandation de la CNIL | Télémédix |
| Données de transaction | 13 mois pour la contestation ; pièces comptables 10 ans | Recommandations de la CNIL ; code de commerce | Télémédix et client |
| Tickets de support | 3 ans après clôture ; pièces jointes 90 jours | Preuve contractuelle ; minimisation | Télémédix |
| Sauvegardes | 35 jours glissants | Une suppression est effective dans les sauvegardes au plus tard à l'expiration du cycle | Télémédix |

### Information et droits des personnes

| Droit | Mise en œuvre | Limite |
|---|---|---|
| Information | Notice à la création du compte et avant chaque téléconsultation ; mention des rôles (praticien responsable, Télémédix sous-traitant) | |
| Accès | Téléchargement des documents depuis l'espace patient ; demande d'accès au dossier adressée au praticien | L'accès au dossier médical suit aussi le code de la santé publique |
| Rectification | Données de compte modifiables en ligne ; contenu médical : demande au praticien | Un compte rendu ne se modifie pas, il se complète |
| Effacement | Suppression du compte possible | Les dossiers médicaux sont conservés par obligation légale du praticien |
| Opposition | Non applicable aux traitements fondés sur le contrat ou l'obligation légale ; applicable aux statistiques | |
| Portabilité | Export des documents déposés par le patient | |
| Circuit | Les demandes reçues par Télémédix pour un traitement du client sont transmises au client sous 72 heures (clause contractuelle) | |

### Sous-traitance (art. 28)

| Sous-traitant ultérieur | Contrat | Garanties à obtenir |
|---|---|---|
| Hébergeur HDS | Contrat d'hébergement comportant les clauses imposées par le code de la santé publique | Certificat HDS en cours de validité et couvrant les activités réellement fournies ; localisation dans l'EEE |
| Prestataire visio | Accord de sous-traitance | Chiffrement de bout en bout ou relais dédié ; localisation UE ; notification d'incident sous 24 heures ; droit d'audit |
| Prestataire de paiement | Accord de sous-traitance | Attestation PCI DSS annuelle |
| Prestataire de notifications | Accord de sous-traitance | Localisation UE ; suppression des messages après envoi |

Les clients sont informés de la liste des sous-traitants ultérieurs et de tout changement, avec un droit d'objection.

## 3.4 Risques pour les droits et libertés des personnes

Échelle de la CNIL : négligeable, limitée, importante, maximale.

| Événement redouté | Impacts pour les personnes | Sources et scénarios (dossier 2) | Gravité | Vraisemblance initiale | Mesures | Vraisemblance résiduelle |
|---|---|---|---|---|---|---|
| **Accès illégitime** aux données | Révélation de pathologies, discrimination, chantage, atteinte à la réputation, hameçonnage ciblé | R01, R02, R03, R05, R06, R08, R09 | Maximale | Importante | A05, A07, A08, A10, A12, A14, A15, A18, A24 | Limitée |
| **Modification non désirée** | Ordonnance ou compte rendu faux : erreur de prise en charge ; faux documents au nom d'un patient ou d'un praticien | R03, R04 | Importante | Importante | A06, A15, A18, A27 | Limitée |
| **Disparition** des données | Perte du dossier, rupture de suivi, consultation impossible | R01, R07 | Importante | Importante | A11, A22, A23 | Négligeable |

**Lecture.** La gravité d'un accès illégitime reste maximale après traitement : une donnée de santé divulguée ne peut pas être « rattrapée ». Le plan agit sur la vraisemblance. Ce risque résiduel est porté à la connaissance des clients.

## 3.5 Plan d'action et validation

| Élément | Contenu |
|---|---|
| Mesures à mettre en œuvre | Actions A04, A05, A06, A07, A08, A10, A11, A12, A13, A14, A15, A17, A18, A24 du dossier 6 |
| Avis du DPO | Favorable **sous réserve** : réalisation des actions A07, A08 et A12 sous 4 mois ; qualification HDS de l'activité 5 (A03) |
| Avis des personnes concernées | À recueillir auprès d'un panel de patients et de praticiens (art. 35.9), ou justification de l'absence de consultation |
| Consultation préalable de la CNIL (art. 36) | Non requise si le risque résiduel est jugé acceptable après réalisation du plan ; à réexaminer si A10 ou A24 étaient abandonnées |
| Décision | Compte patient : validation par la direction de Télémédix. Téléconsultation : validation par chaque client |
| Révision | Tous les 3 ans au plus, et à chaque évolution majeure (enregistrement, nouvelle finalité, nouveau sous-traitant, alimentation du DMP) |

---

## 3.6 Registre des activités de traitement

Télémédix tient **deux registres** : celui du responsable de traitement (art. 30.1) et celui du sous-traitant (art. 30.2).

### Registre du responsable de traitement

| Réf. | Traitement | Finalité | Base légale | Personnes | Données | Destinataires | Durée | Sécurité |
|---|---|---|---|---|---|---|---|---|
| T01 | Compte utilisateur patient | Créer et authentifier le compte, gérer les préférences | Contrat | Patients | D1, identifiants de connexion | Personnel habilité ; hébergeur | 3 ans après la dernière connexion | MFA, chiffrement, journalisation |
| T02 | Gestion de la relation client | Contractualisation, facturation des abonnements | Contrat ; obligation légale (comptabilité) | Professionnels, contacts des structures | D6, coordonnées, données de facturation | Finance, commerce | Durée du contrat + 5 ans ; pièces comptables 10 ans | Contrôle d'accès |
| T03 | Support aux utilisateurs | Répondre aux demandes d'assistance | Contrat | Patients, professionnels | D1, D6, contenu des tickets | Support ; éditeur de l'outil de tickets | 3 ans ; pièces jointes 90 jours | Accès tracé et justifié (A08) |
| T04 | Sécurité et journalisation | Détecter les incidents, tracer les accès, constituer des preuves | Obligation légale | Tous utilisateurs, salariés | D8 | RSSI, SRE ; prestataire de supervision | 6 à 12 mois | Journaux protégés en intégrité |
| T05 | Statistiques d'usage | Améliorer le produit | Intérêt légitime | Utilisateurs | Données agrégées, sans donnée de santé | Produit | 25 mois | Agrégation |
| T06 | Gestion du personnel | Paie, administration | Contrat ; obligation légale | Salariés | Données RH | RH ; prestataire de paie | Selon les obligations sociales | Hors périmètre du dossier |

### Registre du sous-traitant

| Réf. | Catégorie de traitements | Pour le compte de | Données | Sous-traitants ultérieurs | Transferts hors UE | Sécurité |
|---|---|---|---|---|---|---|
| S01 | Téléconsultation (visio, audio, messagerie) | Clients | D3, D4 | Hébergeur, prestataire visio | Aucun | Chiffrement des flux ; cible : bout en bout (A24) |
| S02 | Tenue du dossier de téléconsultation | Clients | D1, D2, D3 | Hébergeur | Aucun | Chiffrement, contrôle d'accès, traces |
| S03 | Prise de rendez-vous et rappels | Clients | D1, D5 | Hébergeur, prestataire de notifications | Aucun | Messages sans donnée de santé (A12) |
| S04 | Encaissement des actes | Clients | D7 | Prestataire de paiement | Aucun | Redirection, pas de stockage de carte |
| S05 | Hébergement, sauvegarde et restitution | Clients | D1 à D8 | Hébergeur | Aucun | Sauvegardes chiffrées et isolées (A11) |

Coordonnées à compléter dans la version opérationnelle : identité de chaque client, DPO de Télémédix, DPO des clients qui en ont désigné un.

## 3.7 Justification des choix (arguments d'entretien)

| Choix | Justification |
|---|---|
| Une AIPD type fournie aux clients | Un médecin libéral n'a pas les moyens de mener seul une AIPD sur une plateforme qu'il ne maîtrise pas ; l'aide du sous-traitant est une obligation, et un argument commercial |
| Le consentement écarté comme base légale | Un consentement n'est pas libre quand le refus prive de soins, et il serait révocable à tout moment, ce qui est incompatible avec l'obligation de conserver le dossier |
| Durées fixées par le client | Le sous-traitant ne détermine pas les durées ; il doit en revanche rendre leur application techniquement possible |
| Gravité maximale maintenue | Cohérent avec l'analyse EBIOS RM : mêmes hypothèses, mêmes conclusions |
| Deux registres | Oubli fréquent : un éditeur SaaS est presque toujours à la fois responsable et sous-traitant |
