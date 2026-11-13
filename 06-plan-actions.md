# 6. Plan d'actions priorisé

Le plan regroupe les mesures issues de l'analyse de risques (dossier 2), de l'AIPD (dossier 3), de la déclaration d'applicabilité (dossier 4) et des matrices d'écarts (dossier 5). Chaque action est identifiée de A01 à A28 et utilisée sous ce même identifiant dans tous les dossiers.

## Méthode de priorisation

| Note | Impact | Effort |
|---|---|---|
| 1 | Amélioration marginale | Moins de 10 jours-homme, sans achat |
| 2 | Réduit un risque moyen ou corrige un écart mineur | 10 à 40 jours-homme, ou achat inférieur à 10 k€ |
| 3 | Réduit un risque élevé de gravité G3, ou plusieurs risques moyens | 40 à 120 jours-homme, ou achat de 10 à 50 k€ |
| 4 | Réduit un risque élevé de gravité G4, ou conditionne une conformité légale | Plus de 120 jours-homme, ou achat supérieur à 50 k€ |

| Quadrant | Règle | Traitement |
|---|---|---|
| Gain rapide | Impact ≥ 3 et effort ≤ 2 | À lancer immédiatement |
| Projet structurant | Impact ≥ 3 et effort ≥ 3 | À planifier avec un budget et un chef de projet |
| Complément | Impact ≤ 2 et effort ≤ 2 | À intégrer au fil de l'eau |
| À arbitrer | Impact ≤ 2 et effort ≥ 3 | À justifier ou à abandonner (aucune action dans ce cas) |

L'échéance est exprimée en mois à partir de la validation du plan (M0).

## Tableau des actions

