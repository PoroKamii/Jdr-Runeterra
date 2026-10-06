# RUNETERRA — JDR
## MANUEL DU JOUEUR (v1.0)

*Tout ce qu'il faut pour créer et jouer un personnage : les règles de base, les origines et rôles, la boutique d'objets, et 36 champions prétirés prêts à jouer. Le Manuel du Maître du Jeu (bestiaire, PNJ, conseils de MJ) est un ouvrage séparé.*

---

# PARTIE 1 — RÈGLES DE BASE

## 1. Philosophie du jeu

Ce système cherche à retranscrire la **sensation de jouer un champion** — passif, trois sorts, un ultime, une montée en puissance progressive — dans un cadre de jeu de rôle narratif se déroulant dans l'univers de Runeterra (Piltover, Zaun, Demacia, Noxus, Freljord, Ionia, Shurima, Bilgewater, les Îles Obscures, etc.).

L'objectif : garder les repères familiers du jeu vidéo (AD, AP, Armure, Résistance Magique, niveaux, objets) tout en laissant la part belle à l'histoire, à l'exploration et au roleplay, contrairement au MOBA d'origine qui est 100% compétitif.

Le respect du lore est une priorité : les factions, régions, tensions politiques et forces surnaturelles (magie du Néant, Runes Anciennes, Formes-Esprit, Hextech/Chimtech...) servent de toile de fond, mais les personnages joueurs sont des **personnages originaux** évoluant dans cet univers — pas des reproductions exactes des champions officiels (ils peuvent s'en inspirer très librement).

---

## 2. La mécanique de base : le d100

Tous les tests utilisent **1d100** (deux d10, un pour les dizaines, un pour les unités — ou un vrai d100).

### 2.1 Résolution d'un test
1. Le joueur additionne sa **Caractéristique** pertinente + son **Bonus de Compétence** (si applicable) → cela donne son **Seuil de Réussite**.
2. Il lance 1d100.
3. **Résultat ≤ Seuil de Réussite → Réussite.** Plus le résultat est bas, meilleure est la réussite (utile en cas d'égalité ou de degré de succès).
4. **Résultat > Seuil de Réussite → Échec.**

### 2.2 Critiques
- **1 à 5 : Réussite Critique** (même si le seuil est dépassé, un jet entre 1 et 5 est presque toujours une réussite spectaculaire — sauf seuil de 0 ou situation jugée impossible par le MJ).
- **95 à 100 : Échec Critique** (une catastrophe narrative, même si le seuil aurait normalement permis la réussite).

*(C'est la convention par défaut : bas = bon, haut = mauvais, comme la majorité des systèmes d100 type BRP/Call of Cthulhu. Si votre groupe préfère l'inverse — haut = bon — il suffit d'inverser cette règle et tous les seuils ; tout le reste du système fonctionne à l'identique.)*

**Bonus régional sur la fenêtre de critique :** dans sa région d'origine (Partie 2, section 1), la fenêtre de Réussite Critique s'élargit de +5, passant de 1-5 à **1-10** — sans toucher à la fenêtre d'échec critique (95-100, inchangée partout).

### 2.3 Avantage / Désavantage contextuel
Le MJ reste libre d'accorder un **avantage** (situation favorable : embuscade, terrain avantageux, information privilégiée, effet de sort allié...) ou d'imposer un **désavantage** (blessure, obscurité, cible protégée, panique...) sur n'importe quel jet, à son appréciation, sans que ce soit codifié à l'avance dans une liste figée. Deux outils sont disponibles, à utiliser selon l'ampleur de l'effet voulu :

**Option A — Jet en 2d100 (effet fort, "tout ou rien") :**
- **Avantage** : lancer **2d100** et garder le **résultat le plus bas** des deux (le meilleur, puisque bas = bon).
- **Désavantage** : lancer **2d100** et garder le **résultat le plus haut** des deux (le pire).
- Les avantages et désavantages multiples ne se cumulent pas au-delà d'un lancer de dé supplémentaire (max 2d100, jamais 3+) — on garde toujours le meilleur/pire des deux.
- Un avantage et un désavantage sur le même jet s'annulent : on revient à un jet normal (1d100).

**Option B — Modificateur direct au Seuil de Réussite (effet gradué, plus précis) :**
Le MJ peut à la place accorder un **bonus** ou infliger un **malus** en points, directement ajouté ou retranché au Seuil de Réussite avant le jet. Barème indicatif :

| Ampleur de la situation | Modificateur |
|---|---|
| Léger avantage/désavantage (ex. bonne/mauvaise position) | ±10 |
| Avantage/désavantage marqué (ex. cible sans défense, terrain très défavorable) | ±20 |
| Avantage/désavantage écrasant (ex. cible endormie, obscurité totale) | ±30 |

Un Seuil de Réussite ne peut jamais dépasser 95 ni descendre sous 5, quels que soient les modificateurs cumulés (pour garder une marge d'échec ou de réussite possible dans tous les cas).

**Quand utiliser quoi ?** Le 2d100 (Option A) est plus rapide pour une situation ponctuelle en combat. Le modificateur en points (Option B) convient mieux quand plusieurs petits facteurs s'accumulent (ex. +10 pour la position en hauteur, -20 pour la cible en armure lourde), puisqu'il peut cumuler plusieurs modificateurs sur un même jet, contrairement au 2d100.

### 2.4 Degrés de réussite (optionnel mais recommandé)
- **Réussite critique (1-5, ou 1-10 en région d'origine)** : effet maximal, bonus narratif.
- **Réussite normale** (résultat ≤ Seuil) : ça passe, dégâts/effet pleins.
- **Échec** (résultat > Seuil) : ça ne passe pas.
- **Échec critique (95-100)** : complication, effet retourné contre le personnage, ou pire.

### 2.5 Jets opposés
Les deux parties lancent un d100 contre leur seuil respectif. Celui qui obtient le meilleur **degré de réussite** l'emporte (critique > normale). En cas d'égalité de degré, le résultat le plus bas gagne.

---

## 3. Caractéristiques de personnage

### 3.0 Comment se calcule une statistique de combat

Toute statistique de combat (PV, AD, AP, Armure, RM) passe par le même enchaînement de 5 étapes :

```
1. Archétype de combat (Tank, Juggernaut, Assassin, Mage, Marksman, Support) → valeur de départ (3.3)
2. + Modificateur de sous-rôle (Partie 2, 4.1) → multiplie PV et dégâts
3. + Bonus d'attribut (tableau ci-dessous) → calculé depuis tes 6 attributs
4. + Bonus d'objets (Partie 3)
5. + Bonus fixe d'affinité élémentaire si applicable (Partie 2, 5.1) → s'ajoute avant la réduction d'Armure/RM de la cible, jamais un multiplicateur (détail et exemple chiffré en section 3.4ter)
= Statistique finale utilisée en jeu
```

**Étape 3 en détail — ce que chaque attribut impacte :** chaque attribut au-dessus ou en-dessous de 10 (le score "neutre") ajoute ou retire un bonus fixe à une seule stat de combat précise :

| Attribut | Stat affectée | Bonus par point au-dessus de 10 |
|---|---|---|
| **CON** | PV | +6 PV par point |
| **FOR** | AD | +1 AD par point |
| **INT** | AP | +2 AP par point |
| **VOL** | Résistance Magique | +1 RM par point |
| **DEX** | Vitesse d'Attaque / Initiative | +1% Vitesse d'Attaque, +1 Initiative par point |
| **CHA** | *(aucun effet en combat)* | Sert uniquement aux tests sociaux et à la réputation (Partie 2) |

*(L'Armure est la seule exception au principe ci-dessus : elle ne dépend que du rôle et des objets, jamais des attributs.)*

**Exemple chiffré — un Tank (CON 15, FOR 14, DEX 12, VOL 12, CHA 11, INT 8) :**
```
PV (niveau 1)  = 65 (base Tank) + [(15-10) × 6]   = 65 + 30   = 95 PV
PV (niveau 18) = 224 (base Tank) + [(15-10) × 6]  = 224 + 30  = 254 PV
AD              = 10 (base Tank)  + [(14-10) × 1]   = 10 + 4    = 14 AD
RM              = 20 (base Tank)  + [(12-10) × 1]   = 20 + 2    = 22 RM
Vitesse d'Attaque = base + [(12-10) × 1%]           = +2% par rapport à la moyenne
AP              = 0 (base Tank)   + [(8-10) × 2]    = 0 - 4     = -4 AP (arrondi à 0, l'AP ne descend jamais sous 0)
```

### 3.1 Attributs primaires — point-buy à coût croissant (façon D&D 5e)

Chaque attribut se situe entre **8 et 15** à la création (avant bonus racial), avec un coût qui augmente plus on vise haut — exactement le principe utilisé dans D&D 5e, bien connu et facile à équilibrer :

| Valeur finale | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|
| **Coût en points** | 0 | 1 | 2 | 3 | 4 | 5 | 7 | 9 |

**Pool évolutif : 21 points à la création, jusqu'à 27 au niveau 18.** Le personnage démarre avec 21 points à répartir entre les 6 attributs (FOR, DEX, CON, INT, VOL, CHA), à dépenser dans ce tableau de coûts. Ce pool gagne ensuite **+1 point automatiquement aux niveaux 3, 6, 9, 12, 15 et 18** (6 paliers), pour atteindre 27 points au niveau 18 — remplaçant l'ancien système de point fixe gagné séparément (voir 5.4, fusionné dans ce pool évolutif). Les points gagnés en montant de niveau se dépensent dans le même tableau de coûts ci-dessus et peuvent être répartis librement entre les 6 attributs, y compris sur un attribut déjà monté à la création.

| Attribut | Utilité |
|---|---|
| **Force (FOR)** | Dégâts physiques bruts, athlétisme, port de charge |
| **Dextérité (DEX)** | Précision, esquive, initiative, discrétion |
| **Constitution (CON)** | Points de Vie, résistance à l'épuisement/poison |
| **Intelligence (INT)** | Sorts, connaissance, artisanat (Hextech, alchimie...) |
| **Sagesse/Volonté (VOL)** | Résistance mentale, perception, canalisation d'énergie spirituelle |
| **Charisme (CHA)** | Persuasion, présence, intimidation, leadership |

Ce système permet naturellement d'avoir **1 ou 2 attributs à 8** (en dessous de la moyenne, comme demandé) tout en montant significativement ailleurs — sans qu'un joueur soit obligé de "sacrifier" quoi que ce soit s'il préfère un profil plus généraliste.

**Recommandations indicatives par sous-rôle (non obligatoires)** — un simple repère, à ignorer pour un concept atypique. La liste complète des 15 sous-rôles avec leur attribut recommandé se trouve au Partie 2, section 4.1 (tableau des modificateurs mécaniques) : par exemple un Tank vise plutôt CON 13+, un Artilleur ou un Control Mage vise INT 14+, un Assassin ou un Sniper vise DEX 13-14+, etc.

**Exemple 1 — build équilibré (array classique) :**
```
FOR 15 · CON 14 · DEX 13 · INT 12 · VOL 10 · CHA 8   (coût total = 9+7+5+4+2+0 = 27)
```

**Exemple 2 — "brute bête" (Juggernaut, INT et CHA sacrifiés à 8) :**
```
FOR 15 · CON 15 · DEX 13 · VOL 12 · INT 8 · CHA 8   (coût total = 9+9+5+4+0+0 = 27)
```

**Exemple 3 — Mage spécialisé (FOR à 8, tout misé sur INT) :**
```
INT 15 · VOL 14 · CON 13 · DEX 11 · CHA 11 · FOR 8   (coût total = 9+7+5+3+3+0 = 27)
```

*(Le bonus racial du Partie 2 s'ajoute par-dessus ces valeurs, et peut donc pousser un attribut au-delà de 15, jusqu'à 18 maximum.)*

### 3.2 Statistiques de combat (directement héritées du jeu vidéo)

Toutes suivent le pipeline en 5 étapes de la section 3.0 (Base d'archétype 3.3 × modificateur de sous-rôle 2/4.1 + bonus d'attribut 3.0 + objets) — le tableau ci-dessous ne précise que ce qui change d'une stat à l'autre : quel attribut l'alimente, et les exceptions à la règle générale.

| Stat | Description | Attribut qui l'alimente (3.0) |
|---|---|---|
| **PV (Points de Vie)** | Santé du personnage | CON |
| **Ressource** (Mana / Énergie / Fureur / Sans ressource, au choix — voir 3.2bis) | Alimente les sorts actifs | *(hors pipeline — voir 3.2bis pour la réserve et la régénération de chaque type)* |
| **AD (Attaque Physique)** | Dégâts des attaques de base et sorts "physiques" | FOR |
| **AP (Puissance Magique)** | Dégâts des sorts "magiques" | INT |
| **Armure** | Réduit les dégâts physiques | *(exception : aucun bonus d'attribut — juste base + objets)* |
| **Résistance Magique (RM)** | Réduit les dégâts magiques | VOL |
| **Vitesse d'Attaque** | Nombre d'attaques de base par round | DEX (+ bonus fixes d'objets/sorts, déjà en %) |
| **Vitesse de Déplacement** | Cases/mètres franchissables par round | *(pas d'attribut — base 6 cases modifiée par le sous-rôle, Partie 2 4.1)* |
| **Chance de Critique** | % de dégâts x1,5 sur attaque de base | *(pas d'attribut — base 0%, via objets uniquement)* |
| **Réduction de Délai de Récupération (CDR)** | Réduit le temps de recharge des sorts | *(pas d'attribut — base 0%, cap 40%)* |
| **Vol de Vie / Sustain** | % des dégâts infligés rendus en PV | *(pas d'attribut — selon objets/sorts uniquement)* |

**Comment utiliser un bonus de Vitesse d'Attaque en jeu :** tout bonus au-dessus de 100% (qu'il vienne d'un objet, d'un attribut ou d'un sort comme l'Ultime de Vayne) se traduit en **% de chance de déclencher une attaque de base bonus**, immédiatement après une attaque de base réussie. Après avoir touché avec une attaque de base, lance 1d100 : résultat ≤ au bonus de Vitesse d'Attaque (en %) = une seconde attaque de base se déclenche aussitôt, sans consommer d'action supplémentaire. *Exemple : Vayne avec +20% Vitesse d'Attaque (son Ultime) touche une attaque de base, lance 1d100, obtient 15 → 15 ≤ 20, elle attaque une seconde fois immédiatement.*

**Formule de réduction de dégâts (simplifiée) :**
`Dégâts subis = Dégâts bruts × 100 / (100 + Armure ou RM selon le type)`

### 3.2bis Types de ressource

Chaque personnage choisit librement, à la création, le type de ressource qui alimente ses sorts : **Mana**, **Énergie**, **Fureur/Rage**, ou **Sans ressource** (sorts limités uniquement par leur temps de recharge). Ce choix est indépendant du sous-rôle — un Mage peut fonctionner à la Fureur, un Juggernaut au Mana, etc., selon la cohérence narrative voulue avec ses compétences.

Pour simplifier les calculs, **le coût d'un sort s'exprime en pourcentage de la réserve maximum**, pas en valeur fixe — ça évite d'avoir à recalculer les coûts à chaque fois que la réserve grandit avec le niveau.

**Coût standard des sorts (identique pour tous les types de ressource) :**

| Emplacement | Coût |
|---|---|
| Q ou E | 10% de la réserve maximum |
| W | 15% de la réserve maximum |
| Ultime (R) | 25% de la réserve maximum |

**Mana**
- Réserve maximum : `30 + (INT × 2)` au niveau 1, progression standard (+60% au niveau 18, comme l'AP/AD)
- Régénération : intégralement entre deux scènes/repos ; **10% de la réserve max par round** en combat
- Ressource la plus généraliste, utilisée par la majorité des Mages, Supports et Marksmen

**Énergie**
- Réserve fixe : **100**, ne varie pas avec les attributs ni le niveau
- Régénération : **20% par round**, automatiquement — la ressource la plus rapide à reconstituer
- Pensée pour l'explosivité (Assassins) : peu de réserve, mais toujours prête à se recharger vite

**Fureur / Rage**
- Réserve maximum : **100**, ne se remplit qu'en combat
- Génération : **+10 par attaque portée ou subie** (au contact) ; se vide de **20 par round hors combat**
- Un personnage doit "chauffer" en frappant/encaissant avant de pouvoir lancer ses sorts payants — cohérent avec Juggernaut/Skirmisher

**Sans ressource**
- Aucune jauge à suivre : les sorts ne sont limités que par leur temps de recharge (section 5.1, cooldown)
- Typique des Juggernauts/Tanks purs, pour rester simple à jouer

---

### 3.3 Fourchettes de statistiques par archétype de combat (dérivées des vrais ratios LoL)

Les valeurs ci-dessous ne sont pas les vraies stats du jeu vidéo (impossible à transposer telles quelles), mais elles respectent les **mêmes proportions entre rôles** que celles observées sur le wiki officiel. Un Juggernaut du JDR doit "sentir" comme Garen ou Darius : lent, très résistant, brutal au contact. Un Assassin doit "sentir" comme Zed ou Akali : fragile mais explosif.

| Rôle | PV (niv.1 → niv.18) | Armure / RM (base) | AD (base) | AP (scaling) | Vitesse Dépl. | Portée | Ressource |
|---|---|---|---|---|---|---|---|
| **Tank / Vanguard** (ex. Nautilus, Malphite, Amumu) | 65 → 224 | 20 / 20 | 10 | — | Normale | Contact/courte | Mana |
| **Juggernaut / Fighter** (ex. Garen, Darius, Illaoi) | 59 → 212 | 16 / 14 | 14 | — | **-1 (la plus faible)** | **Contact uniquement** | Faible/Sans ressource |
| **Assassin** (ex. Zed, Akali, Talon) | 44 → 165 | 10 / 10 | 13 (burst) | Ou AP selon assassin | **+1 (la plus haute)** | Courte, burst | Énergie ou Mana réduit |
| **Mage / Battlemage** (ex. Annie, Anivia, Ryze) | 44 → 159 | 8 / 12 | 6 | **16-20** | Normale | Moyenne/longue | Mana élevé |
| **Marksman / Tireur** (ex. Ashe, Caitlyn, Jinx) | 44 → 171 | 9 / 9 | 11 (scaling objets) | — | Normale | **Longue** | Mana modéré |
| **Support / Enchanter-Catcher** (ex. Janna, Lulu, Thresh) | 47 → 153 | 9 / 11 | 5 | 8-10 (soin/CC) | Normale | Moyenne | Mana élevé |

*(Ces fourchettes sont un point de départ. Le MJ peut ajuster ±10% pour équilibrer son groupe.)*

*Note de terminologie : les 6 lignes ci-dessus sont des **archétypes de combat** (Tank, Juggernaut, Assassin, Mage, Marksman, Support), qui déterminent les stats de base. Le terme **"Rôle"** utilisé au Partie 2 (TOP, JUNGLE, MID, ADC, SUPPORT) désigne la position du personnage dans le groupe, pas son archétype de stats — un Rôle TOP peut par exemple utiliser l'archétype Tank, Juggernaut ou Assassin/Bruiser selon le sous-rôle choisi.*

### 3.4 Ratios AD/AP dans les sorts
Comme dans le vrai jeu, chaque sort doit avoir un **ratio de scaling** indiquant combien il profite de l'AD ou l'AP du personnage. Fourchettes recommandées pour rester dans l'esprit du jeu vidéo :
- **Sort de dégâts simple (Q/E)** : 0.4 à 0.7 AD ou AP
- **Sort de dégâts fort (W)** : 0.6 à 1.0 AD ou AP
- **Ultime (R)** : 0.8 à 1.5 AD ou AP (voire plus pour un ultime "execute" à la Darius)
- **Sort utilitaire/soin/CC** : pas de ratio de dégâts, ou un ratio réduit (0.2-0.4) sur l'effet secondaire

Exemple concret (Juggernaut au style Darius) :
```
E - Coup de Talon
Type : Physique
Coût : Sans ressource (cooldown pur)
Recharge : 3 rounds
Portée : Contact
Effet : Repousse la cible en arrière + 8 (+0.6 AD) dégâts physiques
```

### 3.4ter Lien avec l'affinité élémentaire (Partie 2, section 5)
L'affinité élémentaire (Eau, Feu, Foudre, Terre, Néant, Lumière) est désormais ouverte à tout le monde, pas seulement aux lanceurs de sorts. Ses bonus/malus **ne modifient jamais l'AD ou l'AP eux-mêmes** — ils s'ajoutent en dernier, comme un **bonus de dégâts fixe** (physiques ou magiques selon le sous-rôle du personnage), une fois l'AD ou l'AP déjà pris en compte.

**Ordre de calcul complet (attaque ou sort, physique ou magique) :**
```
1. Dégâts de base (attaque ou sort, défini au rang de la compétence)
2. + Ratio d'AD ou d'AP × valeur totale du personnage
3. + Bonus fixe d'affinité élémentaire si la situation s'y prête (ex. +1d4 si Feu sur cible déjà brûlée)
4. − Réduction d'Armure ou de Résistance Magique de la cible (formule section 3.2, selon le type de dégâts)
= Dégâts finaux infligés
```

**Exemple chiffré (magique)** — Battlemage Feu, 60 AP, sort rang 3 (base 40, ratio 0.6), cible déjà brûlée (1d4 = 3), 20 RM :
```
1. Base : 40
2. + Ratio AP : 40 + (0.6 × 60) = 76
3. + Bonus Feu : 76 + 3 = 79
4. − RM (20) : 79 × 100/(100+20) = 66 dégâts magiques finaux
```

**Exemple chiffré (physique)** — Bruiser Feu, 20 AD, attaque de base (ratio 1.0), cible déjà brûlée (1d4 = 3), 15 Armure :
```
1. Base : 0 (attaque de base pure)
2. + Ratio AD : 0 + (1.0 × 20) = 20
3. + Bonus Feu : 20 + 3 = 23
4. − Armure (15) : 23 × 100/(100+15) = 20 dégâts physiques finaux
```

### 3.5 Liste d'actions neutres (jets communs)

Ces actions sont utilisables par n'importe quel personnage, indépendamment de son rôle ou sous-rôle — elles servent de base pour tous les jets qui ne sont pas une compétence de personnage (Passif/Q/W/E/R), et c'est sur elles que se greffent les bonus de sous-rôle (Partie 2, section 4.1).

| Action | Attribut lié | Utilisation typique |
|---|---|---|
| **Attaque en mêlée** | FOR ou DEX | Toucher une cible au contact |
| **Attaque à distance** | DEX | Toucher une cible avec une arme à distance |
| **Sort magique** | INT | Lancer un sort offensif ou utilitaire |
| **Esquive** | DEX | Éviter une attaque |
| **Résistance mentale** | VOL | Résister à la peur, la panique, un contrôle mental |
| **Concentration** | VOL | Maintenir un sort actif sous pression ou en prenant des dégâts |
| **Discrétion** | DEX | Se cacher, ne pas être repéré |
| **Perception** | VOL | Repérer un danger, une embuscade, un mensonge évident |
| **Enquête** | INT | Analyser un indice, déduire, fouiller méthodiquement une scène |
| **Survie** | VOL | Suivre une piste, s'orienter en milieu sauvage, trouver de la nourriture/un abri |
| **Premiers secours** | INT | Stabiliser un allié à terre, soigner une blessure sans magie |
| **Athlétisme** | FOR | Grimper, sauter, nager, forcer un passage |
| **Persuasion** | CHA | Convaincre, négocier honnêtement |
| **Tromperie** | CHA | Mentir de façon convaincante, se faire passer pour quelqu'un d'autre |
| **Intimidation** | CHA ou FOR | Effrayer, forcer une réaction |
| **Escamotage** | DEX | Crochetage, vol à la tire, manipulation discrète d'un objet |
| **Érudition** | INT | Connaissances, histoire, artisanat |

*(Liste inspirée des compétences classiques qu'on retrouve dans D&D 5e et les systèmes d100 type Call of Cthulhu/BRP, adaptée à nos 6 attributs.)*

Le Seuil de Réussite pour ces actions suit la règle suivante : **Seuil de Réussite = Attribut lié × 5**, puis on ajoute les bonus éventuels (sous-rôle, situationnel). Ce ×5 est ce qui transforme un attribut (8 à 18) en un vrai pourcentage de réussite jouable sur d100 — c'est la même convention que les systèmes d100 classiques type Call of Cthulhu. Les bonus de sous-rôle s'ajoutent par-dessus, exactement comme le modificateur direct de la section 2.3 (Option B), et le Seuil final reste toujours borné entre 5 et 95 (section 2.3).

### 3.5bis Réussite vs Puissance — le rôle exact des stats dérivées

Point important à bien distinguer : **l'attribut brut détermine si l'action réussit, les stats dérivées (AD, AP, Armure, RM...) déterminent seulement ce qui se passe une fois qu'elle a réussi.** Les deux n'interviennent jamais au même moment.

| Étape | Ce qui compte | Exemple |
|---|---|---|
| **Le jet de réussite** (d100) | Uniquement l'**attribut** lié à l'action (section 3.5), + bonus de sous-rôle éventuel | Une "Attaque à distance" se joue sur DEX, jamais sur l'AD |
| **Si l'action réussit et inflige des dégâts** | L'**AD ou l'AP** du personnage, via le ratio de la compétence (section 3.0/3.4) | Le montant de dégâts dépend de l'AD, pas de la réussite du jet |
| **Ce que la cible encaisse** | L'**Armure ou la RM** de la cible réduit les dégâts reçus (section 3.2) | Un personnage à forte Armure encaisse moins, quel que soit son propre jet |
| **Le rythme du combat** | **Vitesse d'Attaque** (attaques bonus), **Vitesse de Déplacement** (cases franchies), **Initiative** (ordre de jeu), **CDR** (recharge des sorts) | Ces stats ne touchent jamais un jet de d100, elles cadencent le combat |
| **Les effets additionnels** | **Vol de Vie** (soin au contact), **Chance de Critique** (bonus de dégâts x1,5 sur attaque de base) | S'ajoutent après un jet réussi, indépendamment du degré de réussite du d100 |

**En clair :** un personnage avec un gros AD ne touche pas plus souvent sa cible qu'un autre — il tape juste plus fort quand il touche. C'est la DEX (ou l'attribut lié à l'action) qui détermine la précision, l'AD/AP qui détermine la puissance de l'impact. Ça évite qu'un personnage stack uniquement des dégâts et devienne injouable en contre-partie (il touchera toujours avec la même fiabilité que les autres, seule la sanction en cas de réussite change).

*Note sur la Chance de Critique (stat d'objets) vs le critique du d100 (section 2.2) : ce sont deux mécaniques distinctes qui se cumulent. Le critique du d100 (résultat 1-5, ou 1-10 en région d'origine) est un critique "narratif" qui s'applique à n'importe quel jet. La Chance de Critique (issue des objets, ex. Lame d'Infini) est un pourcentage de proc supplémentaire qui s'ajoute uniquement sur les attaques de base, comme dans le jeu vidéo — les deux peuvent se déclencher sur la même attaque.*

---

## 4. Création de personnage — étapes

1. **Origine (région de Runeterra)** — voir Partie 2, section 1 : donne un trait culturel, un bonus régional, et une fenêtre de critique élargie sur son propre terrain.
2. **Race** — voir Partie 2, section 2.
3. **Rôle et sous-rôle** (TOP/JUNGLE/MID/ADC/SUPPORT, 15 sous-rôles au total) — voir Partie 2, section 4. Détermine l'archétype de combat de base (section 3.3) et les stats de départ.
4. **Répartition des attributs en point-buy (21 points à la création, jusqu'à 27 au niveau 18, coût croissant)** — voir section 3.1.
5. **Choix du Passif + 3 Sorts (Q/W/E) + 1 Ultime (R)** — voir section 5.
6. **Objet de départ** — un objet signature selon le sous-rôle + 2 Potions de Soin (voir Partie 3, section 7). **Or de départ : 0 po** (comme dans le jeu vidéo, on part les mains presque vides) — sauf exception ponctuelle liée à l'historique du personnage (ex. un noble déchu, un marchand ruiné), au jugement du MJ et rarement au-delà de 20-50 po. Chaque personnage reçoit aussi gratuitement un **Kit d'aventurier** (équipement non-combat, voir Partie 3, section 0bis) qui ne prend aucun des 6 emplacements d'objets.
7. **Historique et lien avec le groupe** — pourquoi ce personnage voyage-t-il avec les autres ? Voir le **Questionnaire de Background** (version Joueur à remplir avant la session 0, version MJ pour guider la discussion) pour construire cette étape en profondeur plutôt qu'en une seule phrase.

---

## 5. Compétences de personnage : Passif, Q/W/E, Ultime

Chaque personnage dispose de **5 compétences**, exactement comme un champion :

- **Passif** : effet permanent ou déclenché automatiquement (pas de coût, pas de temps de recharge).
- **Q, W, E** (3 sorts actifs) : coût en Ressource (Mana/Énergie/Fureur/Sans ressource, section 3.2bis) + temps de recharge (en rounds) + rang (1 à 5).
- **R (Ultime)** : sort le plus puissant, rang 1 à 3, débloqué au niveau 6, temps de recharge long (nécessite plusieurs rounds voire plusieurs scènes).

### 5.1 Gabarit de sort (à remplir pour chaque compétence créée)
```
Nom du sort :
Type : Physique / Magique / Utilitaire / Soin / Contrôle
Coût : X% de la réserve (Mana/Énergie/Fureur) ou Sans ressource (section 3.2bis)
Temps de recharge : X rounds (réduit par le CDR)
Portée : contact / courte (3m) / moyenne (8m) / longue (15m+)
Effet au rang 1 :
Effet au rang 5 (max) :
Interaction avec AD/AP : ex. "inflige 1d6+4 (+0.5 AD) dégâts physiques"
```

### 5.1bis Mémo de création rapide (fourchettes par type de compétence)

Pour remplir le gabarit ci-dessus sans partir d'une page blanche ni déséquilibrer le jeu, voici des fourchettes de référence pour chaque type de compétence, croisées avec l'emplacement (Q/E, W ou Ultime). La base de dégâts/soin utilise des dés classiques plutôt qu'un chiffre plat imposé — lance-les à la création pour fixer ta valeur définitive, ou prends la moyenne si tu préfères un perso figé sans hasard à la création.

**Dégâts mono-cible**

| Emplacement | Dé de base | Ratio AD/AP | Recharge indicative |
|---|---|---|---|
| Q ou E | 1d6 à 2d6 | 0,4 à 0,7 | 2 à 4 rounds |
| W | 2d6 à 2d8 | 0,6 à 1,0 | 3 à 5 rounds |
| Ultime (R) | 2d8 à 3d10 | 0,8 à 1,5 | 5+ rounds, ou 1×/combat |

**Dégâts multi-cible (zone)** — toujours inférieurs au mono-cible du même emplacement, pour compenser le fait de toucher plusieurs ennemis :

| Emplacement | Dé de base | Ratio AD/AP | Recharge indicative |
|---|---|---|---|
| Q ou E | 1d4 à 1d6 | 0,3 à 0,5 | 3 à 5 rounds |
| W | 1d6 à 2d6 | 0,4 à 0,7 | 4 à 6 rounds |
| Ultime (R) | 1d10 à 2d10 | 0,6 à 1,0 | 1×/combat |

**Dégâts sur la durée (DoT — brûlure, poison, saignement...)**

| Emplacement | Dégâts par round | Durée | Ratio (si scaling) |
|---|---|---|---|
| Q ou E | 1d4 | 2 à 3 rounds | 0,1 à 0,2 |
| W | 1d6 | 2 à 3 rounds | 0,15 à 0,25 |
| Ultime (R) | 2d6 | 3 à 4 rounds | 0,2 à 0,3 |

**Soin**

| Emplacement | Dé de base | Ratio (AP surtout) | Recharge indicative |
|---|---|---|---|
| Q ou E | 1d6+2 à 2d6 | 0,3 à 0,5 | 2 à 4 rounds |
| W | 2d8 à 3d8 | 0,5 à 0,8 | 3 à 5 rounds |
| Ultime (R) | 3d10, ou relève un allié K.O. | 0,8 à 1,2 | 1×/combat |

**Contrôle pur (sans dégâts)**

| Emplacement | Effet | Durée | Recharge indicative |
|---|---|---|---|
| Q ou E | Ralenti, léger désavantage | 1 à 2 rounds | 2 à 3 rounds |
| W | Étourdi, immobilisé, silence | 1 round | 3 à 4 rounds |
| Ultime (R) | Contrôle massif en zone, ou durée doublée | 1 à 2 rounds sur zone | 1×/combat |

**Utilitaire / Mobilité**

| Emplacement | Effet type |
|---|---|
| Q ou E | Dash de 3 à 5m, invisibilité 1 round, détection courte portée |
| W | Bouclier temporaire, purge d'un état négatif, mobilité d'équipe |
| Ultime (R) | Effet de zone massif (téléportation d'équipe, changement de terrain), généralement 1×/combat |

**Buff (bonus temporaire à soi ou un allié)**

| Emplacement | Intensité | Durée |
|---|---|---|
| Q ou E | +10% à une stat | 2 rounds |
| W | +20% à une stat, ou bouclier équivalent à quelques PV | 2 à 3 rounds |
| Ultime (R) | Buff d'équipe entier, effet marqué | 3+ rounds |

**Passif** (toujours actif, sans coût en ressource ni temps de recharge — reste volontairement plus modeste qu'une compétence active pour compenser sa permanence)

| Type de passif | Fourchette indicative |
|---|---|
| Dégâts bonus (déclenché) | +1d4 dégâts tous les 3-4 coups portés, ou +5 à 10% de dégâts dans une condition précise (voir aussi les bonus de sous-rôle, Partie 2 section 4.1) |
| Défensif | Réduction fixe de 2 à 4 dégâts par attaque subie, ou +5 à 10% Armure/RM |
| Soin / Sustain | Régénère 2 à 5 PV par round, généralement sous condition (hors combat, au contact d'un élément, sous un seuil de PV...) |
| Contrôle occasionnel | Un effet mineur (ralenti bref, léger désarmement) uniquement en cas de réussite critique — jamais un effet fort de façon garantie |
| Utilitaire | +1 case de Vitesse de Déplacement, détection à courte portée, ou résistance à un état précis |

Un passif n'a normalement pas de ratio AD/AP (ou un ratio très faible, 0,1 maximum, si vraiment nécessaire) : sa force vient de sa permanence, pas de sa puissance brute par activation.

*(Ces fourchettes restent indicatives — le MJ garde toujours le dernier mot si une combinaison semble abusive en pratique, mais elles suffisent à éviter les écarts flagrants entre les compétences des différents joueurs à la création.)*

#### Types additionnels (moins courants, mais bien présents dans le vrai jeu)

Après vérification sur des exemples réels de champions, quelques types de compétences méritent leur propre repère, même s'ils sont plus rares à la table :

| Type | Description | Fourchette indicative |
|---|---|---|
| **Invocation** (façon Tibbers, Daisy, Voidling) | Invoque une créature ou un pantin qui combat à ses côtés pendant un temps limité | PV de l'invocation ≈ 30-50% des PV du lanceur, dégâts ≈ 50-70% de l'AD/AP du lanceur, durée 2-4 rounds, généralement en W ou Ultime |
| **Transformation** (façon Elise, Nidalee, Gnar) | Change temporairement de forme, avec des stats et parfois des compétences différentes | À utiliser avec prudence : la forme alternative ne doit pas cumuler tous les avantages des deux formes à la fois (ex. plus de PV OU plus de dégâts, rarement les deux) |
| **Portée globale** (façon Ezreal, Twisted Fate, Shen) | Utilisable n'importe où sur la carte/la zone de jeu, sans limite de portée classique | Réservé à l'Ultime, cooldown long (1×/combat ou 1×/scène), dégâts ou effet réduits de 20-30% par rapport à un Ultime à portée normale pour compenser |
| **Anti-soin** (façon Grievous Wounds — Darius, Varus, Renekton) | Réduit les soins et la régénération reçus par la cible touchée (généralement -40 à -50%) pendant 2-3 rounds | S'ajoute facilement à un Q ou E existant comme effet secondaire, sans coût de conception supplémentaire notable |
| **Exécution** (façon Evelynn, Darius, Pyke, Vayne) | Dégâts bonus significatifs contre une cible sous un certain seuil de PV (souvent 20-30%) | Bonus de +30 à +50% de dégâts sous le seuil, réservé au W ou à l'Ultime |
| **Furtivité / Intouchable** | Devient indétectable ou insensible aux dégâts/contrôles pendant un court instant | 1 round maximum en Q/E, jusqu'à 2 rounds en Ultime ; briser la discrétion en attaquant reste la norme, sauf mention contraire |
| **Résurrection** (façon Zilean, Anivia, Soraka) | Ramène un allié (ou soi-même) d'entre les K.O., ou empêche la mort une fois | Réservé exclusivement à l'Ultime, cooldown très long (1× par campagne/arc narratif, à l'appréciation du MJ plutôt qu'un simple cooldown de rounds) |
| **Modification du terrain** (façon Anivia, Trundle, Taliyah) | Crée un obstacle temporaire (mur, pilier) qui bloque le passage ou la ligne de vue | Généralement en W, durée 2-3 rounds, cooldown 4-5 rounds ; le MJ arbitre les cas limites (contournement, destruction) |

### 5.1ter Règle de montée en rang

Quand une compétence à dégâts/soin chiffrés monte de rang (Partie 1, section 5.2), elle gagne automatiquement :
- **Q, W ou E** : **+2 aux dégâts/soin fixes** et **+0,1 au ratio AD/AP**, par rang (jusqu'au rang 5)
- **Ultime (R)** : **+4 aux dégâts/soin fixes** et **+0,15 au ratio AD/AP**, par rang (jusqu'au rang 3)

Cette règle simple évite d'avoir à re-choisir un nouvel effet à chaque rang : la compétence garde son identité, elle devient juste plus forte. Les compétences de contrôle/buff pur sans dégâts chiffrés (silence, immobilisation, buff de stats...) gardent leur effet identique à chaque rang, sauf si le joueur/MJ décide explicitement d'augmenter une durée ou un pourcentage à la place.

**La recharge diminue aussi avec le rang** (comme dans le jeu vidéo, la maîtrise d'un sort le rend plus disponible) :
- **Q, W ou E** : recharge de base aux rangs 1 et 2, **-1 round au rang 3**, **-1 round supplémentaire au rang 5** — plancher absolu de **1 round**.
- **Ultime (R)** : **-1 round à chaque rang** (rang 2 et rang 3) — plancher absolu de **2 rounds**.
- Un Ultime à usage limité (ex. "1×/combat" plutôt qu'un nombre de rounds) n'est pas concerné par cette réduction : sa limitation reste inchangée quel que soit le rang.

Exemple : un Q avec 3 rounds de recharge de base reste à 3 rounds aux rangs 1-2, passe à 2 rounds au rang 3-4, puis à 1 round au rang 5 (plancher atteint).

### 5.2 Déblocage des compétences et montée en niveau

**À la création (niveau 1), le personnage possède déjà :**
- Son **Passif** (toujours actif, gratuit, ne coûte jamais de point)
- **Une compétence active au choix du joueur** parmi Q, W ou E, déjà au rang 1 (le joueur décide laquelle correspond le mieux à son concept de personnage — rien n'oblige à commencer par Q)

**Les deux compétences restantes se débloquent aux niveaux suivants, dans l'ordre que le joueur préfère :**
- **Niveau 2** : le joueur débloque l'une des deux compétences encore verrouillées (rang 1)
- **Niveau 3** : la dernière compétence restante se débloque (rang 1)
- **Niveaux 6, 11 et 16** : l'Ultime (R) se débloque puis monte en rang (rang 1 → 2 → 3), toujours dans cet ordre fixe

Autrement dit, au niveau 3, les trois compétences Q/W/E sont toutes débloquées au rang 1, quel que soit l'ordre choisi par le joueur pour y arriver — seul l'Ultime garde un déblocage imposé aux niveaux 6/11/16.

**À partir du niveau 4**, le point de compétence gagné chaque niveau peut être investi librement dans Q, W ou E (au choix du joueur, max rang 5 chacun) pour continuer à les monter en puissance. Un personnage niveau 18 a donc au final : Passif + Q5 + W5 + E5 + R3 — le total est identique quel que soit l'ordre de déblocage choisi au début.

Le rythme de montée de niveau dépend du MJ : généralement **1 niveau par session ou par arc narratif important**, pas par combat individuel.

### 5.2bis Identité générique des emplacements

Pour garder une cohérence entre tous les personnages sans imposer de règle rigide, chaque emplacement a une **fonction générique par défaut** — libre au joueur et au MJ de l'adapter selon le sous-rôle si ça a plus de sens narrativement :

| Emplacement | Fonction générique par défaut | Variation possible selon le sous-rôle |
|---|---|---|
| **Q** | Compétence de dégâts principale | Reste presque toujours des dégâts, quel que soit le sous-rôle |
| **W** | Compétence de contrôle (ralentissement, immobilisation, étourdissement...) | Pour un Support Enchanteur, peut devenir un soin/bouclier à la place d'un contrôle |
| **E** | Compétence utilitaire ou de mobilité (dash, discrétion, buff...) | Pour un Tank, peut devenir une protection d'allié plutôt qu'une mobilité personnelle |
| **Passif** | Effet permanent ou déclenché lié à l'identité du sous-rôle | Toujours propre à chaque personnage, pas de règle générique |
| **Ultime (R)** | La compétence la plus impactante du personnage, tous types d'effets possibles | Libre — c'est là que l'identité unique du personnage s'exprime le plus |

Ces fonctions ne sont **pas obligatoires** : elles servent de repère par défaut pour ne pas partir d'une page blanche, mais un joueur qui a un concept clair en tête (par exemple un Q de contrôle plutôt que de dégâts) peut s'en écarter avec l'accord du MJ.

#### Règles d'équilibrage (sans budget de points)

Plutôt qu'un système de points à calculer, l'équilibrage repose sur des **repères qualitatifs simples** que le MJ peut vérifier d'un coup d'œil :
- Les **ratios AD/AP** par emplacement (section 3.4) donnent déjà une fourchette claire : 0,4-0,7 pour Q/E, 0,6-1,0 pour W, 0,8-1,5 pour l'Ultime.
- **Un effet fort (étourdissement, immobilisation, silence) doit s'accompagner d'un ratio de dégâts réduit ou d'un cooldown plus long** — jamais les deux au maximum en même temps sur la même compétence.
- **Un sort qui touche une zone entière** doit avoir un ratio de dégâts par cible inférieur à un sort ciblant une seule personne, ou un cooldown plus long.
- Le MJ garde toujours le dernier mot pour ajuster une compétence qui semble trop forte ou trop faible en pratique, sans avoir besoin de justifier ça par un calcul — l'objectif reste le plaisir de jeu, pas la précision mathématique.

---

### 5.3 Progression des statistiques de combat (niveau 1 à 18)

Toutes les stats de combat (PV, AD, AP, Armure, RM) augmentent de façon **linéaire**, avec un **bond supplémentaire aux niveaux 6, 11 et 16** — exactement les niveaux où l'Ultime se débloque ou monte de rang, pour que ces paliers se ressentent aussi mécaniquement, pas seulement par un nouveau sort.

**Formule :**
```
Incrément normal (r) = (Valeur au niveau 18 − Valeur au niveau 1) ÷ 20, arrondi à l'entier le plus proche

À chaque niveau : Stat += r
Aux niveaux 6, 11 et 16 uniquement : Stat += 2r (le double, au lieu de r)
```
*(Le ÷20 n'est pas arbitraire : sur les 17 montées de niveau entre le niveau 1 et 18, 14 sont "normales" et 3 sont doublées, ce qui fait bien 14 + (3×2) = 20 unités au total — la formule tombe juste.)*

**PV** : utiliser directement les valeurs niveau 1 / niveau 18 du tableau de rôle (section 3.3).

**AD, AP, Armure, RM** : partir de la valeur "base" du tableau de rôle (section 3.3) comme valeur de niveau 1, et viser **+60% au niveau 18** (valeur niveau 18 = valeur niveau 1 × 1,6) — une progression plus modeste que les PV, cohérente avec l'esprit du jeu vidéo où les dégâts montent surtout via les objets, pas le niveau brut.

**Exemple complet — un Tank (PV base 65 → 224, AD base 10) :**
```
PV  : r = (224-65)/20 = 7,95 ≈ 8       → +8 PV/niveau, +16 PV aux niveaux 6/11/16
AD  : cible niv.18 = 10 × 1,6 = 16 → r = (16-10)/20 = 0,3 ≈ 0 (arrondi)  → +1 AD tous les 3 niveaux environ, +2 AD aux paliers d'ulti

Niveau 1  : 65 PV, 10 AD
Niveau 6  : 65 + (5×8) + 8 = 113 PV     (5 incréments normaux + 1 doublé)
Niveau 11 : 113 + (4×8) + 8 = 153 PV
Niveau 16 : 153 + (4×8) + 8 = 193 PV
Niveau 18 : 193 + (2×8) = 209 PV        (proche de la cible 224, à ajuster de quelques points par le MJ si besoin)
```
*(Pour les stats à faible incrément comme l'AD ici, le MJ peut simplement offrir le bonus par palier de 2-3 niveaux plutôt que de gérer des fractions — l'objectif est la sensation de progression, pas la précision comptable.)*

### 5.4 Progression des attributs primaires
Le personnage gagne des points d'attribut supplémentaires **aux niveaux 3, 6, 9, 12, 15 et 18** — voir section 3.1, où ce gain a été fusionné directement dans le pool de point-buy évolutif (21 points à la création → 27 au niveau 18). Ces points se dépensent dans le même tableau de coûts que la création (0/1/2/3/4/5/7/9 selon la valeur visée) et peuvent être répartis librement entre les 6 attributs.

---

## 6. Objets et équipement

Les objets fonctionnent comme dans League of Legends : ils s'achètent (boutique en ville, forgerons Hextech, marché noir de Zaun...) ou se trouvent en récompense, et donnent des bonus de statistiques + parfois un effet passif/actif unique.

La liste complète des objets — composants de base, épiques, bottes, légendaires, objets régionaux uniques, et le kit de départ par sous-rôle — se trouve dans le **Partie 3 : Objets & Équipement**.

*Pour une session de shopping rapide à la table, voir la **Fiche Résumé : Objets & Boutique**, qui condense tous les tableaux ci-dessous (effets + recettes de craft fusionnés) sur un format court.*

---

## 7. Le combat

### 7.1 Structure d'un round
1. **Initiative** : chaque participant fait un jet de DEX (section 3.5) ; le résultat le plus bas agit en premier (cohérent avec "bas = bon").
2. Dans l'ordre d'initiative, chaque personnage joue son tour : **1 Action principale + 1 Déplacement**, dans l'ordre de son choix (il peut se déplacer avant ou après son action, ou se déplacer en deux fois autour d'une action à portée de contact).
3. Une fois tout le monde passé, un nouveau round commence (l'ordre d'initiative reste le même sauf effet contraire).
4. Le combat se termine quand un camp est mort, K.O., s'est rendu, ou a fui hors de portée de tous les adversaires.

### 7.2 Les actions principales disponibles

| Action | Effet |
|---|---|
| **Attaque de base** | Jet d'Attaque en mêlée ou à distance (section 3.5) contre la cible |
| **Lancer un sort** | Utilise Q, W, E ou R : payer la ressource, vérifier que le cooldown est écoulé, faire le jet si nécessaire |
| **Utiliser un objet actif** | Objets à effet déclenché (Partie 3) : Coutelas de Bilgewater, Hextech Protobelt-01, etc. |
| **Aider un allié** | Renonce à sa propre attaque pour donner un Avantage (section 2.3 Option A) au prochain jet d'un allié à portée |
| **Attente / Vigilance** | Ne fait rien immédiatement, mais peut interrompre son tour plus tard dans le round pour réagir à un événement précis (ex. attaquer dès qu'un ennemi s'approche) |
| **Fuite / Retraite** | Se déplace en tentant de sortir du combat ; déclenche une attaque d'opportunité (section 7.4) si mal négocié |

Une **action mineure gratuite** (ramasser un objet au sol, ouvrir une porte, parler une phrase courte) peut toujours être ajoutée sans consommer l'Action principale, à l'appréciation du MJ.

### 7.3 Portées et positionnement
Le jeu utilise les 4 bandes de portée déjà définies pour les sorts (section 5.1) : **Contact, Courte (3m), Moyenne (8m), Longue (15m+)**. Sur Roll20, ces distances se traduisent directement en cases de la grille (1 case ≈ 1,5m, arrondir au besoin) :

| Portée | Distance | Cases (grille Roll20) |
|---|---|---|
| **Contact** | 0m (adjacent) | 0-1 case |
| **Courte** | 3m | 2 cases |
| **Moyenne** | 8m | 5-6 cases |
| **Longue** | 15m+ | 10+ cases |

La Vitesse de Déplacement (section 3.2) indique combien de cases un personnage peut franchir par round.

### 7.4 Attaque d'opportunité
Si un personnage engagé au contact se déplace hors de portée de contact d'un ennemi **sans utiliser une capacité de mobilité dédiée** (dash, téléportation courte), cet ennemi peut immédiatement faire une attaque de base gratuite contre lui (ne consomme pas son tour). Les capacités qui mentionnent explicitement une esquive de ce genre de riposte (ex. certains sorts d'Assassin) l'évitent.

### 7.4bis Le Combo (enchaîner plusieurs compétences dans le même round)

Un personnage peut tenter d'enchaîner **jusqu'à 4 compétences actives** (Q, W, E et Ultime compris) dans un même round, dans l'ordre de son choix — un moment spectaculaire, mais risqué. *Le Combo remplace l'unique Action principale du round (section 7.1) : au lieu d'utiliser une seule compétence, le personnage en tente plusieurs à la suite, mais garde son tour normal (pas d'action bonus supplémentaire en dehors de ça).*

**Déplacement :** contrairement à une action normale (où le déplacement est libre avant ou après, section 7.1), le personnage peut se déplacer **avant** de tenter le Combo, mais **plus du tout après** — une fois le premier sort du Combo lancé, il reste sur place jusqu'au round suivant.

**Coût :** payer la ressource de chaque compétence effectivement déclenchée (voir plus bas).

**La 1ʳᵉ compétence du combo se lance normalement**, sans jet supplémentaire. **Chaque compétence suivante nécessite un jet de combo** : Attribut lié ×5, moins un malus qui grimpe selon la position :

| Position dans le combo | Malus au jet |
|---|---|
| 1ʳᵉ compétence | Aucun jet de combo (cast normal) |
| 2ᵉ compétence | -10 *(ajustable à -20 après test si ça semble trop facile)* |
| 3ᵉ compétence | -30 |
| **Ultime, quelle que soit sa position** | **-50 fixe** (même utilisé en 2ᵉ position, il garde -50, pas -10) |

**Le combo s'arrête au premier échec.** En cas d'échec sur un maillon :
- Cette compétence **ne produit pas son effet**
- **Elle, ainsi que toutes les compétences prévues après elle dans le combo (non tentées), partent en temps de recharge à 50% de leur valeur normale** — le personnage rate son enchaînement mais épuise quand même une partie de son potentiel
- Aucune de ces compétences ratées/non tentées ne consomme de ressource (seul leur cooldown est impacté)
- Les compétences réussies **avant** l'échec gardent leur plein effet et leur cooldown complet normal, sans réduction

**Échec critique (95-100)** sur un maillon : en plus d'arrêter le combo, cette compétence se retourne contre le lanceur ou touche un allié proche (comme un échec critique classique, section 2.4).

**Exemple concret** — un Mage tente Q → W → R dans le même round (attributs : DEX 13 pour W, VOL 12 pour l'Ultime) :
```
Q (1ère)   : cast normal, pas de jet de combo → réussi, effet plein, cooldown normal
W (2ème)   : Seuil = (13×5) - 10 = 55          → réussi → effet plein, cooldown normal
R (3ème, Ultime) : Seuil = (12×5) - 50 = 10     → échoue (Seuil très bas, l'Ultime est risqué en combo)
```
Résultat : Q et W ont fonctionné normalement. L'Ultime rate, ne produit aucun effet, ne coûte pas sa ressource, mais part en recharge à 50% de sa valeur normale — le personnage "a tenté" et en paie le prix, sans avoir pu en profiter.

### 7.5 Résolution d'une attaque ou d'un sort
1. Le personnage annonce son action et sa cible.
2. Jet d'Attaque, de Sort magique, ou jet opposé selon le cas (sections 2.1/2.5 et 3.5).
3. En cas de réussite, les dégâts se calculent avec la formule complète (section 3.4ter) : base + ratio × AD/AP → + bonus fixe d'affinité élémentaire si applicable → − Armure/RM de la cible.
4. Le **degré de réussite** (section 2.4) module l'effet :
   - **Critique** : dégâts maximum + effet secondaire de l'affinité s'il y en a une (Partie 2, section 5.1)
   - **Réussite normale** : dégâts pleins
   - **Échec critique** : la capacité peut se retourner contre le lanceur ou toucher un allié proche, à l'appréciation du MJ

### 7.6 États et altérations
Ces états, déjà utilisés dans le bestiaire et les objets, sont centralisés ici pour référence rapide :

| État | Effet |
|---|---|
| **Étourdi** | Perd son prochain tour entièrement |
| **Ralenti** | Vitesse de Déplacement réduite de 1 case (ou 2 cases pour un ralenti fort, type objet légendaire) pendant la durée indiquée |
| **Immobilisé / Enraciné** | Ne peut pas se déplacer, mais peut toujours agir (attaquer, lancer un sort) |
| **Silence** | Ne peut pas lancer de sort (Q/W/E/R), mais peut toujours attaquer et se déplacer |
| **Aveuglé** | Désavantage (section 2.3 Option A) sur tous les jets d'attaque |
| **Peur** | Doit s'éloigner de la source de la peur à son prochain tour, ne peut pas s'en approcher volontairement |
| **Dégât continu (Brûlure/Poison/Saignement...)** | Inflige des dégâts fixes au début de chaque tour du porteur, pendant la durée indiquée par la capacité qui l'a causé |
| **Charme / Contrôle mental** | La cible doit exécuter une action décidée par celui qui contrôle l'effet (dans la limite du raisonnable et du bon sens du MJ) |

Sauf indication contraire, un état dure jusqu'à la fin du prochain tour du porteur, et plusieurs applications du même état ne se cumulent pas en durée (elles rafraîchissent simplement le compteur), sauf mention explicite de "cumulable" dans la capacité concernée.

### 7.7 Mort et K.O.
- À **0 PV**, le personnage tombe inconscient (pas mort automatiquement).
- Au début de chacun de ses tours pendant qu'il est à 0 PV, il fait un **jet de Résistance mentale (VOL)** : réussite = stable, échec = gagne un point d'échec ; à **3 points d'échec cumulés**, le personnage meurt.
- N'importe quel allié adjacent peut utiliser son action pour **stabiliser** le personnage à terre (jet de Premiers secours, section 3.5, ou automatique s'il possède un objet/sort de soin) : le personnage repasse à 1 PV et sort de l'état critique.
- Si un personnage à 0 PV subit à nouveau une attaque, il meurt instantanément (pas de jet de Résistance dans ce cas) — cohérent avec le grade de dangerosité voulu pour la campagne, à ajuster si le groupe préfère plus de marge.

### 7.8 Gestion des combats à grande échelle (optionnel, conseil MJ)
Pour un combat impliquant beaucoup d'ennemis faibles (une nuée de Rampants du Néant, une horde de sbires), le MJ peut simplifier en regroupant plusieurs créatures identiques en une seule **"escouade"** — mécanique complète (PV additionnés, un seul jet, puissance de feu qui diminue avec les PV restants) dans le Manuel du Maître du Jeu, section 5.

### 7.9 Repos et récupération

Deux paliers, volontairement simples :

| Type de repos | Fréquence | Effet |
|---|---|---|
| **Repos court** (quelques minutes de calme en fiction) | Aussi souvent que le rythme narratif le permet — le MJ peut le refuser si l'urgence de la scène l'empêche | Régénère la réserve de ressource à **50%** de son maximum ; PV via un jet de Premiers Secours normal (action neutre, section 3.5) |
| **Repos complet** (une nuit de sommeil) | **1× par jour narratif maximum** | Régénère PV et réserve de ressource à 100% ; remet à zéro tous les temps de recharge (cooldowns) |

Le repos complet limité à 1/jour donne un vrai enjeu à la gestion de ressources sur une journée chargée, sans pour autant demander de calculs compliqués à la table.

### 7.10 Défis non-combat (énigmes, poursuites, négociations, infiltration)

Un mécanisme générique unique, pour éviter d'inventer un sous-système différent à chaque situation.

**Règle des 3 réussites avant 2 échecs.** Le MJ pose un défi global (une porte piégée à désamorcer, une poursuite dans les toits, une négociation tendue avec un noble). Chaque personnage impliqué tente une action neutre pertinente (section 3.5) pour faire progresser le groupe — mais **un même personnage ne peut pas retenter deux fois de suite la même action neutre** sur ce défi (il doit varier son approche, ex. passer de Discrétion à Athlétisme, ou d'Enquête à Persuasion).

- Le défi se résout en **réussite** dès que le groupe cumule **3 succès**
- Il se résout en **complication** dès que le groupe cumule **2 échecs** — l'histoire avance quand même, mais avec un coût (bruit qui alerte des gardes, temps perdu, une relation qui se dégrade), jamais un blocage total de la progression
- Un échec critique (section 2.2) compte double (2 échecs d'un coup) et peut introduire une complication plus marquée au choix du MJ

---

## 8. Maîtrise et Runes (optionnel — personnalisation)

Deux systèmes bien distincts, aucun des deux n'ajoute de dégâts bruts — l'idée est de rendre chaque personnage plus **unique**, pas plus fort en chiffres.

### 8.1 Maîtrise — 3 arbres façon grille classique (Combat, Volonté, Utilitaire)

Reprend directement le principe de la grille de Maîtrises historique : des rangées de nœuds, débloquées par palier de points investis dans l'arbre, jusqu'à une **Signature** au fond de chaque arbre qui nécessite un vrai engagement. **1 point de Maîtrise par niveau, du niveau 1 au niveau 18 (18 points au total sur toute la campagne)** — comme dans le jeu vidéo.

**Comment lire un nœud** : chaque nœud a une **limite d'usage fixe** (elle ne change jamais, quel que soit le rang) et un **rang qui améliore la qualité de l'effet**, pas sa fréquence. Le schéma le plus courant : Rang 1 donne l'Avantage (2d100, garde le meilleur) sur le jet concerné ; Rang 2 rend l'effet automatique, sans jet du tout.

**Paliers de déblocage par arbre** : Rangée 1 → 0 point investi dans cet arbre · Rangée 2 → 1 point · Rangée 3 → 3 points · Rangée 4 → 5 points · Signature → 10 points.

**Coût d'un nœud : 1 point par rang.** Un nœud au Rang 1 coûte 1 point ; le monter au Rang 2 coûte 1 point de plus (2 points au total). Le nombre total de points dépensés sur les nœuds d'un arbre ne peut jamais dépasser les points investis dans cet arbre — impossible de prendre plusieurs nœuds gratuitement même en Rangée 1.

**Impossible d'obtenir 2 Signatures.** Avec 18 points au total et 10 points requis par Signature, en débloquer deux coûterait au moins 20 points — plus que ce qui est disponible sur toute la campagne. Pas besoin d'interdiction explicite, la contrainte de points s'en charge naturellement.

#### COMBAT

| Rangée | Nœud | Limite | Rang 1 | Rang 2 | Rang 3 |
|---|---|---|---|---|---|
| 1 | Frappe Assurée | 1×/combat | Avantage sur un jet d'Attaque raté | Cette attaque réussit automatiquement, sans jet | — |
| 1 | Pied Léger | Illimité, chaque round | +1 case de Vitesse de Déplacement | +2 cases | 1×/combat, pendant ton tour : jette 1d100 contre DEX×5 — une réussite te permet un déplacement gratuit de 3 cases supplémentaires, sans consommer ton Action ni ton Déplacement normal |
| 1 | Sang-Froid | 1×/combat | Avantage pour résister à un Étourdissement | Ignore complètement l'Étourdissement, sans jet | — |
| 2 | Ouverture | 1×/combat | Avantage sur l'attaque contre une cible qui n'a pas encore agi | Cette attaque réussit automatiquement | — |
| 2 | Poursuite | 1×/combat | Avantage sur l'Initiative après avoir vaincu un ennemi | Agit immédiatement après, sans jet | — |
| 3 | Contre | 1×/combat | Avantage sur l'attaque qui suit une Esquive réussie | Cette attaque réussit automatiquement | — |
| 3 | Rage Contrôlée | 1×/combat | Réduit de moitié les dégâts d'une attaque reçue | Annule complètement ces dégâts | — |
| 4 | Second Souffle *(1 rang)* | 1×/session | Remonte à 1 PV la première fois qu'il tombe à 0 | — | — |
| Signature | **Impulsion de Combat** | 1×/combat | Prends un tour complet supplémentaire immédiatement — nouvelle Action + Déplacement, comme si le round recommençait rien que pour toi | — | — |

#### VOLONTÉ

| Rangée | Nœud | Limite | Rang 1 | Rang 2 | Rang 3 |
|---|---|---|---|---|---|
| 1 | Peau Dure | 1×/combat | Réduit de moitié les dégâts d'une attaque de base reçue | Annule complètement ces dégâts | — |
| 1 | Clarté d'Esprit | 1×/session | Avantage contre un Charme/Peur | Résiste automatiquement, sans jet | — |
| 1 | Sang-Froid Absolu | 1×/combat | Avantage pour résister à une Immobilisation | Ignore complètement l'Immobilisation | — |
| 2 | Vigilance | Illimité, chaque combat | Avantage permanent sur l'Initiative | Agit automatiquement en premier, sans jet | — |
| 2 | Lien du Groupe | 1×/combat | Un allié adjacent gagne Avantage sur son Initiative | Cet allié agit immédiatement après toi, sans jet | — |
| 3 | Résilience | 1×/session | Avantage pour se défaire d'un état négatif | Retire automatiquement cet état, sans jet | — |
| 3 | Dernier Rempart | 1×/combat | Absorbe un quart des dégâts destinés à un allié adjacent | Absorbe la moitié | — |
| 4 | Ténacité *(1 rang, permanent)* | Illimité | Réduit d'1 round la durée des Contrôles subis (min. 1) | — | — |
| Signature | **Inébranlable** | 1×/session | Ignore un coup qui t'aurait tué — reste à 1 PV | — | — |

#### UTILITAIRE

| Rangée | Nœud | Limite | Rang 1 | Rang 2 |
|---|---|---|---|---|
| 1 | Débrouille | 1×/scène | Avantage pour improviser un usage à un objet du quotidien | Réussit automatiquement, sans jet |
| 1 | Bonne Mémoire | 1×/session | Avantage pour se souvenir d'un détail sur un PNJ déjà croisé | Se souvient automatiquement |
| 1 | Sens de l'Orientation | 1×/voyage | Avantage pour ignorer un malus de terrain | Ignore automatiquement |
| 2 | Beau Parleur | 1×/session | Avantage pour changer d'approche sociale sans le malus anti-spam | Change automatiquement, sans malus |
| 2 | Bricoleur | 1×/session | Avantage pour réparer ou évaluer un objet rare | Réussit automatiquement, sans jet |
| 3 | Contact | 1×/arc narratif | Avantage pour activer un contact utile dans une grande ville | Contact automatiquement disponible |
| 3 | Réserves Cachées | 1×/session | Récupère la moitié des effets d'une Potion de Soin déjà utilisée | Récupère la Potion entièrement |
| 4 | Œil Aiguisé *(1 rang, permanent)* | Illimité | Repère automatiquement les pièges/passages secrets évidents | — |
| Signature | **Coup du Sort** | 1×/session | Transforme n'importe quel échec (n'importe quel jet, combat compris) en réussite automatique, comme si les astres s'alignaient | — |

*Répartition des Rangées : les 7 nœuds "classiques" de chaque arbre sont répartis 3/2/2 dans l'ordre du tableau ci-dessus (Rangée 1 : les 3 premiers · Rangée 2 : les 2 suivants · Rangée 3 : les 2 derniers), identique pour les 3 arbres. Le nœud à 1 rang correspond toujours à la Rangée 4, la Signature reste à part.*

*Exemple de répartition : un joueur qui vise la Signature Combat investit 10 points dans cet arbre au fil des niveaux (assez pour débloquer les 5 rangées et payer le coût des nœuds), puis répartit ses 8 points restants ailleurs. Un joueur généraliste pioche large dans les 3 arbres sans jamais atteindre une Signature — les deux approches sont valides.*

### 8.2 Runes — des fragments du Monde, pas des achats

Les vraies Runes de Runeterra ne sont pas des babioles de boutique : ce sont des fragments des **Runes du Monde**, des artefacts créés par des Célestes inconnus pour façonner Runeterra elle-même — c'est d'ailleurs de là que vient le nom du monde. Leur découverte a jadis déclenché les Guerres des Runes, et depuis, la plupart des fragments restants sont soit perdus, soit jalousement gardés.

Dans notre système, une **Rune est un ingrédient de craft consommable**, jamais vendue en boutique : elle s'obtient uniquement en explorant un lieu précis, en vainquant un gardien, ou en accomplissant une quête liée à un fragment particulier. Sans elle, une recette légendaire (Partie 3, section 2) reste bloquée, peu importe l'or disponible.

*Le procédé qui permet de canaliser une Rune dans un objet a un nom : c'est le Hextech, popularisé par les artisans de Piltover (Manuel du Maître du Jeu, section 12) — combiner une Rune et des composants, c'est littéralement faire du Hextech.*

**Un rival tout trouvé pour vos campagnes** : **Ryze**, archimage errant légendaire, parcourt Runeterra depuis des siècles dans le but inverse de vos joueurs — il cherche à retrouver et **sceller** chaque fragment de Rune du Monde encore libre, convaincu (à raison ou non) qu'une nouvelle Guerre des Runes éclatera si les mortels continuent d'en abuser. Il peut apparaître comme un mentor bourru qui met en garde le groupe, ou comme un rival qui arrive juste avant eux sur le lieu d'une Rune et la scelle sous leurs yeux — au MJ de décider selon le ton voulu.

*Exemple concret :* `Fléau + Épée Longue + Rune de l'Acier + 700 po = Couperet Noir`

| Rune | Débloque la recette de... | Où la trouver (ancrée dans nos livres) |
|---|---|---|
| **Rune du Sang** | Danse de la Mort, Lame du Roi Déchu | Cachée dans le repaire de Vilemaw (Îles Obscures) — un fragment corrompu par des siècles de Brume |
| **Rune de l'Acier** | Présage de Randuin, Couperet Noir, Gage de Sterak | Disputée depuis des générations entre la Légion Trifarienne (Noxus) et l'Avant-Garde Intrépide (Demacia) — accomplir une quête pour l'un des deux camps |
| **Rune de l'Éclat** | Lame d'Infini, Canon Ultrarapide | Scellée dans une arène de duel oubliée d'Ionia, ou dans un coffre-fort technologique de Piltover |
| **Rune du Néant** | Bâton du Vide, Coiffe de Rabadon | Dans les ruines d'Icathia, à la source même de la corruption du Néant — un fragment qui a jadis mal tourné |
| **Rune du Flux** | Bâton de l'Archange, Manamune | Confiée par un Aspect ou un temple de Targon — un fragment resté proche des Célestes qui l'ont créé |
| **Rune de l'Aube** | Renouveleur de Pierre de Lune, Médaillon de l'Iron Solari, Voile de la Banshee | Offerte en récompense d'un service rendu à une communauté ou un temple (Bandle City, Targon) |
| **Rune de la Furie** | Lame Spectre de Youmuu, Force de la Trinité | Arrachée à un boss épique vaincu (Baron Nashor, Dragon Ancien, Atakhan — Manuel du MJ) |
| **Rune du Titan** | Armure de Warmog, Égide Solaire | Gardée au cœur de la jungle profonde d'Ixtal, protégée par les guerriers Yun Tal — une épreuve d'endurance et de survie, pas de combat |

*(Le MJ est libre d'inventer d'autres lieux ou gardiens pour chaque Rune — ce tableau n'est qu'un point de départ ancré dans le lore déjà posé.)*

---

## 9. Où trouver le reste

Ce Manuel du Joueur couvre tout ce qu'il faut pour créer et jouer un personnage. Pour le bestiaire, les PNJ génériques et les conseils de MJ, voir le **Manuel du Maître du Jeu**. Les fiches résumé (Création de Personnage, Guide de Combat, Objets & Boutique, et côté Manuel du Maître du Jeu Guide du MJ et Bestiaire condensé) offrent un accès rapide aux règles les plus utilisées à la table. Pour jouer, imprimez la **Fiche de Personnage** (vierge, à remplir au crayon) — distincte de la Fiche Création de Personnage, qui résume les règles plutôt que d'offrir des cases à remplir.

Pour construire l'historique de son personnage (étape 7 de la création), voir le **Questionnaire de Background** — une version MJ (guide de discussion avec relances) et une version Joueur (à remplir en amont de la session 0) sont disponibles séparément.

Reste à venir dans de futurs suppléments : campagne longue. *(Le scénario tuto existe en document séparé complet ; quêtes régionales et fiche de personnage Roll20 + macros existent aussi déjà séparément — voir le suivi de projet.)*

---

## 10. Outils recommandés pour jouer en ligne

| Besoin | Outil suggéré |
|---|---|
| Table virtuelle / cartes / jetons | **Roll20** (compatible d100 via macros `/roll 1d100`) ou **Foundry VTT** (plus de contrôle mais payant) |
| Musique d'ambiance par région | **Tabletop Audio**, **Syrinscape**, ou playlists YouTube "League of Legends region OST" (Piltover/Zaun, Freljord, Ionia ont des thèmes officiels très adaptés) |
| Bruitages ponctuels | **Syrinscape SFX**, **Battlebards** |
| Cartes de Runeterra | Recherchez "Runeterra map fanart/battlemap" sur Reddit (r/battlemaps) ou créez les vôtres avec **Dungeondraft**/**Inkarnate** |
| Gestion des fiches de perso | Feuille personnalisée sur Roll20 (character sheet custom) — je peux vous préparer le HTML/CSS si vous voulez l'importer directement |
| Communication vocale | Discord (intégration facile avec Roll20 via overlay) |


---

# PARTIE 2 — ORIGINES, RACES, RÔLES & RÉPUTATION

## 1. Région d'origine

Chaque personnage choisit une région de naissance. Elle donne : un **trait culturel** (bonus mécanique permanent), un **bonus "terrain connu"** (avantage quand l'action se déroule dans sa région d'origine), et une **réputation de départ** ailleurs (voir section 4).

*Décompte : les 12 régions canoniques de Runeterra (Demacia à Bandle City ci-dessous), plus le Néant (Icathia) ajouté délibérément par ce système comme 13ᵉ origine jouable pour les personnages liés au Néant (Voidborn, humains touchés par le Néant...), plus enfin Sans région (Errant) pour les personnages sans terre natale claire — 14 lignes au total dans le tableau, mais seulement 12 régions "officielles" au sens strict du lore.*

Le bonus "terrain connu" est le même pour toutes les régions (rappel, Partie 1 section 2.2) : **fenêtre de Réussite Critique élargie à 1-10 (au lieu de 1-5) quand l'action se déroule dans sa région d'origine.** Seul le trait culturel change d'une région à l'autre :

| Région | Trait culturel (bonus permanent) |
|---|---|
| **Demacia** | +1 en tests de Volonté contre la peur/magie hostile (discipline martiale) |
| **Noxus** | +1 dégâts infligés quand le personnage est seul contre plusieurs ennemis ("la force prime") |
| **Ionia** | +1 en tests d'Esquive/DEX (harmonie du mouvement) |
| **Piltover** | +1 en tests d'artisanat/Hextech, accès à des objets technologiques exclusifs |
| **Zaun** | Résistance aux poisons/maladies, accès au marché noir chimtech |
| **Freljord** | Résistance au froid, +1 PV max par niveau supplémentaire |
| **Shurima** | Résistance à la chaleur/déshydratation, +1 en tests d'Histoire ancienne |
| **Bilgewater** | +1 en Charisme (marchandage, intimidation de bas-fonds), résistance à l'ivresse |
| **Îles Obscures** | Résistance à la peur surnaturelle, mais -1 Charisme avec les non-initiés (aura étrange) |
| **Ixtal** | +1 en Discrétion/survie en milieu naturel, affinité Nature facilitée |
| **Bandle City** | +1 DEX, taille réduite (avantage discrétion, désavantage portée de mêlée) |
| **Targon** | +1 en Volonté, sensibilité accrue aux Aspects/entités célestes |
| **Néant (Void)** | Résistance à la peur surnaturelle et à la corruption mentale ; perception accrue des anomalies du Néant. *Terrain connu élargi : toute zone corrompue par le Néant (Icathia, failles zaunites, Marais Putrides...), pas seulement une région précise.* |
| **Sans région (Errant)** | Polyvalent : +1 à un attribut au choix, déterminé à la création selon son histoire personnelle (civilisation disparue, terre natale abandonnée, voyageur de toujours). *Exception : aucune fenêtre de critique élargie nulle part (pas de région d'origine) ; en échange, ne part jamais de zéro en réputation — +1 partout dès la création, au lieu de +1 dans une seule région.* |

*(Le MJ peut activer ou non le bonus "terrain connu" selon le rythme voulu — c'est un levier d'équilibrage simple.)*

---

## 2. Races jouables

| Race | Bonus | Malus / contrepartie |
|---|---|---|
| **Humain** | +1 point d'attribut libre (polyvalence) | Aucun malus racial (norme de référence) |
| **Vastaya** (forme hybride animale, lignées diverses) | +1 attribut lié à la lignée animale (FOR, DEX ou VOL au choix) + sens aiguisé (bonus Perception) | -1 Charisme envers les humains méfiants, apparence non-humaine parfois stigmatisée |
| **Yordle** | +2 DEX, +1 en tests de Discrétion, résistance mentale contre la peur | -1 FOR, portée de mêlée réduite |
| **Transfiguré** (être façonné/altéré par une magie ancienne ou le Royaume des Esprits, capable d'emprunter une forme partielle animale ou spirituelle à volonté) | +1 VOL, une forme mineure de métamorphose utilisable en jeu (bonus temporaire à un test, 1 fois par scène) | Forme instable : un échec critique en métamorphose peut provoquer une perte de contrôle temporaire (au choix du MJ) |
| **Void (Symbiote)** (hôte lié à une entité du Néant, à la Kog'Maw/Bel'Veth, sans en être une incarnation majeure) | Résistance aux dégâts magiques du Néant, vision dans le noir total, +1 en tests d'intimidation | Suscite la peur/méfiance de la majorité des PNJ, -1 Charisme général, vulnérable aux effets de Lumière/Purification |
| **Troll** | +2 FOR, régénération naturelle (petit soin passif entre les scènes) | -1 INT, réputation de "sauvage" qui complique les interactions dans les grandes cités |
| **Freljordien** (humain endurci par le Grand Nord, tribus Avarosan/Winter's Claw/Frostguard) | +1 CON, résistance totale au froid, +1 en Survie | -1 en tests liés à la chaleur extrême/déshydratation |
| **Darkin** (hôte porteur d'un fragment d'arme Darkin ou de sang ancien Ascendant, hérité d'une lignée qui a jadis semé le chaos à travers tout Runeterra durant des siècles sans meneur — la Grande Guerre des Darkins) | +2 dans un attribut au choix, résistance aux dégâts physiques | Corruption latente : la puissance grandit avec l'usage (le MJ peut faire progresser un compteur de corruption narratif), forte notoriété/crainte des PNJ |
| **Ascendu** (mortel élevé à un pouvoir quasi-divin par le rituel d'ascension shurimais précis — contrairement au Transfiguré, aucune métamorphose : un renforcement permanent et définitif du corps et de l'endurance) | +2 dans un attribut au choix, résistance à la chaleur extrême, immunité à la soif/faim prolongée | Statut hors du commun : suscite crainte ou vénération selon les régions, ne peut plus jamais vivre une existence anonyme parmi les mortels |
| **Augmenté Chemtech** (Zaunite modifié, façon Viktor/Ekko-tech légère) | +1 attribut au choix + un gadget mineur de départ | Dépendance à l'entretien de l'augmentation (coût en argent régulier), méfiance de certains PNJ conservateurs |
| **Être des Étoiles** (lié à un Aspect ou à une entité céleste, façon Aurelion Sol/Zoé sans en être une incarnation) | +2 VOL, résistance à la magie du Néant | Rêves/visions parfois incontrôlables (le MJ peut s'en servir narrativement), -1 CON |
| **Vessel d'Aspect** (mortel porteur d'une étincelle céleste, Solari ou Lunari au choix — Manuel du MJ, section 11) | +2 VOL, Avantage sur les jets de Résistance mentale contre la peur/le désespoir | Cible vivante du schisme religieux de Targon : le camp opposé (Solari si Lunari, ou l'inverse) le considère comme une menace ou une hérésie |

---

## 3. Réputation régionale

Chaque région dispose d'une **jauge de réputation indépendante** allant de **-5 (Traqué activement) à +5 (Héros local / Accès exclusif)**, démarrant à 0 sauf la région d'origine du perso (+1 par défaut).

| Palier | Effet |
|---|---|
| **+5** | Héros local, accès exclusif : quêtes uniques, portes fermées à tous les autres qui s'ouvrent, cadeaux/faveurs sans contrepartie |
| **+3 / +4** | Allié reconnu : soutien actif possible (renforts, informations privilégiées), réductions marchandes importantes |
| **+1 / +2** | Cordial : attitude amicale, informations plus faciles à obtenir, petites réductions |
| **0** | Neutre, traitement standard |
| **-1 / -2** | Méfiant : réticence à aider, surveillance légère, prix légèrement gonflés |
| **-3 / -4** | Ennemi : prix fortement gonflés ou refus de vendre, accès interdit à certains lieux, surveillance active |
| **-5** | Traqué activement : primes sur la tête du personnage, la région peut organiser une chasse contre lui |

La réputation évolue selon les actions du groupe (quêtes accomplies, choix politiques, factions soutenues) et **peut avoir des répercussions croisées** : aider Demacia dans un conflit contre Noxus fera monter la réputation en Demacia... et baisser celle à Noxus. C'est le moteur principal des embranchements narratifs de la campagne (voir Runeterra-JDR-Campagne-Principale-Ouverture.md, section 7 — l'Horloge du Monde, document séparé du Manuel du Joueur).

---

## 4. Rôles et sous-rôles

Plutôt que 5 archétypes indépendants, le système repose maintenant sur **5 rôles** — calqués sur les postes réels de League of Legends — chacun décliné en **3 sous-rôles**, pour un total de 15. Le rôle correspond à la position/fonction du personnage dans le groupe ; le sous-rôle porte l'identité mécanique réelle (stats, dégâts, ressource).

| Rôle | Sous-rôles |
|---|---|
| **TOP** | Bruiser (façon Irelia, Camille, Fiora) / Juggernaut (façon Garen, Darius, Illaoi) / Tank (façon Malphite, Ornn, Sion) |
| **JUNGLE** | Assassin (façon Kha'Zix, Rengar, Evelynn) / Skirmisher (façon Xin Zhao, Warwick, Vi) / Vanguard (façon Sejuani, Zac, Amumu) |
| **MID** | Control Mage (façon Orianna, Anivia, Azir) / Battle Mage (façon Vladimir, Cassiopeia) / Artilleur — AP (façon Xerath, Ziggs, Syndra) |
| **ADC** | Hypercarry (façon Kog'Maw, Jinx, Vayne) / Sniper (façon Caitlyn, Ashe, Varus) / Caster — AD (façon Ezreal, Corki, Varus) |
| **SUPPORT** | Enchanteur (façon Janna, Lulu, Soraka) / Initiateur (façon Leona, Nautilus, Rakan) / Catcher (façon Thresh, Blitzcrank, Pyke) |

### 4.1 Modificateurs mécaniques par sous-rôle

Les modificateurs s'appliquent **par-dessus** la fourchette d'archétype de combat correspondante (Partie 1, section 3.3). Voici quel archétype sert de base à chaque sous-rôle — attention, deux sous-rôles de **Rôles différents** peuvent partager le même archétype de base sans être liés pour autant (ex. Tank et Vanguard ci-dessous) :

| Rôle | Sous-rôle | Archétype de combat de base (Partie 1, 3.3) |
|---|---|---|
| TOP | Bruiser | Juggernaut |
| TOP | Juggernaut | Juggernaut |
| TOP | Tank | Tank |
| JUNGLE | Assassin | Assassin |
| JUNGLE | Skirmisher | Juggernaut |
| JUNGLE | Vanguard | Tank |
| MID | Control Mage | Mage |
| MID | Battle Mage | Mage |
| MID | Artilleur (AP) | Mage |
| ADC | Hypercarry | Marksman |
| ADC | Sniper | Marksman |
| ADC | Caster (AD) | Marksman |
| SUPPORT | Enchanteur | Support |
| SUPPORT | Initiateur | Support |
| SUPPORT | Catcher | Support |

"Modif. Dégâts" s'applique à l'AD ou l'AP selon le sous-rôle. Les bonus de jet se réfèrent aux actions neutres du Partie 1, section 3.5.

| Rôle | Sous-rôle | Modif. PV | Modif. Dégâts (niv.1) | Vit. Dépl. | Ressource typique | Profil de scaling | Bonus de jet |
|---|---|---|---|---|---|---|---|
| TOP | **Bruiser** | ×1,0 | ×1,0 | Normale | Mana | Standard | +10 en Attaque immédiatement après une Esquive ou Parade réussie |
| TOP | **Juggernaut** | ×1,1 | ×1,1 | -1 | Sans ressource ou Fureur | Standard | +10 en Attaque en mêlée dès le 2ᵉ round consécutif contre la même cible |
| TOP | **Tank** | ×1,2 (le plus haut du jeu) | ×0,7 | -1 | Mana ou Sans ressource | Précoce | +10 en Esquive en s'interposant pour absorber les dégâts d'un allié (1×/round) |
| JUNGLE | **Assassin** | ×0,85 | ×1,2 | +1 | Énergie | Précoce | +15 au premier jet d'attaque ou de sort du combat (embuscade/gank) |
| JUNGLE | **Skirmisher** | ×0,95 | ×1,1 | +1 | Fureur ou Mana | Standard | +10 en Attaque contre une cible isolée (sans allié à portée courte) |
| JUNGLE | **Vanguard** | ×1,1 | ×0,8 | Normale | Mana | Précoce | +10 en Attaque ou Sort s'il agit avant tout le monde dans le combat (initiation) |
| MID | **Control Mage** | ×0,85 | ×1,0 | Normale | Mana | Standard | +10 en Sort magique visant 2 cibles ou plus |
| MID | **Battle Mage** | ×1,05 | ×0,95 | Normale | Mana | Standard | +10 en Concentration pour maintenir un sort en étant attaqué au contact |
| MID | **Artilleur (AP)** | ×0,75 (le plus fragile du jeu) | ×1,2 | Normale | Mana | Tardif | +10 en Sort magique contre une cible à portée longue (8m+) |
| ADC | **Hypercarry** | ×0,9 (niv.1) → ×1,1 (niv.18) | ×1,0 | Normale | Mana | Tardif | +1 dégât fixe cumulatif à chaque objet légendaire complété |
| ADC | **Sniper** | ×1,0 | ×1,0 | Normale | Mana modéré | Standard | +10 en Attaque à distance contre une cible à portée longue (8m+) |
| ADC | **Caster (AD)** | ×0,95 | ×1,05 | +1 | Mana faible ou Énergie | Standard | +10 en Sort après un déplacement dans le même round. *Particularité : ses sorts utilisent un ratio d'AD au lieu d'AP (voir Partie 1, section 3.4) — seul sous-rôle du jeu à mélanger dégâts physiques et lancement de sorts* |
| SUPPORT | **Enchanteur** | ×0,9 | ×0,7 | Normale | Mana élevé | Standard | +1d4 PV bonus sur ses soins/boucliers ciblant un allié sous 50% PV |
| SUPPORT | **Initiateur** | ×1,05 | ×0,85 | Normale | Mana | Précoce | +10 en Attaque ou Sort s'il agit avant tout le monde dans le combat |
| SUPPORT | **Catcher** | ×0,95 | ×0,8 | Normale | Mana | Standard | +10 en Sort de contrôle (immobilisation/attraction) visant une cible isolée |

*(Tous ces bonus s'appliquent comme le modificateur direct du Partie 1, section 2.3 Option B — un simple +X au Seuil de Réussite avant de lancer le d100.)*

### 4.2 Profils de scaling (progression niveau 1 → 18)

Chaque sous-rôle suit l'un de ces 3 profils pour sa progression de **dégâts** (AD ou AP) au fil des niveaux — les PV continuent de suivre la formule standard du Partie 1 (section 5.3) multipliée par le "Modif. PV" du tableau ci-dessus, sans changement selon le profil.

| Profil | Croissance des dégâts niv.1 → niv.18 | Logique |
|---|---|---|
| **Précoce** | ×1,3 (au lieu de ×1,6 standard) | Fort dès le niveau 1 (valeur indiquée dans la colonne "Modif. Dégâts"), plafonne plus vite : convient aux rôles utiles dès le début (tanks, engageurs) |
| **Standard** | ×1,6 (formule par défaut du Partie 1, section 5.3) | Croissance régulière, sans particularité |
| **Tardif** | Départ ×0,8 de la valeur indiquée en "Modif. Dégâts", puis croissance jusqu'à ×1,3 au niveau 18 (par rapport à cette valeur de départ réduite) | Faible en début de partie, devient dévastateur en fin de campagne : convient aux carries qui dépendent des objets/niveaux (Hypercarry, Artilleur) |

**Exemple comparatif à dégâts de base identiques (Modif. Dégâts ×1,0, disons 10 AD de base) :**
```
Précoce  : niveau 1 = 10 AD          → niveau 18 = 10 × 1,3 = 13 AD
Standard : niveau 1 = 10 AD          → niveau 18 = 10 × 1,6 = 16 AD
Tardif   : niveau 1 = 10 × 0,8 = 8 AD → niveau 18 = 8 × 1,3 = 10,4 AD (≈10 AD)
```
*(Le Tardif finit plus bas que le Standard en dégâts "bruts" de base — c'est normal, sa vraie force vient des synergies d'objets, pas du niveau brut. C'est le seul profil qui dévie de la formule standard du Partie 1, section 5.3 ; tous les autres sous-rôles la suivent, juste avec un point de départ différent selon les multiplicateurs ci-dessus.)*

---

## 5. Affinité élémentaire

Tout personnage peut choisir une **affinité élémentaire**, quel que soit son sous-rôle — pas seulement les lanceurs de sorts. Elle teinte narrativement et mécaniquement les dégâts du personnage (physiques ou magiques selon son sous-rôle).

### 5.1 Les 6 affinités

| Affinité | Bonus de dégâts | Effet secondaire | Bonus de jet | Faiblesse |
|---|---|---|---|---|
| **Eau** | Les attaques/sorts appliquent un ralentissement de -1 case de Vitesse de Déplacement (1 round) | 3 stacks de Givre cumulés sur la même cible = immobilisation 1 round | +10 en Attaque ou Sort contre une cible déjà ralentie | -2 dégâts fixes sur toutes ses attaques/sorts |
| **Feu** | +1d4 dégâts bonus sur cible déjà brûlée/enflammée | Sur réussite critique, applique Brûlure (3 dégâts/round pendant 2 rounds) | +10 en Attaque ou Sort contre une cible déjà affectée par le Feu | -2 dégâts fixes contre cible résistante au feu (Freljordiens, créatures de glace) |
| **Foudre** | Sur réussite critique, propage la moitié des dégâts infligés à une cible proche | Sur réussite critique, la cible perd sa prochaine action (étourdissement bref) | +10 en Attaque ou Sort contre une cible en contact avec l'eau ou du métal | -2 dégâts fixes en milieu aquatique/mouillé |
| **Terre** | +1d4 PV bonus sur ses sorts de soin/régénération, ou +1d4 dégâts bonus si la cible est immobilisée | Régénère 5 PV par round au lanceur tant qu'il reste en contact avec le sol/la végétation | +10 en Attaque ou Sort de soin/buff | -2 dégâts fixes, plus orienté soutien/contrôle |
| **Néant** | +1d6 dégâts bonus contre une cible sous 30% PV (finisher) | Sur réussite critique, applique Corruption (-5 en Résistance mentale à la cible) | +10 en Intimidation | +2 dégâts subis fixes de sources d'affinité Lumière |
| **Lumière** | +1d6 dégâts bonus contre les créatures Ombre/Néant | Ses attaques/sorts de zone soignent aussi 10 PV à un allié touché par la même zone | +10 en Résistance mentale contre la peur ou le contrôle mental | Présence "voyante" : désavantage en Discrétion ; -2 dégâts fixes contre une cible en territoire Néant pur |

*(Le calcul exact des bonus/malus de dégâts dans la formule finale se trouve au Partie 1, section 3.4ter — l'effet secondaire et le bonus de jet s'ajoutent par-dessus sans changer cette formule.)*

*Précision de lore : le Néant est littéralement l'absence de magie (Manuel du MJ, section 12), donc un personnage d'affinité Néant ne "lance" pas de sort au sens propre — il canalise la corruption et le vide comme une arme, souvent au prix de sa propre santé mentale. Une nuance purement narrative, sans impact sur les chiffres ci-dessus.*

### 5.2 Choix de l'affinité

L'affinité élémentaire reste **entièrement facultative**, quelle que soit la région d'origine du personnage — aucune région n'oblige à en choisir une. Un personnage peut très bien n'avoir aucune affinité élémentaire s'il le souhaite.

---

## 5bis. Langues de Runeterra

Pour garder le jeu simple à la table, **tous les personnages parlent et comprennent une seule et même langue commune**, quelle que soit leur région d'origine — pas de barrière de langue entre joueurs, ni entre un personnage et l'immense majorité des PNJ. Les particularités linguistiques mentionnées ça et là (le vastayen pour "Premières Terres" en Ionia, par exemple) sont des tournures culturelles, pas des langues séparées à apprendre.

**Une exception : l'Ancien.** Une langue morte, liée aux civilisations disparues et à la magie la plus profonde — les inscriptions runiques sur les Runes du Monde (Manuel du Joueur, section 8.2), les tablettes shurimaises antérieures à la Chute, les glyphes des ruines d'Icathia. Personne ne la parle couramment ; elle ne s'utilise que pour lire un texte ancien ou un artefact inscrit.

*Usage à la table : un personnage ne "sait" pas l'Ancien comme une compétence à cocher — un jet d'**Érudition** (INT, section 3.5) suffit pour déchiffrer une inscription en Ancien, avec un Désavantage si le texte est particulièrement obscur ou corrompu (au jugement du MJ). Une bonne occasion pour un personnage à haut INT (Control Mage, Artilleur AP...) de briller sur ce genre de découverte, sans ajouter de nouvelle mécanique.*

---

## 6. Feuille de synthèse à la création

```
Nom :
Région d'origine : ______ (trait culturel : ______ / bonus terrain connu : ______)
Race : ______ (bonus : ______ / malus : ______)
Rôle (TOP/JUNGLE/MID/ADC/SUPPORT) : ______ → Sous-rôle : ______
Affinité élémentaire (si applicable) : ______
Réputation de départ : Région d'origine +1, toutes les autres 0
Attributs (point-buy 21 points à la création, coût croissant, valeurs 8 à 15 avant race) : FOR__ DEX__ CON__ INT__ VOL__ CHA__
```


---

# PARTIE 3 — OBJETS & ÉQUIPEMENT

## 0. Règles d'inventaire

**6 emplacements d'objets actifs**, dont **1 réservé aux bottes** (un seul type de bottes porté à la fois, section 3) — soit 5 objets "libres" + 1 paire de bottes, exactement comme dans le jeu vidéo. Un personnage peut posséder plus d'objets dans ses affaires narrativement (un coffre, un sac), mais seuls ceux dans ces 6 emplacements donnent leurs bonus de statistiques actifs.

**Pas de système de poids, pas de zones corporelles (tête/buste/jambes...).** Le choix est volontaire : le jeu vidéo d'origine n'a jamais eu de gestion de poids ou d'emplacement par partie du corps, juste un inventaire de 6 cases — coller à ce principe garde le système simple à la table. Si un groupe veut plus de simulation, le MJ peut ajouter une règle maison, mais ce n'est pas le système par défaut.

**Consommables** (potions) ne comptent pas dans les 6 emplacements — ils se gèrent à part.

---

## 0bis. Kit d'aventurier (équipement non-combat)

Chaque personnage reçoit **gratuitement à la création** un kit d'équipement de base, purement narratif — il ne prend aucun des 6 emplacements d'objets et n'a aucun effet chiffré. Il sert de réponse par défaut à la question "est-ce que j'ai ça sur moi ?" pour tout ce qui n'est pas un objet de combat.

**Contenu du Kit d'aventurier :**
- Un sac à dos
- Une corde (10 mètres)
- Un silex et amadou (pour faire du feu)
- Une gourde
- Des rations de voyage (3 jours)
- Une couverture de couchage
- 3 torches
- Un petit nécessaire de réparation/couture

*Le MJ peut considérer ce kit comme acquis par défaut sans jet, sauf circonstance qui l'aurait fait perdre (naufrage, capture, fouille). Un objet plus spécifique et non couvert par le kit (grappin, kit de crochetage dédié, matériel d'escalade professionnel) reste à trouver ou acheter en jeu — voir Manuel du MJ, section 8bis, pour les prix courants.*

---

## 1. Objets de base (Basic items — 300-500 po)

Simples à trouver chez n'importe quel forgeron ou marchand, ils servent aussi de brique pour fabriquer des objets supérieurs (le MJ peut exiger de posséder les composants avant de "combiner" un objet supérieur, comme dans le jeu vidéo — optionnel).

| Objet | Prix | Effet |
|---|---|---|
| **Épée Longue** *(Long Sword)* | 350 po | +4 AD |
| **Tome d'Amplification** *(Amplifying Tome)* | 400 po | +10 AP |
| **Cristal de Rubis** *(Ruby Crystal)* | 400 po | +29 PV |
| **Armure d'Étoffe** *(Cloth Armor)* | 300 po | +8 Armure |
| **Manteau de Négatron** *(Null-Magic Mantle)* | 350 po | +8 RM |
| **Sceptre Vampirique** *(Vampiric Scepter)* | 450 po | regagne 1d4 PV par attaque de base touchée |
| **Cape d'Agilité** *(Cloak of Agility)* | 500 po | +15% Chance de Critique |
| **Dague** *(Dagger)* | 300 po | +10% Vitesse d'Attaque |
| **Larme de la Déesse** *(Tear of the Goddess)* | 400 po | +Réserve de ressource, évolue après un certain nombre de sorts lancés (voir section 4) |
| **Potion de Soin** *(Health Potion, consommable, hors emplacements)* | 50 po | Restaure 2d6+4 PV immédiatement, usage unique |

### Objets Doran — le vrai kit de départ

| Objet | Prix | Effet |
|---|---|---|
| **Casque de Doran** *(Doran's Helm)* | 450 po | +24 PV, +8 Armure, +8 RM |
| **Bouclier de Doran** *(Doran's Shield)* | 450 po | +21 PV. Passif : après avoir subi l'attaque d'un personnage, régénère 1d4 PV au début de son prochain tour (une seule fois par combat) |
| **Lame de Doran** *(Doran's Blade)* | 450 po | +10 AD, +15 PV. Passif : regagne 1 PV par attaque de base touchée |
| **Anneau de Doran** *(Doran's Ring)* | 400 po | +18 AP, +15 PV, régénère 2 points de réserve supplémentaires par round |
| **Arc de Doran** *(Doran's Bow)* | 400 po | +8 AD, +15% Vitesse d'Attaque. Passif : regagne 1 PV par attaque de base touchée |

### Objets de snowball

| Objet | Prix | Effet |
|---|---|---|
| **Sceau des Ténèbres** *(Dark Seal)* | 350 po | +9 PV, +15 AP. Passif "Gloire" : +2 AP par ennemi vaincu ou objectif de quête rempli (jusqu'à 5 stacks = +10 AP max) ; perd toutes ses stacks s'il tombe à 0 PV |
| **Moisson** *(Cull)* | 450 po | +7 AD. Régénère 3 PV par attaque de base touchée. Passif "Récolte" : +3 po par créature mineure vaincue (jusqu'à 60 po cumulés), puis +150 po immédiats une fois le plafond atteint |

---

## 2. Objets épiques (Epic items — 800-1200 po)

| Objet | Prix | Effet |
|---|---|---|
| **Zèle** *(Zeal)* | 950 po | +12% Vitesse d'Attaque, +15% Chance de Critique |
| **Gemme Exaltante** *(Kindlegem)* | 850 po | +29 PV. Passif : -1 round de recharge sur toutes ses compétences |
| **Hexdrinker** *(Hexdrinker)* | 1150 po | +8 AD, +15 RM. Passif : bouclier anti-magie de 1d6 PV qui se recharge après quelques rounds |
| **Dernier Souffle** *(Last Whisper)* | 1200 po | +8 AD. Passif : ignore 4 points d'Armure de la cible |
| **Protège-Bras du Savant** *(Seeker's Armguard)* | 900 po | +15 Armure. Évolue en objet légendaire plus tard |
| **Feu Follet Éthéré** *(Aether Wisp)* | 950 po | +18 AP, +1 case de Vitesse de Déplacement |
| **Appel du Bourreau** *(Executioner's Calling)* | 900 po | +8 AD. Passif : ses attaques appliquent l'Anti-soin (Partie 1, section 5.1ter) pendant 2 rounds |
| **Fléau** *(Phage)* | 1100 po (uniquement via craft, voir ci-dessous) | +8 AD, +29 PV. Passif "Rage" : gagne +1 case de Vitesse de Déplacement pendant 1 round après avoir touché une attaque de base ; tuer une cible donne cet effet doublé (2 rounds) |

### Système de craft (combiner des objets)

Comme dans le vrai jeu, la plupart des objets épiques, bottes et légendaires se combinent : possède les composants requis + paie des **frais d'assemblage** (moins cher que d'acheter l'objet final directement en une fois) pour obtenir l'objet supérieur. Les composants sont "consommés" dans la combinaison — ils ne comptent plus comme emplacements séparés, seul l'objet final occupe 1 emplacement.

**Réussir le craft demande un jet d'Érudition** (INT × 5, l'action neutre couvre déjà l'artisanat — section 3.5). Réussite : l'objet est fabriqué normalement. Échec : rien n'est perdu (composants, or et Rune intacts), mais la tentative échoue — on peut réessayer après un repos (section 7.9). Échec critique : un des composants est détruit dans le processus (au choix du MJ) et doit être racheté ou retrouvé avant de retenter.

*(Chaque objet légendaire nécessite aussi une Rune obtenue en jeu — jamais achetée en boutique. Voir section 8.2 pour la liste des Runes et comment les obtenir.)*

**Tableau des recettes** (toutes basées sur de vrais objets du jeu) :

**Objets épiques**

| Objet final | Recette | Coût total |
|---|---|---|
| Zèle *(Zeal)* | Cape d'Agilité + Dague + 100 po | 900 po |
| Gemme Exaltante *(Kindlegem)* | Cristal de Rubis + 400 po | 800 po |
| Hexdrinker *(Hexdrinker)* | Épée Longue + Manteau de Négatron + 400 po | 1100 po |
| Dernier Souffle *(Last Whisper)* | Épée Longue + 800 po | 1150 po |
| Protège-Bras du Savant *(Seeker's Armguard)* | Armure d'Étoffe + 550 po | 850 po |
| Feu Follet Éthéré *(Aether Wisp)* | Tome d'Amplification + 500 po | 900 po |
| Appel du Bourreau *(Executioner's Calling)* | Épée Longue + 500 po | 850 po |
| **Fléau** *(Phage)* | Épée Longue + Cristal de Rubis + 350 po | 1100 po |

**Bottes** — toutes construites à partir des Bottes de base (300 po) + frais :

| Objet final | Recette | Coût total |
|---|---|---|
| Jambières du Berzerker | Bottes + 800 po | 1100 po |
| Bottes de Lucidité | Bottes + 800 po | 1100 po |
| Chaussures du Sorcier | Bottes + 800 po | 1100 po |
| Coques en Acier | Bottes + 700 po | 1000 po |
| Sandales de Mercure | Bottes + 750 po | 1050 po |
| Bottes de Célérité | Bottes + 700 po | 1000 po |
| Grèves Gloutonnes | Bottes + 700 po | 1000 po |

**Objets légendaires** *(1 par sous-rôle + 3 iconiques, tous ouverts à n'importe qui ; chacun nécessite aussi une Rune obtenue en jeu, jamais achetée — voir section 8.2)* — la liste complète (recette de craft + prix + effet) est regroupée en un seul tableau **section 4**, pour ne pas avoir à chercher à deux endroits différents.

Deux légendaires illustrent bien la logique en cascade : Fléau → Couperet Noir (+ Épée Longue) et Fléau → Force de la Trinité (+ Dague) ; ou encore Zèle → Canon Ultrarapide (+ Dague) — exactement la chaîne du vrai jeu, où un objet épique sert de brique à plusieurs légendaires différents. Sans la Rune requise, ces recettes restent bloquées quel que soit l'or disponible — voir section 8.2 pour où les trouver.

---

## 3. Bottes (Boots — 900-1200 po, un seul type porté à la fois)

| Objet | Prix | Effet |
|---|---|---|
| **Bottes** *(Boots)* | 300 po | +1 Vitesse de Déplacement (niveau de base) |
| **Jambières du Berzerker** *(Berserker's Greaves)* | 1100 po | +1 Vitesse de Déplacement, +15% Vitesse d'Attaque |
| **Bottes de Lucidité** *(Ionian Boots of Lucidity)* | 1100 po | +1 Vitesse de Déplacement. Passif : -2 rounds de recharge sur toutes ses compétences |
| **Chaussures du Sorcier** *(Sorcerer's Shoes)* | 1100 po | +1 Vitesse de Déplacement. Passif : ignore 3 points de RM de la cible |
| **Coques en Acier** *(Plated Steelcaps)* | 1000 po | +1 Vitesse de Déplacement, +10 Armure. Passif : réduit de 2 les dégâts de chaque attaque de base subie |
| **Sandales de Mercure** *(Mercury's Treads)* | 1050 po | +1 Vitesse de Déplacement, +10 RM. Passif : réduit d'1 round la durée des Étourdissements/Immobilisations subis (minimum 1 round) |
| **Bottes de Célérité** *(Boots of Swiftness)* | 1000 po | +2 Vitesse de Déplacement (les seules à donner +2). Passif : résiste aux effets de Ralenti |
| **Grèves Gloutonnes** *(Gluttonous Greaves)* | 1000 po | +1 Vitesse de Déplacement. Passif : regagne 1d4 PV par attaque de base touchée |

---

## 4. Objets légendaires (2500-3600 po — uniquement via craft, voir Partie 3 section 2)

**1 objet légendaire signature par sous-rôle** — n'importe quel personnage peut l'équiper (rien ne le verrouille à son sous-rôle d'origine), mais c'est celui qui correspond le mieux à son identité. Chaque recette nécessite aussi une Rune obtenue en jeu, jamais achetée (section 8.2) :

| Sous-rôle | Objet | Recette de craft | Prix | Effet |
|---|---|---|---|---|
| Bruiser | **Danse de la Mort** *(Death's Dance)* | Épée Longue + Armure d'Étoffe + Rune du Sang + 900 po | 3000 po | +14 AD, +15 Armure. Passif : convertit une partie des dégâts subis en dégâts différés, réductibles en infligeant des dégâts pendant ce délai |
| Juggernaut | **Gage de Sterak** *(Sterak's Gage)* | Cristal de Rubis + Épée Longue + Rune de l'Acier + 900 po | 3100 po | +20 AD, +15 Armure. Passif : sous 40% PV, gagne un bouclier de 1d8+4 PV une fois par combat |
| Tank | **Présage de Randuin** *(Randuin's Omen)* | Armure d'Étoffe + Cristal de Rubis + Rune de l'Acier + 900 po | 2900 po | +88 PV, +15 Armure. Passif : les attaques ralentissent la cible de 2 cases de Vitesse de Déplacement pendant 2 rounds |
| Assassin | **Lame Spectre de Youmuu** *(Youmuu's Ghostblade)* | Épée Longue + Dague + Rune de la Furie + 900 po | 2700 po | +18 AD, +15% Critique. Passif : -1 round de recharge sur toutes ses compétences. Actif (1×/combat) : +1 case de Vitesse de Déplacement et +6 AD pendant 2 rounds |
| Skirmisher | **Lame du Roi Déchu** *(Blade of the Ruined King)* | Sceptre Vampirique + Épée Longue + Rune du Sang + 900 po | 3200 po | +10 AD, regagne 1d4 PV par attaque de base touchée, ses attaques infligent 1d6 dégâts bonus fixes. Actif (1×/combat) : inflige 1d8 dégâts, Ralentit 1 case (2 rounds) et se soigne de la moitié des dégâts infligés |
| Vanguard | **Couperet Noir** *(Black Cleaver)* | Fléau + Épée Longue + Rune de l'Acier + 700 po | 3000 po | +18 AD, +20 Armure. Passif : réduit l'Armure de la cible touchée de 6 (cumulable 3 fois) |
| Control Mage | **Bâton du Vide** *(Void Staff)* | Tome d'Amplification ×2 + Rune du Néant + 800 po | 3000 po | +30 AP. Passif : ignore 6 points de RM de la cible |
| Battle Mage | **Bâton de l'Archange** *(Archangel's Staff, évolue en Étreinte du Séraphin)* | Larme de la Déesse + Tome d'Amplification + Rune du Flux + 800 po | 2900 po | +25 AP, +Réserve de ressource. Passif : l'AP augmente avec la réserve maximale du personnage |
| Artilleur (AP) | **Coiffe de Rabadon** *(Rabadon's Deathcap)* | Tome d'Amplification ×2 + Rune du Néant + 900 po | 3600 po | +40 AP. Passif : +5 AP supplémentaires par tranche de 20 AP déjà possédée |
| Hypercarry | **Lame d'Infini** *(Infinity Edge)* | Cape d'Agilité + Épée Longue + Rune de l'Éclat + 900 po | 3000 po | +15 AD, +20% Critique. Passif : ses critiques infligent +1d6 dégâts fixes supplémentaires |
| Sniper | **Canon Ultrarapide** *(Rapid Firecannon)* | Zèle + Dague + Rune de l'Éclat + 800 po | 3000 po | +20% Vitesse d'Attaque, +20% Critique. Passif : après un déplacement, sa prochaine attaque a une portée doublée et touche en petite zone |
| Caster (AD) | **Manamune** *(évolue en Muramana)* | Larme de la Déesse + Épée Longue + Rune du Flux + 900 po | 3100 po | +18 AD, +Réserve de ressource. Passif : l'AD augmente encore avec la réserve maximale du personnage |
| Enchanteur | **Renouveleur de Pierre de Lune** *(Moonstone Renewer)* | Gemme Exaltante + Tome d'Amplification + Rune de l'Aube + 700 po | 2900 po | +20 AP, +Réserve de ressource. Passif : ses soins/boucliers touchent aussi un second allié proche pour moitié effet |
| Initiateur | **Médaillon de l'Iron Solari** *(Locket of the Iron Solari)* | Gemme Exaltante + Manteau de Négatron + Rune de l'Aube + 700 po | 2800 po | +59 PV, +Réserve de ressource. Actif (1×/combat) : place un bouclier de 1d6+4 PV sur tous les alliés proches |
| Catcher | **Voile de la Banshee** *(Banshee's Veil)* | Manteau de Négatron + Gemme Exaltante + Rune de l'Aube + 700 po | 2900 po | +40 RM, +29 PV. Passif : bloque le prochain effet de contrôle ou sort ciblé subi, se recharge après quelques rounds hors combat |

**+ 3 objets iconiques supplémentaires**, encore bien vivants dans le jeu aujourd'hui, ouverts à tous :

| Objet | Recette de craft | Prix | Effet |
|---|---|---|---|
| **Armure de Warmog** *(Warmog's Armor)* | Cristal de Rubis ×2 + Rune du Titan + 900 po | 3000 po | +106 PV. Passif : régénère 15 PV par round si aucun dégât subi depuis 2 rounds |
| **Égide Solaire** *(Sunfire Aegis)* | Armure d'Étoffe + Manteau de Négatron + Rune du Titan + 900 po | 3000 po | +29 PV, +20 Armure, +20 RM. Passif : aura qui inflige 1d4 dégâts par round aux ennemis proches |
| **Force de la Trinité** *(Trinity Force)* | Fléau + Dague + Rune de la Furie + 900 po | 3000 po | +10 AD, +10 AP, +12 PV, +15% Vitesse d'Attaque. Passif "Lame de Sheen" : après un sort, sa prochaine attaque de base inflige +1d6 dégâts bonus fixes |

---

## 5. Objets régionaux uniques — anciens objets historiques de League of Legends

Une sélection de **vrais objets ayant existé dans League of Legends**, aujourd'hui retirés du jeu ou remplacés. Chaque objet a été rattaché à la région qui lui correspond le mieux thématiquement.

| Objet | Région | Prix / Obtention | Effet |
|---|---|---|---|
| **Bannière de Commandement** *(Banner of Command)* | Demacia | Quête (forces royales) | +15 RM, +10 CHA. Passif (1×/combat) : donne à un allié +1d8 dégâts fixes sur sa prochaine attaque |
| **Étreinte du Feu Mortel** *(Deathfire Grasp)* | Noxus | 3200 po | +20 AP. Actif (1×/combat) : inflige des dégâts magiques ; la cible subit +1d4 dégâts bonus sur la prochaine attaque qu'elle reçoit ce round |
| **Lanterne de Wriggle** *(Wriggle's Lantern)* | Ionia | 2600 po | +8 AD, +10 Armure. Passif : regagne 1d4 PV par attaque touchant une créature (pas les personnages) ; peut éclairer une zone une fois par scène |
| **Proto-Ceinture Hextech-01** *(Hextech Protobelt-01)* | Piltover | 3000 po | +15 AP. Actif (recharge longue) : propulsion de 3m dans une direction, inflige des dégâts magiques en zone sur le trajet |
| **Tranchoir de Madred** *(Madred's Bloodrazor)* | Zaun | 2900 po | +10 AD. Passif : les attaques infligent 1d6 dégâts bonus fixes |
| **Massue Gelée** *(Frozen Mallet)* | Freljord | 3100 po | +59 PV, +8 AD. Passif : les attaques ralentissent la cible de 2 cases de Vitesse de Déplacement pendant 1 round |
| **Empaleur d'Atma** *(Atma's Impaler)* | Shurima | 2900 po | +15 Armure. Passif : +1 AD par tranche de 12 PV maximum possédés |
| **Coutelas de Bilgewater** *(Bilgewater Cutlass)* | Bilgewater | 2700 po | +10 AD. Passif : regagne 1d4 PV par attaque de base touchée. Actif (1×/combat) : grappin qui attire une cible ennemie à portée courte vers vous |
| **Sceptre Abyssal** *(Abyssal Scepter)* | Îles Obscures | 3000 po | +20 AP, +15 RM. Passif : réduit de 3 la RM des ennemis à portée courte |
| **Ombres Jumelles** *(Twin Shadows)* | Ixtal | 2800 po | +10 AP, +1 case de Vitesse de Déplacement. Actif (1×/scène) : envoie un éclaireur spectral scouter une zone ; les ennemis croisés doivent réussir un test de VOL ou fuir 1 round |
| **Héraut de Zeke** *(Zeke's Harbinger)* | Targon | 2900 po | +15 RM, +10 VOL. Passif : quand un allié à portée courte attaque, son attaque inflige des dégâts magiques bonus |
| **Pierre du Philosophe** *(Philosopher's Stone)* | Bandle City | 2200 po | +3 à tous les attributs. Régénération de ressource et de PV accrue entre les scènes |
| **Potion Corruptrice** *(Corrupting Potion)* | Kumungu | 300 po (usage unique) | Inflige un dégât magique continu à la prochaine cible touchée, puis soigne le porteur de 20 PV |
| **Portail Zz'Rot** *(Zz'Rot Portal)* | Néant | 2800 po | +59 PV, +15 Armure. Actif (1×/combat) : invoque un Rampant du Néant (voir le Manuel du Maître du Jeu) qui combat à vos côtés et attire l'attention des ennemis pendant 2 rounds |

---

## 6. Objets Jungle et Support (vrais objets du jeu, évolutifs)

**Ligne Jungle** — chaque sous-rôle JUNGLE a son propre "familier", qui inflige +5 dégâts bonus contre les créatures du Bestiaire (Manuel du Maître du Jeu) dès le départ, et évolue au niveau 6 :

| Objet de départ | Sous-rôle | Prix | Effet de départ | Évolution (niveau 6) |
|---|---|---|---|---|
| **Chiot Scorchclaw** *(Scorchclaw Pup)* | Assassin | 400 po | +5 AD ou +8 AP (au choix) | Sa prochaine attaque/sort contre un personnage inflige un dégât continu (1d4/round, 2 rounds) et Ralentit de 1 case |
| **Pousse Mosstomper** *(Mosstomper Seedling)* | Vanguard | 400 po | +8 Armure ou +8 RM (au choix) | Gagne un bouclier de 1d6+4 PV, qui se recharge après avoir vaincu une créature ou 2 rounds hors combat |
| **Oisillon Gustwalker** *(Gustwalker Hatchling)* | Skirmisher | 400 po | +5 AD | +1 Vitesse de Déplacement en Discrétion (couvert/ombre), +2 pendant 2 rounds après avoir vaincu une grosse créature |

**Ligne Support** — tous les sous-rôles SUPPORT démarrent avec le même objet de base, qui évolue vers une forme différente selon le sous-rôle au niveau 6 :

| Objet | Sous-rôle | Prix / Évolution | Effet |
|---|---|---|---|
| **Atlas du Monde** *(World Atlas)* | Tous les Supports (départ) | 400 po | +18 PV, régénère 3 points de réserve supplémentaires par round |
| **Créateur de Rêves** *(Dream Maker)* | Enchanteur (évolution niv.6) | 800 po | +24 PV, +20 à la réserve de ressource. Passif : ses soins/boucliers donnent aussi +1d4 dégâts magiques bonus et -2 dégâts subis à l'allié pendant 2 rounds |
| **Opposition Céleste** *(Celestial Opposition)* | Initiateur (évolution niv.6) | 800 po | +24 PV, +20 à la réserve de ressource. Passif : après avoir subi une attaque d'un personnage, réduit de 3 les dégâts qu'il subit pendant 1 round ; à la fin de cet effet, une onde Ralentit les ennemis proches de 1 case |
| **Traîneau du Solstice** *(Solstice Sleigh)* | Catcher (évolution niv.6) | 800 po | +24 PV, +20 à la réserve de ressource. Passif : chaque fois qu'il Ralentit ou Immobilise un ennemi, lui et l'allié le plus proche sous 50% PV gagnent +20 PV temporaires et +1 Vitesse de Déplacement pendant 1 round |

*(Les évolutions ne consomment pas un nouvel emplacement d'inventaire — l'objet se transforme à sa place, exactement comme dans le jeu vidéo.)*

## 7. Objets de départ par sous-rôle

Chaque personnage commence la partie avec un objet signature propre à son sous-rôle, plus 2 Potions de Soin communes à tous. **Or de départ : 0 po** (voir Partie 1, section 4, étape 6) — sauf exception ponctuelle liée à l'historique, au jugement du MJ.

| Rôle | Sous-rôle | Objet de départ | Objet réel correspondant |
|---|---|---|---|
| TOP | Tank | Casque de Doran + 2 Potions de Soin | Doran's Helmet |
| TOP | Juggernaut | Bouclier de Doran + 2 Potions de Soin | Doran's Shield |
| TOP | Bruiser | Lame de Doran + 2 Potions de Soin | Doran's Blade |
| JUNGLE | Assassin | Chiot Scorchclaw + 2 Potions de Soin | Scorchclaw Pup |
| JUNGLE | Vanguard | Pousse Mosstomper + 2 Potions de Soin | Mosstomper Seedling |
| JUNGLE | Skirmisher | Oisillon Gustwalker + 2 Potions de Soin | Gustwalker Hatchling |
| MID | Control Mage | Larme de la Déesse + 2 Potions de Soin | Tear of the Goddess |
| MID | Battle Mage | Sceau des Ténèbres + 2 Potions de Soin | Dark Seal |
| MID | Artilleur (AP) | Anneau de Doran + 2 Potions de Soin | Doran's Ring |
| ADC | Hypercarry | Moisson + 2 Potions de Soin | Cull |
| ADC | Sniper | Arc de Doran + 2 Potions de Soin | Doran's Bow |
| ADC | Caster (AD) | Lame de Doran + 2 Potions de Soin | Doran's Blade |
| SUPPORT | Enchanteur | Atlas du Monde + 2 Potions de Soin (→ Créateur de Rêves au niv.6) | World Atlas → Dream Maker |
| SUPPORT | Initiateur | Atlas du Monde + 2 Potions de Soin (→ Opposition Céleste au niv.6) | World Atlas → Celestial Opposition |
| SUPPORT | Catcher | Atlas du Monde + 2 Potions de Soin (→ Traîneau du Solstice au niv.6) | World Atlas → Solstice Sleigh |

*(Voir section 6 pour le détail des évolutions Jungle et Support au niveau 6.)*

## 8. Cas particulier — Kayn et la Faux Darkin

Kayn (Annexe Champions, sous-rôle Assassin) ne porte pas d'objet de départ classique : il possède déjà **Rhaast, la Faux Vivante**, une arme Darkin unique et non-achetable, qui remplace son emplacement d'arme habituel.

| Objet | Obtention | Effet |
|---|---|---|
| **Rhaast, la Faux Vivante** | Unique à Kayn, jamais en vente | +10 AD. Passif : c'est cette arme qui rend possible l'Ultime "Incursion Spectrale" (sans elle, Kayn n'aurait pas accès à sa Transformation). Le choix définitif entre Rhaast et Ombre au niveau 6 (voir sa fiche) est directement le fruit de la volonté de la lame elle-même autant que celle de Kayn — un bon accroche narrative pour le MJ. |

Cette arme ne compte pas dans les 6 emplacements normaux (elle est une extension de Kayn lui-même, pas un objet interchangeable) — elle reste avec lui même s'il "perd" ses autres objets narrativement.


---

---

*Fin du Manuel du Joueur. Les 36 champions prétirés se trouvent dans l'Annexe : Champions prétirés (document séparé). Voir le Manuel du Maître du Jeu pour le bestiaire et les conseils de jeu.*
