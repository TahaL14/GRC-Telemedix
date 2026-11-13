# 2. Analyse de risques EBIOS Risk Manager

Méthode : EBIOS Risk Manager (ANSSI), ateliers 1 à 5. Objet de l'étude : la plateforme Télémédix et ses processus de développement, d'exploitation et de support (périmètre du dossier 1).

| Paramètre de l'étude | Choix |
|---|---|
| Objectif | Identifier les risques numériques, justifier la déclaration d'applicabilité ISO 27001 et bâtir le plan d'actions |
| Participants (fictifs) | DG, CTO, RSSI, responsable SRE, responsable développement, responsable support, DPO, un médecin utilisateur (représentant métier) |
| Cycle stratégique | Révision complète tous les 2 ans ou après un changement majeur |
| Cycle opérationnel | Revue des scénarios opérationnels et du plan d'actions chaque année |
| Cotation de la vraisemblance | Méthode expresse du guide (estimation globale argumentée) |

## Échelles

**Gravité (impact sur les patients, les clients et l'entreprise)**

| Niveau | Libellé | Critères |
|---|---|---|
| G1 | Mineure | Gêne passagère, aucune conséquence sur la prise en charge ni sur la vie privée |
| G2 | Significative | Dégradation du service ou atteinte réversible touchant moins de 100 personnes ; préjudice financier limité |
| G3 | Grave | Divulgation de données de santé ou atteinte à l'intégrité touchant de 100 à 10 000 personnes ; perte de chance ponctuelle pour des patients ; sanction probable, départ de clients |
| G4 | Critique | Divulgation massive et irréversible (plus de 10 000 patients), mise en danger de patients ou perte définitive de dossiers ; survie de l'entreprise menacée |

**Vraisemblance**

| Niveau | Libellé | Critères |
|---|---|---|
| V1 | Peu vraisemblable | L'attaquant devrait franchir plusieurs barrières robustes et indépendantes |
| V2 | Vraisemblable | Réalisable avec des moyens importants ou un concours de circonstances |
| V3 | Très vraisemblable | Réalisable avec des techniques courantes ; mode opératoire observé dans le secteur |
| V4 | Quasi certain | Attaque automatisable, déjà observée ou attendue à court terme |

**Niveau de risque**

| | V1 | V2 | V3 | V4 |
|---|---|---|---|---|
| **G4** | Moyen | Élevé | Élevé | Élevé |
| **G3** | Moyen | Moyen | Élevé | Élevé |
| **G2** | Faible | Faible | Moyen | Moyen |
| **G1** | Faible | Faible | Faible | Faible |

Élevé : inacceptable, à traiter en priorité. Moyen : tolérable sous surveillance, acceptation formelle par la direction. Faible : acceptable.

---

## Atelier 1 : cadrage et socle de sécurité

### Valeurs métier

| Réf. | Valeur métier | Nature | Responsable |
|---|---|---|---|
| VM1 | Réaliser une téléconsultation (visio, audio, messagerie en temps réel) | Processus | Directeur produit |
| VM2 | Tenir le dossier de téléconsultation (comptes rendus, ordonnances, documents) | Information | Directeur produit ; les clients en sont responsables de traitement |
| VM3 | Gérer les identités, les comptes et les rendez-vous | Processus et information | Directeur produit |
| VM4 | Encaisser les actes | Processus | DAF |

### Biens supports

| Réf. | Bien support | Valeurs métier portées | Responsable |
|---|---|---|---|
| BS1 | Applications web et mobiles | VM1 à VM4 | Responsable développement |
| BS2 | API et services applicatifs | VM1 à VM4 | Responsable développement |
| BS3 | Bases de données et stockage de documents | VM2, VM3 | Responsable SRE |
| BS4 | Infrastructure virtuelle, réseau et sauvegardes (hébergeur) | VM1 à VM4 | Responsable SRE ; hébergeur |
| BS5 | Dépôt de code et chaîne CI/CD | VM1 à VM4 | Responsable développement |
| BS6 | Postes d'administration et bastion | VM1 à VM4 | Responsable SRE |
| BS7 | Service de visio (tiers) | VM1 | Prestataire visio |
| BS8 | Service de paiement (tiers) | VM4 | Prestataire de paiement |
| BS9 | Service de notifications (tiers) | VM3 | Prestataire de notifications |
| BS10 | Outils de support (tickets, connexion « en tant que ») | VM2, VM3 | Responsable support |
| BS11 | Personnel à privilèges (SRE, développeurs, support) | VM1 à VM4 | CTO |

### Événements redoutés

| Réf. | Valeur métier | Événement redouté | Critère | Impacts | Gravité |
|---|---|---|---|---|---|
| ER1 | VM2 | Divulgation massive de données de santé | C | Atteinte irréversible à la vie privée, chantage aux patients, sanction CNIL, perte de confiance | G4 |
| ER2 | VM2 | Altération de comptes rendus ou d'ordonnances | I | Erreur de prise en charge, détournement de médicaments | G3 |
| ER3 | VM1 | Indisponibilité de la téléconsultation pendant plus de 4 heures ouvrées | D | Consultations annulées, perte de chance ponctuelle, pénalités contractuelles | G3 |
| ER4 | VM1 | Écoute ou interception de téléconsultations | C | Violation du secret médical | G3 |
| ER5 | VM3 | Usurpation de l'identité d'un professionnel de santé | I | Fausses ordonnances, faux arrêts de travail, responsabilité du praticien engagée | G3 |
| ER6 | VM3 | Prise de contrôle de comptes patients | C | Accès au dossier, usurpation, hameçonnage ciblé | G3 |
| ER7 | VM2 | Perte irréversible de dossiers | D, I | Rupture de la continuité des soins, manquement des clients à leur obligation de conservation | G4 |
| ER8 | VM4 | Fraude ou détournement de paiements | I | Préjudice financier, litiges | G2 |
| ER9 | VM2, VM3 | Consultation illégitime de dossiers par un membre du personnel | C | Violation du secret, plainte, sanction | G3 |

### Socle de sécurité

| Référentiel | Statut | Écarts principaux (détail au dossier 1, §1.7) |
|---|---|---|
| RGPD | Partiellement appliqué | AIPD absente, durées de conservation non automatisées |
| Certification HDS | Hébergeur certifié (activités 1, 2, 3, 6) ; éditeur non certifié | Activité 5 réalisée par l'éditeur sans certification |
| PGSSI-S et services socles (Pro Santé Connect, INS) | Partiellement appliqué | Authentification des professionnels non conforme à la cible |
| Guide d'hygiène informatique de l'ANSSI | Partiellement appliqué | MFA partiel, cloisonnement, journalisation, sauvegardes non testées |
| ISO/IEC 27001:2022 | Non appliqué | Pas de SMSI |
| PCI DSS | Délégué au prestataire | Attestation de conformité du prestataire à collecter chaque année |

Les écarts au socle sont traités directement dans le plan d'actions ; ils alimentent aussi la vraisemblance des scénarios de l'atelier 4.

---

## Atelier 2 : sources de risque et objectifs visés

Cotation de 1 (faible) à 4 (forte). La pertinence combine motivation, ressources et activité observée dans le secteur de la santé.

| Réf. | Source de risque | Objectif visé | Motivation | Ressources | Activité | Pertinence | Retenu |
|---|---|---|---|---|---|---|---|
| SR1 | Groupe cybercriminel organisé | Extorquer l'éditeur par rançongiciel et menace de publication | 4 | 3 | 4 | Élevée | Oui |
| SR2 | Cybercriminel (vol de données) | Voler en masse des données de santé et d'identité pour les revendre | 4 | 3 | 3 | Élevée | Oui |
| SR3 | Fraudeur | Obtenir de fausses ordonnances ou de faux arrêts de travail, détourner des paiements | 3 | 2 | 3 | Élevée | Oui |
| SR4 | Salarié ou prestataire indélicat | Consulter ou exfiltrer des dossiers (curiosité, vengeance, revente) | 2 | 3 | 2 | Moyenne | Oui |
| SR5 | Hacktiviste | Rendre le service indisponible pour nuire à l'image | 2 | 2 | 2 | Moyenne | Oui |
| SR6 | Acteur étatique | Espionner des patients ciblés | 2 | 4 | 1 | Faible | Non |
| SR7 | Concurrent | Voler le code source ou la base clients | 1 | 2 | 1 | Faible | Non |
| SR8 | Attaquant opportuniste isolé | Défi, dégradation | 2 | 1 | 3 | Faible | Non |

**Justification des écarts.** SR6 : la plateforme ne vise pas de population stratégique et l'attaquant dispose de voies plus directes ; à réévaluer si un client sensible est signé. SR7 : aucun cas documenté dans ce secteur, impact limité. SR8 : couvert par le socle (correctifs, durcissement) et par les scénarios de SR2, plus exigeants.

---

## Atelier 3 : scénarios stratégiques

### Cartographie de l'écosystème

Niveau de menace = (dépendance × pénétration) / (maturité cyber × confiance), chaque critère étant coté de 1 à 4.
Seuils retenus : **zone de danger** à partir de 2,5 ; **zone de contrôle** de 1,0 à moins de 2,5 ; **zone de veille** en dessous de 1,0.

| Réf. | Partie prenante | Dépendance | Pénétration | Maturité | Confiance | Niveau de menace | Zone |
|---|---|---|---|---|---|---|---|
| PP1 | Hébergeur HDS | 4 | 4 | 4 | 4 | 1,00 | Contrôle |
| PP2 | Prestataire visio | 4 | 3 | 3 | 3 | 1,33 | Contrôle |
| PP3 | Prestataire de paiement | 2 | 1 | 4 | 4 | 0,13 | Veille |
| PP4 | Prestataire de notifications | 2 | 2 | 2 | 3 | 0,67 | Veille |
| PP5 | Clients : professionnels de santé et leurs postes | 3 | 3 | 1 | 3 | 3,00 | Danger |
| PP6 | Patients et leurs terminaux | 1 | 1 | 1 | 2 | 0,50 | Veille |
| PP7 | Fournisseur du dépôt de code et de la CI/CD (SaaS) | 3 | 4 | 3 | 3 | 1,33 | Contrôle |
| PP8 | Éditeur de l'outil de tickets (SaaS) | 2 | 2 | 3 | 3 | 0,44 | Veille |
| PP9 | ANS (Pro Santé Connect, INSi) | 3 | 2 | 4 | 4 | 0,38 | Veille |
| PP10 | Dépendances logicielles open source | 4 | 4 | 2 | 2 | 4,00 | Danger |

**Lecture.** Les deux parties prenantes les plus dangereuses ne sont pas les sous-traitants contractuels : ce sont les postes des professionnels (non maîtrisés, accès légitime aux dossiers) et les dépendances logicielles (exécutées en production sans relation contractuelle).

### Scénarios stratégiques

| Réf. | Source / objectif | Chemin d'attaque | Parties prenantes | Événements redoutés | Gravité |
|---|---|---|---|---|---|
| SS1 | SR1 : extorsion | Compromission d'un administrateur, prise de contrôle de l'infrastructure, exfiltration puis chiffrement de la production et des sauvegardes | PP1 | ER1, ER3, ER7 | G4 |
| SS2 | SR2 : vol de masse | Exploitation d'un défaut de contrôle d'accès de l'API depuis un compte légitime, extraction automatisée | Aucune | ER1 | G4 |
| SS3 | SR2 : vol de masse | Compromission de la chaîne logicielle (jeton CI/CD ou dépendance piégée), déploiement de code malveillant | PP7, PP10 | ER1, ER2 | G4 |
| SS4 | SR3 : fraude | Vol des identifiants d'un professionnel, émission de fausses ordonnances ou d'arrêts de travail | PP5 | ER5, ER2 | G3 |
| SS5 | SR2 ou SR3 : comptes patients | Réutilisation massive d'identifiants volés ailleurs, accès aux dossiers | PP6 | ER6 | G3 |
| SS6 | SR4 : interne | Usage détourné de la connexion « en tant que » ou d'un accès direct aux bases | Aucune | ER9, ER1 | G3 |
| SS7 | SR5 ou SR1 : indisponibilité | Déni de service sur le front, ou défaillance du prestataire visio ou de l'hébergeur | PP1, PP2 | ER3 | G3 |
| SS8 | SR2 : écoute | Compromission des relais média du prestataire visio | PP2 | ER4 | G3 |
| SS9 | SR2 : canaux secondaires | Compromission du prestataire de notifications ou de l'outil de tickets, récupération des contenus | PP4, PP8 | ER1 (partiel) | G2 |
| SS10 | SR3 : fraude financière | Détournement de paiements ou de remboursements | PP3 | ER8 | G2 |

### Mesures de sécurité sur l'écosystème

| Partie prenante | Mesures (actions du dossier 6) | Effet attendu |
|---|---|---|
| PP5 Clients | A06, A27 | Baisse de la pénétration : l'authentification ne repose plus sur le seul poste du praticien |
| PP10 Dépendances | A15 | Hausse de la maturité : inventaire, versions figées, analyse automatique |
| PP7 Dépôt et CI/CD | A05, A15 | Baisse de la pénétration : jetons à durée courte, MFA, artefacts signés |
| PP2 Visio | A24 | Baisse de la pénétration : chiffrement de bout en bout ; plan de sortie |
| PP1 Hébergeur | A11, A25 | Baisse de la dépendance : sauvegardes isolées ; suivi du certificat |
| PP4, PP8 Notifications et tickets | A12, A25 | Baisse de la pénétration : plus aucune donnée de santé dans ces canaux |

---

## Atelier 4 : scénarios opérationnels

Chaque scénario stratégique donne un risque. Les quatre risques les plus graves sont détaillés selon la séquence Connaître, Rentrer, Trouver, Exploiter.

### R01 : rançongiciel avec double extorsion (SS1)

| Phase | Actions élémentaires | Biens supports |
|---|---|---|
| Connaître | Repérage des administrateurs sur les réseaux professionnels ; les offres d'emploi révèlent la pile technique | BS11 |
| Rentrer | Hameçonnage ciblé d'un SRE et vol de session par un logiciel voleur d'informations ; variante : exploitation d'un accès VPN non corrigé | BS6, BS11 |
| Trouver | Rebond par le bastion, récupération de secrets, accès à la console de l'hébergeur, repérage des sauvegardes | BS4, BS6 |
| Exploiter | Exfiltration des bases et des documents, suppression des sauvegardes, chiffrement des VM, demande de rançon | BS3, BS4 |

Vraisemblance **V3** : MFA absent sur la console, pas d'EDR, sauvegardes accessibles depuis le même compte, aucune détection ; le secteur de la santé est une cible habituelle de ces groupes.

### R02 : extraction massive par défaut de contrôle d'accès (SS2)

| Phase | Actions élémentaires | Biens supports |
|---|---|---|
| Connaître | Création d'un compte patient, analyse de l'application mobile et des appels à l'API | BS1, BS2 |
| Rentrer | Aucune intrusion : l'attaquant agit avec son propre compte authentifié | BS2 |
| Trouver | Découverte d'un point d'accès qui renvoie un document sans vérifier qu'il appartient à l'appelant (référence directe non contrôlée) | BS2 |
| Exploiter | Énumération lente et automatisée des identifiants, extraction des documents, revente | BS3 |

Vraisemblance **V3** : aucun test d'autorisation automatisé, dernier test d'intrusion vieux de 14 mois, aucune alerte sur les volumes consultés. Ce défaut est le plus fréquent sur les API.

### R03 : compromission de la chaîne logicielle (SS3)

| Phase | Actions élémentaires | Biens supports |
|---|---|---|
| Connaître | Identification des dépendances et des développeurs | BS5 |
| Rentrer | Vol d'un jeton d'accès au dépôt sur le poste d'un développeur ; variante : publication d'une version piégée d'une dépendance | BS5, BS11 |
| Trouver | Lecture des secrets de déploiement stockés dans la CI/CD | BS5 |
| Exploiter | Ajout de code qui exfiltre les données ou ouvre une porte dérobée ; déploiement automatique en production | BS2, BS3 |

Vraisemblance **V2** : la revue par un pair existe, mais les secrets de déploiement sont à longue durée de vie et les dépendances ne sont ni figées ni analysées.

### R04 : usurpation d'un compte de professionnel de santé (SS4)

| Phase | Actions élémentaires | Biens supports |
|---|---|---|
| Connaître | Liste des praticiens dans l'annuaire public de la plateforme | BS1 |
| Rentrer | Hameçonnage imitant la page de connexion ; variante : logiciel malveillant sur le poste du cabinet | BS1 |
| Trouver | Accès à l'agenda et aux dossiers du praticien | BS2 |
| Exploiter | Émission d'ordonnances ou d'arrêts de travail au nom du praticien ; consultation des dossiers de ses patients | BS2, BS3 |

Vraisemblance **V3** : second facteur facultatif, postes des cabinets hors de tout contrôle, fraude aux arrêts de travail en ligne déjà observée.

### Autres scénarios opérationnels

| Risque | Scénario (résumé) | Biens supports | Vraisemblance | Justification |
|---|---|---|---|---|
| R05 | Test automatisé de couples identifiant/mot de passe issus de fuites tierces sur l'espace patient, puis accès aux dossiers (SS5) | BS1, BS2 | V4 | Mot de passe seul, pas de limitation de débit avancée ; attaque entièrement automatisée |
| R06 | Un agent du support ou un administrateur consulte ou exporte des dossiers sans besoin (SS6) | BS10, BS3, BS11 | V2 | Fonction « en tant que » sans justification ni revue ; effectif restreint et contractuellement tenu au secret |
| R07 | Saturation du front par déni de service, ou panne prolongée du prestataire visio ou de l'hébergeur (SS7) | BS1, BS4, BS7 | V3 | Pas de protection anti-DDoS dédiée, prestataire visio unique, PRA jamais testé |
| R08 | Compromission des relais média du prestataire : écoute de consultations en cours (SS8) | BS7 | V2 | Flux déchiffré sur le relais ; attaque ciblée et complexe ; rien n'est enregistré |
| R09 | Compromission du prestataire de notifications ou de l'outil de tickets : accès aux messages et pièces jointes (SS9) | BS9, BS10 | V3 | Messages contenant praticien et spécialité ; pièces jointes de tickets jamais purgées |
| R10 | Détournement de paiements ou de remboursements par fraude ou compromission d'un compte (SS10) | BS8 | V2 | Encaissement délégué à un prestataire certifié ; contrôles antifraude du prestataire |

---

## Atelier 5 : traitement du risque

### Synthèse des risques

| Risque | Intitulé | Gravité | Vraisemblance | Niveau initial |
|---|---|---|---|---|
| R01 | Rançongiciel avec double extorsion | G4 | V3 | Élevé |
| R02 | Extraction massive par défaut de contrôle d'accès | G4 | V3 | Élevé |
| R03 | Compromission de la chaîne logicielle | G4 | V2 | Élevé |
| R04 | Usurpation d'un compte de professionnel | G3 | V3 | Élevé |
| R05 | Prise de contrôle de comptes patients | G3 | V4 | Élevé |
| R06 | Consultation illégitime par le personnel | G3 | V2 | Moyen |
| R07 | Indisponibilité prolongée | G3 | V3 | Élevé |
| R08 | Écoute de téléconsultations chez le prestataire visio | G3 | V2 | Moyen |
| R09 | Fuite par les canaux secondaires | G2 | V3 | Moyen |
| R10 | Fraude au paiement | G2 | V2 | Faible |

Dix risques, dont six élevés : un volume cohérent avec cinq couples source/objectif et dix scénarios stratégiques, et pilotable par une équipe de cette taille.

### Cartographie initiale

| | V1 | V2 | V3 | V4 |
|---|---|---|---|---|
| **G4** | | R03 | R01, R02 | |
| **G3** | | R06, R08 | R04, R07 | R05 |
| **G2** | | R10 | R09 | |
| **G1** | | | | |

### Stratégie de traitement et risques résiduels

| Risque | Option | Mesures (actions du dossier 6) | Gravité résiduelle | Vraisemblance résiduelle | Niveau résiduel |
|---|---|---|---|---|---|
| R01 | Réduire | A05, A10, A11, A18, A19, A20, A21, A22, A26 | G4 | V1 | Moyen |
| R02 | Réduire | A10, A14, A16, A17, A18, A20, A21 | G4 | V1 | Moyen |
| R03 | Réduire | A05, A15, A19, A25 | G4 | V1 | Moyen |
| R04 | Réduire | A06, A16, A27 | G3 | V2 | Moyen |
| R05 | Réduire | A07, A16, A18 | G3 | V2 | Moyen |
| R06 | Réduire | A08, A09, A10, A17, A18, A26 | G3 | V1 | Moyen |
| R07 | Réduire | A11, A21, A22, A23, A24, A25 | G3 | V2 | Moyen |
| R08 | Réduire | A24, A25 | G3 | V1 | Moyen |
| R09 | Réduire | A04, A12, A13, A25 | G2 | V2 | Faible |
| R10 | Transférer et réduire | A12, A25 | G2 | V1 | Faible |

### Cartographie résiduelle (après réalisation du plan)

| | V1 | V2 | V3 | V4 |
|---|---|---|---|---|
| **G4** | R01, R02, R03 | | | |
| **G3** | R06, R08 | R04, R05, R07 | | |
| **G2** | R10 | R09 | | |
| **G1** | | | | |

**Acceptation.** Plus aucun risque élevé. Les huit risques résiduels moyens sont soumis à l'acceptation formelle de la direction générale, avec revue annuelle. La gravité des risques R01 à R03 reste G4 : les mesures agissent sur la vraisemblance, pas sur le volume de données exposées. Seul le chiffrement applicatif (A10) limite aussi l'impact, sans le faire changer de niveau.

### Justification des choix (arguments d'entretien)

| Choix | Justification |
|---|---|
| Dix risques | Le guide recommande de retenir quelques couples source/objectif pertinents plutôt que de viser l'exhaustivité ; au-delà d'une quinzaine de risques, une structure de 52 personnes ne peut plus les piloter |
| Risques accidentels absents | EBIOS RM traite les menaces intentionnelles par scénarios ; pannes et erreurs relèvent du socle de sécurité (atelier 1) et de la continuité (A11, A23) |
| Acteur étatique écarté | Écart assumé et tracé ; une étude doit montrer ce qu'elle exclut et pourquoi |
| Méthode expresse | Adaptée à une première itération ; la méthode standard (probabilité et difficulté par action élémentaire) est prévue au prochain cycle opérationnel pour R01 et R02 |
| Gravité inchangée après traitement | Position prudente : promettre qu'une fuite deviendra moins grave grâce à des mesures préventives fausse la décision de la direction |
| Clients et dépendances en zone de danger | Résultat du calcul, pas d'une intuition : faible maturité et forte pénétration pèsent plus que le caractère « externe » d'un sous-traitant certifié |
