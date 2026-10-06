# RUNETERRA — JDR
## FICHE RÉSUMÉ : Guide de Combat

*Aide-mémoire condensé. Détails complets dans le Manuel du Joueur, Partie 1, section 7.*

---

## Structure d'un round

Chaque personnage : **1 Action principale + 1 Déplacement** (ordre libre, sauf pendant un Combo). 6 actions possibles : attaque de base, sort, objet actif, aide à un allié, attente/vigilance, fuite.

**Portées** : Contact (0-1 case) · Courte (3m, 2 cases) · Moyenne (8m, 5-6 cases) · Longue (15m+, 10+ cases). 1 case ≈ 1,5m.

---

## Résolution d'une attaque ou d'un sort

1. Annoncer l'action et la cible
2. Jet sur l'**attribut lié** (Seuil = Attribut × 5, + bonus) — **jamais** sur l'AD/AP
3. Si réussite : dégâts = Base + Ratio×AD/AP, + bonus d'affinité fixe si applicable, − Armure/RM de la cible
4. Le degré de réussite module l'effet :

| Degré | Résultat | Effet |
|---|---|---|
| **Critique** (1-5, ou 1-10 en région d'origine) | ≤ 5 ou 10 | Dégâts maximum + effet secondaire d'affinité |
| **Normale** | ≤ Seuil | Dégâts pleins |
| **Échec** | > Seuil | Ça ne passe pas |
| **Échec critique** | 95-100 | Retournement possible contre le lanceur ou un allié |

**Formule de réduction de dégâts** : `Dégâts subis = Dégâts bruts × 100 / (100 + Armure ou RM)`

---

## Repos et récupération

| Type | Fréquence | Effet |
|---|---|---|
| **Court** | Aussi souvent que le rythme le permet | Ressource à 50% du max ; PV via Premiers Secours |
| **Complet** | 1×/jour narratif max | PV et ressource à 100% ; tous les cooldowns remis à zéro |

---

## Le Combo (enchaîner plusieurs compétences)

Jusqu'à 4 compétences (Q/W/E/R) dans le même round. Déplacement possible **avant**, plus du tout après.

| Position | Malus au jet de combo |
|---|---|
| 1ʳᵉ compétence | Aucun (cast normal) |
| 2ᵉ | -10 |
| 3ᵉ | -30 |
| **Ultime (quelle que soit sa position)** | **-50 fixe** |

Le combo s'arrête au premier échec : la compétence ratée + celles non tentées partent en recharge à 50%, sans effet ni coût de ressource. Les compétences réussies avant gardent leur plein effet.

---

## États et altérations

| État | Effet |
|---|---|
| Étourdi | Perd son prochain tour entièrement |
| Ralenti | -1 case de Vitesse de Déplacement (-2 si "ralenti fort") |
| Immobilisé/Enraciné | Ne peut pas se déplacer, peut toujours agir |
| Silence | Ne peut pas lancer de sort, peut attaquer/se déplacer |
| Aveuglé | Désavantage sur tous les jets d'attaque |
| Peur | Doit s'éloigner de la source à son prochain tour |
| Dégât continu | Dégâts fixes au début de chaque tour du porteur |
| Charme/Contrôle mental | Doit exécuter une action décidée par le contrôleur |

Sauf indication contraire, un état dure jusqu'à la fin du prochain tour du porteur ; les réapplications rafraîchissent la durée sans cumuler (sauf mention "cumulable").

---

## Vitesse d'Attaque bonus

Tout bonus au-dessus de 100% = % de chance de déclencher une attaque de base bonus après une attaque réussie. Jet 1d100 : résultat ≤ bonus% = attaque bonus immédiate, gratuite.

---

## Mort et K.O.

- **0 PV** = inconscient (pas mort)
- Chaque tour à 0 PV : jet de Résistance mentale (VOL). Échec = 1 point cumulé ; **3 points = mort**
- Un allié adjacent peut **stabiliser** (jet de Premiers secours ou objet/sort de soin) → repasse à 1 PV
- Une nouvelle attaque subie à 0 PV = mort instantanée, sans jet

---

## Avantage / Désavantage (à la discrétion du MJ)

**Option A (2d100)** : garder le meilleur (avantage) ou le pire (désavantage) des deux jets. Ne se cumule jamais au-delà de 2d100.

**Option B (modificateur direct)** : ±10 (léger) / ±20 (marqué) / ±30 (écrasant) au Seuil de Réussite. Cumulable entre plusieurs facteurs. Seuil final toujours entre 5 et 95.