| ID | Action | Risques couverts | Impact | Effort | Quadrant | Échéance | Pilote | Indicateur de réussite |
|---|---|---|---|---|---|---|---|---|
| A01 | Approuver la PSSI en comité de direction ; lettre de mission du RSSI avec accès direct au DG ; comité sécurité trimestriel | Tous | 3 | 1 | Gain rapide | M1 | DG | PSSI signée ; 4 comités par an |
| A02 | Déployer le SMSI ISO 27001 (inventaire, classification, procédures, audit interne, revue de direction) et obtenir les certifications ISO 27001 et HDS activité 5 | Tous | 4 | 4 | Projet structurant | M18 | RSSI | Certificats obtenus |
| A03 | Qualifier le périmètre HDS (FAQ de l'ANS, avis juridique), arrêter la trajectoire, mettre à jour les contrats clients et hébergeur | Conformité HDS | 4 | 1 | Gain rapide | M2 | DG | Décision formalisée ; contrats revus |
| A04 | Finaliser registres et AIPD ; diffuser l'AIPD type aux clients ; procédure de violation de données (72 h) ; mise à jour des accords de sous-traitance | R09 | 3 | 2 | Gain rapide | M3 | DPO | AIPD validée ; procédure testée |
| A05 | MFA résistant à l'hameçonnage (clés FIDO2) sur tous les accès d'administration : console de l'hébergeur, bastion, dépôt, CI/CD, outils SaaS ; comptes nominatifs ; jetons à durée courte | R01, R03 | 4 | 1 | Gain rapide | M1 | Responsable SRE | 100 % des comptes à privilèges sous MFA |
| A06 | Authentification des professionnels par Pro Santé Connect ; MFA obligatoire en solution de repli | R04 | 4 | 3 | Projet structurant | M6 | Responsable développement | 100 % des connexions de professionnels à deux facteurs |
| A07 | MFA pour les patients avant tout accès à un document médical ; protection contre le test d'identifiants (limitation de débit, refus des mots de passe compromis, alerte de connexion inhabituelle) | R05 | 3 | 2 | Gain rapide | M4 | Responsable développement | Taux de comptes sous MFA ; tentatives bloquées |
| A08 | Encadrer la connexion « en tant que » : justification obligatoire, durée limitée, notification de l'utilisateur, trace dédiée, revue mensuelle | R06 | 3 | 2 | Gain rapide | M4 | Responsable support | 100 % des accès justifiés et revus |
| A09 | Revue trimestrielle des droits ; procédure d'arrivée, de mobilité et de départ ; vérifications à l'embauche pour les postes à privilèges ; séparation des rôles | R06 | 2 | 1 | Complément | M3 | RSSI | Revues réalisées ; comptes orphelins = 0 |
| A10 | Chiffrement applicatif des documents médicaux avec une clé par client, gérée dans un service de gestion de clés ; rotation | R01, R02, R06 | 4 | 3 | Projet structurant | M9 | Responsable développement | 100 % des documents chiffrés |
| A11 | Sauvegardes immuables dans un compte séparé (règle 3-2-1) ; test de restauration trimestriel ; RPO de 1 heure et RTO de 4 heures formalisés | R01, R07 | 4 | 2 | Gain rapide | M3 | Responsable SRE | Restauration réussie chaque trimestre |
| A12 | Supprimer les données de santé des canaux secondaires : messages génériques, masquage dans les journaux, purge des pièces jointes des tickets, libellé bancaire neutre | R09, R10 | 2 | 1 | Complément | M2 | Directeur produit | Contrôle par échantillonnage : 0 donnée de santé |
| A13 | Automatiser les durées de conservation : comptes inactifs, journaux, tickets, restitution et suppression en fin de contrat ; effacement sécurisé des matériels | R09 | 2 | 2 | Complément | M6 | Responsable développement | Purges exécutées et tracées |
| A14 | Contrôle d'autorisation systématique sur chaque objet de l'API ; tests automatisés d'autorisation dans la CI ; exigences de sécurité dès la conception (référentiel OWASP ASVS) | R02 | 4 | 2 | Gain rapide | M3 | Responsable développement | 100 % des points d'accès couverts par un test d'autorisation |
| A15 | Sécuriser la chaîne logicielle : analyse du code, des dépendances et des secrets dans la CI ; inventaire des composants (SBOM) ; versions figées ; artefacts signés ; branches protégées avec double validation | R03 | 4 | 2 | Gain rapide | M4 | Responsable développement | 0 vulnérabilité critique non traitée en production |
| A16 | Test d'intrusion immédiat (le dernier date de 14 mois), puis annuel et après tout changement majeur ; politique de divulgation des vulnérabilités | R02, R04, R05 | 3 | 2 | Gain rapide | M2 | RSSI | Rapport reçu ; corrections critiques sous 30 jours |
| A17 | Séparer strictement les environnements ; données de test synthétiques ; aucune donnée de production en recette | R02, R06 | 3 | 2 | Gain rapide | M5 | Responsable développement | 0 donnée réelle hors production |
| A18 | Centraliser les journaux et les traces d'accès ; règles de détection alignées sur R01 à R06 ; supervision externalisée ; conservation de 12 mois | R01, R02, R05, R06 | 4 | 3 | Projet structurant | M8 | RSSI | Délai de détection ; scénarios couverts |
| A19 | EDR sur les postes et les serveurs ; poste d'administration dédié ; blocage des supports amovibles ; effacement avant réparation | R01, R03 | 3 | 2 | Gain rapide | M4 | Responsable SRE | 100 % du parc couvert |
| A20 | Gestion des vulnérabilités : analyse hebdomadaire, veille CERT-FR et CERT Santé, délais de correction (7 jours pour une vulnérabilité critique, 48 heures si elle est exploitée) | R01, R02 | 3 | 2 | Gain rapide | M3 | Responsable SRE | Respect des délais ≥ 95 % |
| A21 | Cloisonner le réseau de production ; filtrer les flux sortants ; pare-feu applicatif et protection anti-DDoS | R01, R02, R07 | 3 | 3 | Projet structurant | M6 | Responsable SRE | Matrice de flux appliquée ; test de charge réussi |
| A22 | Plan de réponse aux incidents ; cellule de crise et canal de communication de secours ; modèles de notification (clients, CNIL, autorité NIS2) ; exercice annuel | R01, R07 | 4 | 2 | Gain rapide | M4 | RSSI | Exercice réalisé ; notification simulée sous 24 h |
| A23 | Plan de continuité et de reprise testé chaque année ; bascule sur le second site ; mode dégradé par téléphone si la visio est indisponible ; test de réversibilité | R07 | 3 | 3 | Projet structurant | M9 | Responsable SRE | RTO mesuré ≤ 4 h |
| A24 | Visio : chiffrement de bout en bout, ou relais dédiés hébergés sur l'infrastructure HDS ; clauses renforcées ; plan de sortie | R07, R08 | 3 | 3 | Projet structurant | M9 | CTO | Flux illisible par le prestataire |
| A25 | Gestion des tiers : évaluation annuelle, collecte des certificats (HDS, ISO 27001, PCI DSS), clauses de sécurité et de notification, registre des sous-traitants ultérieurs | R03, R07, R08, R09, R10 | 3 | 2 | Gain rapide | M5 | RSSI | 100 % des tiers critiques évalués |
| A26 | Sensibilisation continue ; simulations d'hameçonnage ; formation des dirigeants ; développement sécurisé ; secret médical pour le support | R01, R06 | 3 | 1 | Gain rapide | M3 | RSSI | Participation ≥ 90 % ; taux de clic en baisse |
| A27 | Protéger les clients : guide de sécurité pour les cabinets, alerte de connexion inhabituelle, détection des volumes anormaux d'ordonnances et d'arrêts de travail | R04 | 3 | 2 | Gain rapide | M6 | Directeur produit | Alertes traitées sous 24 h |
| A28 | Veille sur la loi de transposition de NIS2 et ses décrets ; auto-qualification ; analyse d'écart avec le référentiel de l'ANSSI ; enregistrement le moment venu | Conformité NIS2 | 2 | 1 | Complément | M2 | RSSI | Note de qualification à jour |

## Synthèse

| Quadrant | Nombre | Actions |
|---|---|---|
| Gain rapide | 17 | A01, A03, A04, A05, A07, A08, A11, A14, A15, A16, A17, A19, A20, A22, A25, A26, A27 |
| Projet structurant | 7 | A02, A06, A10, A18, A21, A23, A24 |
| Complément | 4 | A09, A12, A13, A28 |
| À arbitrer | 0 | |

## Feuille de route

| Vague | Période | Objectif | Actions |
|---|---|---|---|
| 1. Fermer les portes ouvertes | M1 à M3 | Supprimer les causes directes des risques G4 et poser la gouvernance | A01, A03, A04, A05, A09, A11, A12, A14, A16, A20, A26, A28 |
| 2. Construire les défenses | M4 à M9 | Détection, authentification des utilisateurs, chiffrement, continuité, tiers | A06, A07, A08, A10, A13, A15, A17, A18, A19, A21, A22, A23, A24, A25, A27 |
| 3. Faire reconnaître | M10 à M18 | Audits de certification ISO 27001 et HDS activité 5 | A02 (lancée dès M1) |

## Justification des choix (arguments d'entretien)

| Choix | Justification |
|---|---|
| A05 et A11 en tout premier | Ce sont les deux mesures qui cassent le scénario de rançongiciel (R01) pour un effort faible : sans compte d'administration compromis, pas de prise de contrôle ; avec des sauvegardes hors d'atteinte, pas de perte définitive |
| La certification en dernier | Un certificat constate un système qui fonctionne. Le viser d'abord produit de la documentation sans réduire les risques |
| A03 en gain rapide | La décision coûte peu, mais elle conditionne l'architecture, les contrats et le budget de tout le reste |
| Aucune action « à arbitrer » | Les actions à faible impact et fort effort ont été écartées lors de la construction du plan (par exemple un SOC interne en 24/7) |
| Impact et effort notés sur 4 | Échelle paire : elle interdit la note médiane de confort |
| Indicateur pour chaque action | Une action sans critère de fin ne se termine jamais ; c'est aussi l'exigence d'évaluation de l'efficacité (ISO 27001 clause 9.1, NIS2 art. 21.2.f) |
