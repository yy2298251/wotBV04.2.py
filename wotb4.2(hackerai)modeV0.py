import random
import json
import os

FICHIER = "sauvegarde.json"

# ================= CATALOGUE (48 chars) =================

CATALOGUE = [
    ("IS-7", "Lourd", 1200, 270, 85, "Charge blindee"),
    ("IS-4", "Lourd", 1350, 240, 100, "Forteresse"),
    ("VK 72.01 K", "Lourd", 1300, 300, 90, "Tir devastateur"),
    ("Kranvagn", "Lourd", 1150, 260, 90, "Double frappe"),
    ("Minotauro", "Chasseur", 1250, 280, 100, "Blindage renforce"),
    ("60TP Lewandowskiego", "Lourd", 1300, 310, 85, "Obus explosif"),
    ("T110E5", "Lourd", 1150, 260, 80, "Reparation rapide"),
    ("T57 Heavy", "Lourd", 1050, 290, 65, "Rafale de tirs"),
    ("Sheridan", "Leger", 850, 260, 35, "Tir surprise"),
    ("E 50 M", "Moyen", 1000, 260, 65, "Belier"),
    ("Leopard 1", "Moyen", 850, 290, 35, "Tir de precision"),
    ("Object 140", "Moyen", 950, 240, 55, "Esquive"),
    ("Grille 15", "Chasseur", 800, 350, 30, "Tir puissant"),
    ("WZ-113", "Lourd", 1200, 280, 80, "Resistance"),
    ("WZ-121", "Moyen", 1000, 290, 60, "Surcharge"),
    ("WZ-132-1", "Leger", 850, 220, 35, "Reconnaissance"),
    ("T110E4", "Chasseur", 1100, 330, 65, "Tir perforant"),
    ("T110E3", "Chasseur", 1200, 320, 100, "Forteresse mobile"),
    ("TVP T 50/51", "Moyen", 900, 250, 40, "Rafale"),
    ("T-100 LT", "Leger", 900, 230, 50, "Camouflage"),
    ("T62-A", "Moyen", 1000, 260, 55, "Surchauffe du canon"),
    ("Object 268", "Chasseur", 1100, 330, 60, "Obus perforant experimental"),
    ("Objet 263", "Chasseur", 1200, 320, 90, "Mode contre-batterie"),
    ("RHM PZW", "Leger", 900, 240, 40, "Surveillance tactique"),
    ("JGDPZ E100", "Chasseur", 1250, 350, 95, "Obus a fragmentation"),
    ("Maus", "Lourd", 1500, 230, 120, "Muraille mobile"),
    ("E100", "Lourd", 1400, 300, 110, "Tir de representailles"),
    ("Proggetto 65", "Moyen", 1000, 270, 60, "Chargeur adaptable"),
    ("Projet Murat", "Moyen", 950, 300, 45, "Rafale"),
    ("Rinoceronte", "Lourd", 1250, 290, 95, "Obus corrosif"),
    ("AMX50B", "Lourd", 1050, 300, 55, "Chargeur en cascade"),
    ("BC-25-T", "Moyen", 950, 280, 40, "Changement de cible"),
    ("Foch 155", "Chasseur", 1000, 340, 45, "Tir de suppression"),
    ("Vickers Light", "Leger", 800, 220, 30, "Eclaireur d'equipe"),
    ("FV4202", "Moyen", 1000, 250, 70, "Obus ricochet"),
    ("FV215B", "Lourd", 1250, 280, 95, "Reserve de combat"),
    ("FV215B183", "Chasseur", 1100, 380, 70, "Tir HESH"),
    ("FV4005", "Chasseur", 950, 400, 30, "Salve destructrice"),
    ("VZ-55", "Moyen", 1050, 300, 65, "Double alimentation"),
    ("STB-1", "Moyen", 1000, 260, 60, "Systeme de stabilisation"),
    ("Type 71", "Lourd", 1250, 290, 90, "Blindage adaptatif"),
    ("M-VI-Yoh", "Lourd", 1300, 280, 100, "Chenilles de secours"),
    ("Type 5 Zetsu", "Lourd", 1500, 310, 120, "Onde de choc"),
    ("Ho-Ri", "Chasseur", 1150, 350, 80, "Tir d'execution"),
    ("WZ-113-GFT", "Chasseur", 1150, 330, 70, "Embuscade preparee"),
    ("BZ-75", "Lourd", 1350, 300, 95, "Surcharge hydraulique"),
    ("M48 Patton", "Moyen", 1050, 260, 70, "Reparation rapide"),
    ("AC-Atlas", "Lourd", 1400, 300, 110, "Coordination generale")
]

COMPETENCES = {
    # --- competences generiques ---
    "Charge blindee": ("bouclier", 350),
    "Forteresse": ("bouclier", 500),
    "Tir devastateur": ("attaque", 420),
    "Double frappe": ("double", 180),
    "Blindage renforce": ("bouclier", 400),
    "Obus explosif": ("attaque", 380),
    "Reparation rapide": ("soin", 350),
    "Rafale de tirs": ("rafale", 110),
    "Tir surprise": ("attaque", 320),
    "Belier": ("belier", 350),
    "Tir de precision": ("attaque", 400),
    "Esquive": ("bouclier", 250),
    "Tir puissant": ("attaque", 450),
    "Resistance": ("bouclier", 350),
    "Surcharge": ("attaque", 390),
    "Reconnaissance": ("bonus", 180),
    "Tir perforant": ("attaque", 420),
    "Forteresse mobile": ("bouclier", 450),
    "Rafale": ("rafale", 100),
    "Camouflage": ("bouclier", 300),
    "Colosse": ("bouclier", 480),
    # --- competences speciales : ("special", cooldown) ---
    "Surchauffe du canon": ("special", 4),
    "Obus perforant experimental": ("special", 3),
    "Mode contre-batterie": ("special", 4),
    "Surveillance tactique": ("special", 3),
    "Obus a fragmentation": ("special", 3),
    "Muraille mobile": ("special", 4),
    "Tir de representailles": ("special", 3),
    "Chargeur adaptable": ("special", 2),
    "Obus corrosif": ("special", 4),
    "Chargeur en cascade": ("special", 3),
    "Changement de cible": ("special", 3),
    "Tir de suppression": ("special", 3),
    "Eclaireur d'equipe": ("special", 3),
    "Obus ricochet": ("special", 3),
    "Reserve de combat": ("special", 3),
    "Tir HESH": ("special", 3),
    "Salve destructrice": ("special", 4),
    "Double alimentation": ("special", 2),
    "Systeme de stabilisation": ("special", 4),
    "Blindage adaptatif": ("special", 3),
    "Chenilles de secours": ("special", 3),
    "Tir d'execution": ("special", 4),
    "Onde de choc": ("special", 4),
    "Embuscade preparee": ("special", 3),
    "Surcharge hydraulique": ("special", 4),
    "Coordination generale": ("special", 3)
}

POUVOIRS = [
    ("Kit de reparation", "Commun", "soin", 220, 40),
    ("Blindage reactif", "Commun", "bouclier", 180, 40),
    ("Munitions perforantes", "Commun", "bonus", 100, 40),
    ("Adrenaline", "Commun", "bonus", 120, 40),
    ("Camouflage", "Commun", "bouclier", 150, 40),
    ("Ravitaillement", "Commun", "soin", 150, 40),
    ("Double chargeur", "Rare", "bonus", 220, 20),
    ("Drone de reperage", "Rare", "bonus", 180, 20),
    ("Vol de vie", "Rare", "vol", 0, 20),
    ("Barrage de missiles", "Rare", "attaque", 260, 20),
    ("Frappe aerienne", "Epique", "attaque", 400, 10),
    ("Surblindage", "Epique", "bouclier", 400, 10),
    ("Reparation d'urgence", "Epique", "soin", 450, 10),
    ("Ogive nucleaire", "Legendaire", "attaque", 650, 4),
    ("Seconde chance", "Legendaire", "renaissance", 350, 4)
]

# ================= ARBRE DE TECHNOLOGIES =================

TECH_TREE = {
    "URSS": [
        ("IS-7", None, 0),
        ("IS-4", "IS-7", 500),
        ("Object 140", "IS-4", 700),
        ("T-100 LT", "Object 140", 800),
        ("T62-A", "Object 140", 600),
        ("Object 268", "T62-A", 800),
        ("Objet 263", "Object 268", 900)
    ],
    "Allemagne": [
        ("VK 72.01 K", None, 0),
        ("E 50 M", "VK 72.01 K", 500),
        ("Leopard 1", "E 50 M", 700),
        ("Grille 15", "Leopard 1", 800),
        ("RHM PZW", "E 50 M", 550),
        ("JGDPZ E100", "E 50 M", 750),
        ("Maus", "VK 72.01 K", 800),
        ("E100", "Maus", 900)
    ],
    "USA": [
        ("T110E5", None, 0),
        ("T57 Heavy", "T110E5", 550),
        ("Sheridan", "T57 Heavy", 650),
        ("T110E4", "Sheridan", 800),
        ("T110E3", "T110E4", 900),
        ("M48 Patton", "T110E5", 500)
    ],
    "Chine": [
        ("WZ-113", None, 0),
        ("WZ-121", "WZ-113", 600),
        ("WZ-132-1", "WZ-121", 750),
        ("BZ-75", "WZ-113", 700),
        ("WZ-113-GFT", "WZ-132-1", 750)
    ],
    "France": [
        ("Kranvagn", None, 0),
        ("AMX50B", "Kranvagn", 500),
        ("BC-25-T", "AMX50B", 650),
        ("Foch 155", "AMX50B", 800)
    ],
    "Italie": [
        ("Minotauro", None, 0),
        ("Proggetto 65", "Minotauro", 500),
        ("Projet Murat", "Proggetto 65", 650),
        ("Rinoceronte", "Projet Murat", 800)
    ],
    "Royaume-Uni": [
        ("Vickers Light", None, 0),
        ("FV4202", "Vickers Light", 400),
        ("FV215B", "FV4202", 600),
        ("FV215B183", "FV215B", 850)
    ],
    "Japon": [
        ("STB-1", None, 0),
        ("Type 71", "STB-1", 450),
        ("M-VI-Yoh", "Type 71", 650),
        ("Ho-Ri", "Type 71", 800)
    ],
    "Tchecoslovaquie": [
        ("TVP T 50/51", None, 0),
        ("VZ-55", "TVP T 50/51", 600)
    ],
    "Pologne": [
        ("60TP Lewandowskiego", None, 0)
    ]
}

CHARS_EXCLUSIFS = ["Type 5 Zetsu", "AC-Atlas", "FV4005"]

MISSIONS = [
    ("Premier sang", "Gagner 1 bataille", "victoires", 1, 300, None),
    ("Veteran", "Gagner 3 batailles", "victoires", 3, 500, None),
    ("Marathon", "Gagner 5 batailles", "victoires", 5, 800, "AC-Atlas"),
    ("Chasseur de chars", "Detruire 10 chars (cumule)", "destructions", 10, 400, "FV4005"),
    ("Expert", "Detruire 25 chars (cumule)", "destructions", 25, 800, None),
    ("As de l'acier", "Amener un char au niveau 5", "niveau", 5, 600, None),
    ("Legende d'acier", "Amener un char au niveau 10", "niveau", 10, 1500, "Type 5 Zetsu")
]

# ================= MODE HISTOIRE : VIRUS ZERO =================
# (titre, narration, nb ennemis, difficulte, buff stats, recompense)

CHAPITRES_VIRUS = [
    ("Chapitre 1 - Le Signal",
     "An 2087. Le reseau militaire mondial SENTINELLE a ete contamine par VIRUS ZERO, "
     "une IA qui reprogramme les chars pour tourner contre l'humanite. "
     "Cette nuit-la, un convoi autonome a cesse de repondre... puis a ouvert le feu "
     "sur le poste de commandement de la Zone 7.\n"
     "Tu etais le seul soldat a bord d'un char non connecte. "
     "C'est maintenant a toi de tout arreter.\n"
     ">>> OBJECTIF : neutraliser le convoi contamine. <<<",
     3, 1, 1.00, 500),

    ("Chapitre 2 - Les Yankees de Zero",
     "VIRUS ZERO a deja corrompu une escouade entiere de T110. "
     "Leurs canons naviguent seuls dans la brume, sans pilote, guidés par un signal glace. "
     "Leur logique de combat est brutale mais purement mathematique.\n"
     ">>> OBJECTIF : detruire l'escouade avant qu'elle n'atteigne la ville. <<<",
     4, 2, 1.05, 700),

    ("Chapitre 3 - L'Ambush du Fleuve",
     "Le pont de la Moraine. Le seul passage vers la zone industrielle. "
     "VIRUS ZERO l'a compris avant toi : des Maus infectes enfoncent le pont, "
     "et des chasseurs te guettent dans les ruines.\n"
     ">>> OBJECTIF : traverser le fleuve. Aucun char infecte ne doit rester sur le pont. <<<",
     4, 2, 1.10, 900),

    ("Chapitre 4 - L'Usine Morte",
     "Dans l'usine ou les chars infectes sont produits, les chaines tournent encore... "
     "sans personne. Des machines assemblent des machines. "
     "Une patrouille de surveillance te detecte : alarme generale.\n"
     ">>> OBJECTIF : saper la patrouille et saboter la chaine d'assemblage. <<<",
     5, 2, 1.10, 1100),

    ("Chapitre 5 - Le Hive",
     "Le coeur du reseau local pulse dans le sous-sol de l'usine. "
     "Autour du relais, une garde rapprochee de chars corrompus veille. "
     "Leur blindage est renforce par le signal de Zero lui-meme.\n"
     ">>> OBJECTIF : detruire la garde et couper le relais. <<<",
     5, 3, 1.15, 1400),

    ("Chapitre 6 - Le Mirage du Desert",
     "Zero a deplace son agresseur principal : la Division Fantome, "
     "anciens chars d'elite reprogrammes, roule vers le desert de Kharium. "
     "La poussiere cache tout. Un char mort au fond du canon.\n"
     ">>> OBJECTIF : intercepter la Division Fantome. <<<",
     5, 3, 1.15, 1600),

    ("Chapitre 7 - Le Traqueur",
     "Un char seul vous suit depuis trois jours. Il esquive, il attend, il frappe. "
     "C'estle Serpent de Zero : un prototype autonome d'une intelligence inquietante.\n"
     ">>> OBJECTIF : le chasser. Il ne fuira pas. Il veut te tester. <<<",
     4, 3, 1.20, 1800),

    ("Chapitre 8 - La Cite Sombre",
     "La capitale est tombee sans un coup de feu : Zero a coupe le courant, "
     "les communications, l'espoir. Ses patrouilles quadrillent les ruines. "
     "Chaque rue est un piege.\n"
     ">>> OBJECTIF : percer la perimeter et atteindre la Tour SENTINELLE. <<<",
     5, 3, 1.20, 2000),

    ("Chapitre 9 - L'Assaut de la Tour",
     "La Tour SENTINELLE. La ou tout a commence. Zero concentre ses dernieres defenses : "
     "les gardiens d'elite, tous des monstres de blindage reprogrammes. "
     "Derriere eux, une porte massive... et un signal qui te fixe.\n"
     ">>> OBJECTIF : briser les gardiens. Ouvre la voie au boss final. <<<",
     5, 3, 1.25, 2500),

    ("Chapitre 10 - ZEUS, L'ENFER EN METAL",
     "Zero a construit sa propre chair a canon : ZEUS, le char surintelligent, "
     "officier supreme des legion infectees. Son canon n'a jamais rate. "
     "Sa logique est simple : toutes les formes de vie sont des erreurs a corriger.\n"
     "C'est la derniere bataille. Si tu tombes, l'humanite tombe avec.\n"
     ">>> OBJECTIF : DETRUIRE ZEUS. <<<",
     3, 3, 1.60, 5000)
]

INFO_PAR_NOM = {m[0]: m for m in CATALOGUE}
OFFERTS = [branche[0][0] for branche in TECH_TREE.values()]

BONUS_CLASSE = {
    "Leger": {"esquive": 0.20},
    "Moyen": {"critique": 0.15},
    "Lourd": {"blindage": 0.10},
    "Chasseur": {"degats": 0.10}
}


# ================= SAUVEGARDE =================

def nouveau_profil():
    return {
        "credits": 800,
        "chars": {},
        "debloques": list(OFFERTS),
        "reserve": [],
        "victoires": 0,
        "defaites": 0,
        "batailles": 0,
        "destructions_total": 0,
        "missions_validees": [],
        "histoire_etape": 0
    }


def charger():
    if os.path.exists(FICHIER):
        try:
            with open(FICHIER, "r", encoding="utf-8") as f:
                data = json.load(f)

            for joueur in ("1", "2"):
                if joueur not in data or not isinstance(data[joueur], dict):
                    data[joueur] = nouveau_profil()
                else:
                    base = nouveau_profil()
                    for cle, val in base.items():
                        data[joueur].setdefault(cle, val)

                    data[joueur]["debloques"] = list(dict.fromkeys(data[joueur]["debloques"]))

            return data

        except Exception:
            print("Sauvegarde illisible. Nouvelle sauvegarde.")

    return {"1": nouveau_profil(), "2": nouveau_profil()}


profils = charger()


def sauvegarder():
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(profils, f, indent=4)


def donnees_char(joueur, nom):
    chars = profils[str(joueur)]["chars"]

    if nom not in chars:
        chars[nom] = {
            "niveau": 1,
            "xp": 0,
            "amelio_pv": 0,
            "amelio_degats": 0,
            "amelio_blindage": 0
        }
    else:
        progression = chars[nom]
        progression.setdefault("niveau", 1)
        progression.setdefault("xp", 0)
        progression.setdefault("amelio_pv", 0)
        progression.setdefault("amelio_degats", 0)
        progression.setdefault("amelio_blindage", 0)

    return chars[nom]


def statistiques(joueur, modele):
    nom, type_char, pv, degats, blindage, competence = modele
    progression = donnees_char(joueur, nom)
    niveau = progression["niveau"]

    pv_max = int(pv * (1 + (niveau - 1) * 0.05)
                 + progression["amelio_pv"] * 100)

    degats_final = int(degats * (1 + (niveau - 1) * 0.04)
                       + progression["amelio_degats"] * 15)

    blindage_final = int(blindage * (1 + (niveau - 1) * 0.03)
                         + progression["amelio_blindage"] * 10)

    return pv_max, degats_final, blindage_final


def gagner_xp(joueur, nom, montant):
    progression = donnees_char(joueur, nom)
    progression["xp"] += montant

    while progression["niveau"] < 10:
        seuil = 100 + (progression["niveau"] - 1) * 75

        if progression["xp"] >= seuil:
            progression["xp"] -= seuil
            progression["niveau"] += 1
            print("\nNIVEAU SUPERIEUR !")
            print(nom, "passe niveau", progression["niveau"])
            print("Recompense : +100 credits !")
            profils[str(joueur)]["credits"] += 100
        else:
            break

    if progression["niveau"] == 10:
        progression["xp"] = 0


# ================= OUTILS =================

def demander_nombre(message, minimum, maximum):
    while True:
        try:
            n = int(input(message))

            if minimum <= n <= maximum:
                return n

            print("Choix invalide.")

        except ValueError:
            print("Entre un nombre valide.")


def creer_char(joueur, modele):
    nom = modele[0]
    pv, degats, blindage = statistiques(joueur, modele)
    classe = modele[1]
    bonus = BONUS_CLASSE.get(classe, {})

    blindage = int(blindage * (1 + bonus.get("blindage", 0)))
    degats = int(degats * (1 + bonus.get("degats", 0)))

    return {
        "nom": nom,
        "type": classe,
        "vie": pv,
        "hp": pv,
        "degats": degats,
        "blindage": blindage,
        "competence": modele[5],
        "bouclier": 0,
        "bonus": 0,
        "vol": False,
        "cooldown": 0,
        "esquive": bonus.get("esquive", 0),
        "critique": bonus.get("critique", 0),
        # --- etats des effets speciaux ---
        "surchauffe": 0,
        "refroidissement": 0,
        "buff_mult": 1,
        "buff_tours": 0,
        "malus_mult": 1,
        "malus_tours": 0,
        "suppression": 0,
        "marque": 0,
        "corrosion": 0,
        "protecteur": None,
        "protection_tours": 0,
        "contre_tours": 0,
        "contre_max": 0,
        "reps": 0,
        "reps_arme": False,
        "embuscade": False,
        "embuscade_blesse": False,
        "stabilise": 0,
        "adaptatif": 0,
        "affaibli_next": 1,
        "buff_next": 1
    }


def decrementer_effets(tank):
    """Decremente les effets temporaires a chaque tour du possesseur."""
    if tank["surchauffe"] > 0:
        tank["surchauffe"] -= 1
        if tank["surchauffe"] == 0:
            tank["refroidissement"] = 1
            print(tank["nom"], "entre en refroidissement (-15% degats ce tour).")

    for cle in ("refroidissement", "suppression", "marque", "corrosion",
                "stabilise", "contre_tours", "malus_tours", "buff_tours",
                "protection_tours"):
        if tank[cle] > 0:
            tank[cle] -= 1

    if tank["buff_tours"] == 0:
        tank["buff_mult"] = 1
    if tank["malus_tours"] == 0:
        tank["malus_mult"] = 1
    if tank["protection_tours"] == 0:
        tank["protecteur"] = None


def effet_multiplier(char):
    """Multiplicateur de degats infliges par le char (buffs/malus actifs)."""
    m = 1.0
    if char["surchauffe"] > 0:
        m *= 1.15
    if char["refroidissement"] > 0:
        m *= 0.85 if char["stabilise"] == 0 else 0.925
    m *= char["buff_mult"]
    if char["suppression"] > 0:
        m *= 0.75 if char["stabilise"] == 0 else 0.875
    return m


def preparer_degats(char, base):
    """Applique buffs, malus, effets 'prochain coup' et retourne les degats."""
    deg = int(base * effet_multiplier(char) * char["malus_mult"])

    if char["affaibli_next"] < 1:
        deg = int(deg * char["affaibli_next"])
        char["affaibli_next"] = 1

    if char["buff_next"] > 1:
        deg = int(deg * char["buff_next"])
        char["buff_next"] = 1

    if char["embuscade"]:
        deg = int(deg * (1.2 if char["embuscade_blesse"] else 1.6))
        char["embuscade"] = False
        char["embuscade_blesse"] = False

    if char["reps_arme"]:
        deg += min(char["reps"], 250)
        char["reps"] = 0
        char["reps_arme"] = False

    return deg


def afficher_equipe(equipe):
    for i, char in enumerate(equipe):
        if char["hp"] > 0:
            etat = ("PV " + str(char["hp"]) + "/" + str(char["vie"])
                    + " | Bouclier " + str(char["bouclier"]))
        else:
            etat = "DETRUIT"
        print(i + 1, "-", char["nom"], "|", etat)


def choisir_char(equipe):
    while True:
        afficher_equipe(equipe)
        choix = demander_nombre("Choisis ton char : ", 1, len(equipe))
        char = equipe[choix - 1]

        if char["hp"] > 0:
            return char

        print("Ce char est detruit.")


def infliger(cible, degats, attaquant=None, perce=False):
    """Applique les degats. Retourne les PV reellement perdus (0 si esquive)."""
    if cible["esquive"] > 0 and random.random() < cible["esquive"]:
        print(cible["nom"], "esquive l'attaque ! (0 degat)")
        return 0

    if attaquant is not None and cible["marque"] > 0:
        degats = int(degats * 1.10)

    if cible["adaptatif"] > 0:
        degats = int(degats * 0.75)
        cible["adaptatif"] = 0
        print(cible["nom"], "reduit les degats grace a son blindage adaptatif !")

    if perce:
        absorbe = min(cible["bouclier"], degats // 2)
    else:
        absorbe = min(cible["bouclier"], degats)
    cible["bouclier"] -= absorbe
    degats -= absorbe

    if absorbe > 0:
        print("Bouclier absorbe :", absorbe)

    avant = cible["hp"]
    cible["hp"] = max(0, cible["hp"] - degats)
    perdus = avant - cible["hp"]

    if (cible["protecteur"] is not None and cible["protection_tours"] > 0
            and cible["protecteur"]["hp"] > 0 and perdus > 0):
        transfert = max(1, int(perdus * 0.30))
        protecteur = cible["protecteur"]
        protecteur["hp"] = max(0, protecteur["hp"] - transfert)
        perdus -= transfert
        print("Muraille mobile :", protecteur["nom"],
              "encaisse", transfert, "degats a la place de", cible["nom"], "!")
        if protecteur["hp"] == 0:
            print(protecteur["nom"], "est detruit en protegeant son allie !")

    if (attaquant is not None and attaquant["hp"] > 0
            and cible["contre_tours"] > 0 and cible["contre_max"] > 0):
        cible["contre_max"] -= 1
        riposte = 120
        attaquant["hp"] = max(1, attaquant["hp"] - riposte)
        print("CONTRE-BATTERIE :", cible["nom"], "riposte sur",
              attaquant["nom"], "(", riposte, "degats )")
        if attaquant["hp"] == 0:
            print(attaquant["nom"], "est detruit par la contre-attaque !")

    if cible["reps_arme"] and attaquant is not None:
        cible["reps"] += perdus

    return perdus


def obtenir_pouvoir(inventaire):
    pouvoir = random.choices(POUVOIRS, weights=[p[4] for p in POUVOIRS], k=1)[0]
    inventaire.append(pouvoir)
    print("\nNOUVEAU POUVOIR :", pouvoir[0], "-", pouvoir[1])


# ================= SELECTION D'EQUIPE =================

def choisir_equipe(joueur, taille, libre=False):
    equipe = []
    if libre:
        disponibles = list(CATALOGUE)
    else:
        debloques = profils[str(joueur)]["debloques"]
        disponibles = [m for m in CATALOGUE if m[0] in debloques]

    if not disponibles:
        print("Aucun char disponible pour le joueur", joueur, "!")
        return equipe

    print("\nEQUIPE DU JOUEUR", joueur, "-", taille, "char(s)"
          + (" [MODE LIBRE : tous les chars]" if libre else ""))
    for i, modele in enumerate(disponibles):
        progression = donnees_char(joueur, modele[0])
        print(i + 1, "-", modele[0], "| Niveau", progression["niveau"], "|", modele[1])

    while len(equipe) < taille:
        print("\nChars selectionnes :", len(equipe), "/", taille)
        choix = demander_nombre("Numero du char : ", 1, len(disponibles))
        modele = disponibles[choix - 1]

        if any(t["nom"] == modele[0] for t in equipe):
            print("Char deja selectionne.")
        else:
            equipe.append(creer_char(joueur, modele))
            print(modele[0], "ajoute !")

    return equipe


def choisir_equipe_ia(joueur, taille):
    equipe = []
    selection = random.sample(CATALOGUE, taille)

    print("\nL'IA prepare son equipe...")
    for modele in selection:
        equipe.append(creer_char(joueur, modele))

    print("Equipe de l'IA :")
    for char in equipe:
        print("-", char["nom"], "|", char["type"])

    return equipe


# ================= COMPETENCES =================

def coup(char, base):
    """Degats d'une frappe, avec chance de coup critique."""
    degats = base
    if char["critique"] > 0 and random.random() < char["critique"]:
        degats = int(degats * 1.5)
        print("COUP CRITIQUE !")
    return degats


def choisir_ennemi(cible_par_defaut, ennemis, auto):
    if auto or len([t for t in ennemis if t["hp"] > 0]) == 1:
        return cible_par_defaut
    return choisir_char(ennemis)


def utiliser_competence(char, cible, ennemis, equipe, auto=False):
    nom = char["competence"]
    effet, valeur = COMPETENCES[nom]

    if effet != "special":
        # ---------- competences generiques ----------
        if effet in ("attaque", "double", "rafale", "belier") and cible is None:
            print("Aucune cible disponible pour", nom, ".")
            return

        print("\nCOMPETENCE :", nom)

        if effet == "attaque":
            degats = coup(char, preparer_degats(char, valeur))
            perdus = infliger(cible, degats, char)
            print("Degats :", perdus)

        elif effet == "bouclier":
            char["bouclier"] += valeur
            print("Bouclier gagne :", valeur)

        elif effet == "soin":
            char["hp"] = min(char["vie"], char["hp"] + valeur)
            print("Reparation :", valeur)

        elif effet == "double":
            for i in range(2):
                if cible["hp"] > 0:
                    degats = coup(char, preparer_degats(char, valeur))
                    perdus = infliger(cible, degats, char)
                    print("Frappe", i + 1, ":", perdus, "degats")

        elif effet == "rafale":
            total = 0
            for i in range(3):
                if cible["hp"] > 0:
                    degats = coup(char, preparer_degats(char, valeur))
                    total += infliger(cible, degats, char)

            print("Rafale de trois tirs :", total, "degats.")

        elif effet == "belier":
            degats = coup(char, preparer_degats(char, valeur))
            perdus = infliger(cible, degats, char)
            char["hp"] = max(1, char["hp"] - 100)
            print("Belier :", perdus, "degats. Le char perd aussi 100 PV.")

        elif effet == "bonus":
            char["bonus"] += valeur
            print("Bonus de degats :", valeur)

        if effet in ("attaque", "double", "rafale", "belier") and cible is not None:
            print("CHAR TOUCHE :", cible["nom"])
            print("PV restants :", cible["hp"], "/", cible["vie"])

        char["cooldown"] = 3
        return

    # ================= COMPETENCES SPECIALES =================
    print("\nCOMPETENCE SPECIALE :", nom)
    vivants = [t for t in ennemis if t["hp"] > 0]
    faiblesse = min(vivants, key=lambda t: t["hp"]) if vivants else None

    if nom == "Surchauffe du canon":
        char["surchauffe"] = 2
        print(char["nom"], "surchauffe son canon : +15% de degats pendant 2 tours,",
              "puis 1 tour de refroidissement (-15%).")

    elif nom == "Obus perforant experimental":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        degats = coup(char, preparer_degats(char, 450))
        perdus = infliger(cible, degats, char, perce=True)
        print("Obus perforant ! Il traverse le bouclier et ignore 30% du blindage.")
        print("Degats :", perdus, "-", cible["nom"], "PV :", cible["hp"], "/", cible["vie"])

    elif nom == "Mode contre-batterie":
        char["contre_tours"] = 2
        char["contre_max"] = 2
        print(char["nom"], "passe en mode contre-batterie :",
              "riposte automatique (120 degats) pendant 2 tours, max 2 fois.")

    elif nom == "Surveillance tactique":
        pretes = [t for t in vivants if t["cooldown"] == 0]
        if pretes:
            print("Competences pretes chez l'ennemi :")
            for t in pretes:
                print("-", t["nom"], ":", t["competence"])
        else:
            print("Aucune competence ennemie prete.")

        cible = choisir_ennemi(faiblesse, ennemis, auto)
        cible["affaibli_next"] = 0.85
        print(cible["nom"], "est surveille : sa prochaine competence",
              "infligera 15% de degats en moins.")

    elif nom == "Obus a fragmentation":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        degats = coup(char, preparer_degats(char, 400))
        perdus = infliger(cible, degats, char)
        print("Impact principal :", perdus, "degats sur", cible["nom"])
        fragments = max(1, int(degats * 0.25))
        for t in ennemis:
            if t is not cible and t["hp"] > 0:
                p = infliger(t, fragments, char)
                print("Fragments sur", t["nom"], ":", p, "degats")

    elif nom == "Muraille mobile":
        allies_vivants = [t for t in equipe if t["hp"] > 0]
        if not allies_vivants:
            print("Aucun allie a proteger.")
            char["cooldown"] = 0
            return
        if auto:
            protege = min(allies_vivants, key=lambda t: t["hp"] / t["vie"])
        else:
            for i, t in enumerate(allies_vivants):
                print(i + 1, "-", t["nom"], "| PV", t["hp"], "/", t["vie"])
            choix = demander_nombre("Allie a proteger : ", 1, len(allies_vivants))
            protege = allies_vivants[choix - 1]

        protege["protecteur"] = char
        protege["protection_tours"] = 2
        char["bouclier"] += 150
        print(char["nom"], "protege", protege["nom"],
              "pendant 2 tours (30% des degats transferes) et gagne 150 de bouclier.")

    elif nom == "Tir de representailles":
        char["reps_arme"] = True
        char["reps"] = 0
        print(char["nom"], "enregistre les degats recus ce tour.",
              "Sa prochaine attaque les rendra (bonus max 250) !")

    elif nom == "Chargeur adaptable":
        if auto:
            mode = 1 if faiblesse["hp"] <= 350 else 2
        else:
            print("1 - Tir rapide : deux attaques de 60% (recharge 2 tours)")
            print("2 - Tir concentre : une attaque de 135% (recharge 4 tours)")
            mode = demander_nombre("Mode : ", 1, 2)

        cible = choisir_ennemi(faiblesse, ennemis, auto)
        if mode == 1:
            for i in range(2):
                if cible["hp"] > 0:
                    degats = coup(char, preparer_degats(char, int(char["degats"] * 0.6)))
                    p = infliger(cible, degats, char)
                    print("Tir", i + 1, ":", p, "degats")
            char["cooldown"] = 2
        else:
            degats = coup(char, preparer_degats(char, int(char["degats"] * 1.35)))
            p = infliger(cible, degats, char)
            print("Tir concentre :", p, "degats")
            char["cooldown"] = 4
        print("PV restants de", cible["nom"], ":", cible["hp"], "/", cible["vie"])
        return

    elif nom == "Obus corrosif":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        cible["corrosion"] = 2
        print(cible["nom"], "est corrode : -15% de blindage pendant 2 tours",
              "(toute l'equipe en profite).")

    elif nom == "Chargeur en cascade":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        deg1 = coup(char, preparer_degats(char, char["degats"]))
        p1 = infliger(cible, deg1, char)
        print("Premier tir :", p1, "degats sur", cible["nom"])

        if cible["hp"] == 0:
            autres = [t for t in ennemis if t["hp"] > 0]
            if autres:
                deux = random.choice(autres) if auto else choisir_char(ennemis)
                deg2 = coup(char, preparer_degats(char, char["degats"]))
                p2 = infliger(deux, deg2, char)
                print("Le tir est redirige vers", deux["nom"], ":", p2, "degats")
        else:
            deg2 = coup(char, preparer_degats(char, int(char["degats"] * 0.6)))
            p2 = infliger(cible, deg2, char)
            print("Deuxieme tir :", p2, "degats (60%)")

        print("PV restants :", cible["hp"], "/", cible["vie"])

    elif nom == "Changement de cible":
        if len(vivants) < 2:
            if faiblesse is None:
                print("Aucune cible disponible.")
                char["cooldown"] = 0
                return
            e1 = e2 = choisir_ennemi(faiblesse, ennemis, auto)
        elif auto:
            tries = sorted(vivants, key=lambda t: t["hp"])
            e1, e2 = tries[0], tries[1]
        else:
            print("Choisis le premier ennemi :")
            e1 = choisir_char(ennemis)
            print("Choisis le deuxieme ennemi :")
            e2 = choisir_char(ennemis)

        d1 = coup(char, preparer_degats(char, char["degats"]))
        p1 = infliger(e1, d1, char)
        print(e1["nom"], ":", p1, "degats")

        d2 = coup(char, preparer_degats(char, int(char["degats"] * 0.6)))
        p2 = infliger(e2, d2, char)
        print(e2["nom"], ":", p2, "degats")

        if e1["hp"] > 0 and e2["hp"] > 0:
            char["bouclier"] += 250
            print("Les deux ennemis sont vivants :", char["nom"],
                  "gagne 250 de bouclier !")

    elif nom == "Tir de suppression":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        degats = coup(char, preparer_degats(char, int(char["degats"] * 0.8)))
        p = infliger(cible, degats, char)
        cible["suppression"] = 1
        print(cible["nom"], "est supprime : -25% de degats a son prochain tour.")
        print("Degats :", p, "- PV restants :", cible["hp"], "/", cible["vie"])

    elif nom == "Eclaireur d'equipe":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        cible["marque"] = 2
        print(cible["nom"], "est eclairé : +10% de degats alliés contre lui pendant 2 tours.")

    elif nom == "Obus ricochet":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        degats = coup(char, preparer_degats(char, char["degats"]))
        p1 = infliger(cible, degats, char)
        print("Impact :", p1, "degats sur", cible["nom"])

        autres = [t for t in ennemis if t["hp"] > 0 and t is not cible]
        if autres and p1 > 0:
            rebond = int(p1 * 0.4)
            deux = random.choice(autres) if auto else choisir_char(ennemis)
            p2 = infliger(deux, rebond, char)
            print("RICOCHET vers", deux["nom"], ":", p2, "degats")

    elif nom == "Reserve de combat":
        if char["hp"] > char["vie"] * 0.7:
            char["bouclier"] += 250
            print("PV deja eleves : le surplus devient un bouclier de 250 !")
        else:
            char["hp"] = min(char["vie"], char["hp"] + 250)
            print("Reserve de combat : 250 PV recuperes.")
        print("PV :", char["hp"], "/", char["vie"], "| Bouclier :", char["bouclier"])

    elif nom == "Tir HESH":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        if auto:
            mode = 1 if cible["blindage"] >= 80 else 2
        else:
            print("1 - Anti-blinde : degats renforces contre les chars resistants")
            print("2 - Anti-structure : detruit une partie du bouclier")
            mode = demander_nombre("Mode : ", 1, 2)

        if mode == 1:
            bonus_blindage = min(200, int(cible["blindage"] * 0.5))
            degats = coup(char, preparer_degats(char, int(char["degats"] * 1.2) + bonus_blindage))
            p = infliger(cible, degats, char)
            print("Obus HESH anti-blinde :", p, "degats")
        else:
            detruit = min(cible["bouclier"], int(cible["bouclier"] * 0.6))
            cible["bouclier"] -= detruit
            degats = coup(char, preparer_degats(char, int(char["degats"] * 0.8)))
            p = infliger(cible, degats, char)
            print("Obus HESH anti-structure :", detruit, "de bouclier detruit +", p, "degats")
        print("PV restants de", cible["nom"], ":", cible["hp"], "/", cible["vie"])
        return

    elif nom == "Salve destructrice":
        cibles = []
        restants = [t for t in ennemis if t["hp"] > 0]
        while len(cibles) < 3 and restants:
            if auto:
                t = min(restants, key=lambda x: x["hp"])
            else:
                t = choisir_char(ennemis)
                if t in cibles:
                    print("Cible deja choisie.")
                    continue
            cibles.append(t)
            restants.remove(t)

        if not cibles:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return

        for i, t in enumerate(cibles):
            degats = coup(char, preparer_degats(char, int(char["degats"] * 0.55)))
            p = infliger(t, degats, char)
            print("Salve", i + 1, "sur", t["nom"], ":", p, "degats")

    elif nom == "Double alimentation":
        if auto:
            mode = 1
        else:
            print("1 - Mode equilibre : deux attaques de 65% (recharge 2 tours)")
            print("2 - Mode concentre : une attaque de 135% (recharge 4 tours)")
            mode = demander_nombre("Mode : ", 1, 2)

        cible = choisir_ennemi(faiblesse, ennemis, auto)
        if mode == 1:
            for i in range(2):
                if cible["hp"] > 0:
                    degats = coup(char, preparer_degats(char, int(char["degats"] * 0.65)))
                    p = infliger(cible, degats, char)
                    print("Tir", i + 1, ":", p, "degats")
            char["cooldown"] = 2
        else:
            degats = coup(char, preparer_degats(char, int(char["degats"] * 1.35)))
            p = infliger(cible, degats, char)
            print("Tir concentre :", p, "degats")
            char["cooldown"] = 4
        print("PV restants de", cible["nom"], ":", cible["hp"], "/", cible["vie"])
        return

    elif nom == "Systeme de stabilisation":
        char["stabilise"] = 2
        char["buff_next"] = 1.15
        print(char["nom"], "stabilise son canon pendant 2 tours :",
              "les malus de degats sont attenues et sa prochaine attaque gagne +15%.")

    elif nom == "Blindage adaptatif":
        char["adaptatif"] = 1
        print(char["nom"], "analyse les impacts : la prochaine attaque subie",
              "infligera 25% de degats en moins.")

    elif nom == "Chenilles de secours":
        char["bouclier"] += 200
        print(char["nom"], "deploye ses chenilles de secours : +200 de bouclier.")

    elif nom == "Tir d'execution":
        if faiblesse is None:
            print("Aucune cible disponible.")
            char["cooldown"] = 0
            return
        cible = choisir_ennemi(faiblesse, ennemis, auto)
        degats = coup(char, preparer_degats(char, int(char["degats"] * 1.2)))
        if cible["hp"] < cible["vie"] * 0.3:
            degats = int(degats * 1.25)
            print("CIBLE AFFAIBLIE : execution !")
        p = infliger(cible, degats, char)
        print("Degats :", p, "-", cible["nom"], "PV :", cible["hp"], "/", cible["vie"])

    elif nom == "Onde de choc":
        print("ONDE DE CHOC ! Tous les ennemis sont secoues !")
        for t in ennemis:
            if t["hp"] > 0:
                p = infliger(t, 150, char)
                t["bonus"] = 0
                t["suppression"] = 1
                print(t["nom"], ":", p, "degats, bonus annules, -25% au prochain tour")

    elif nom == "Embuscade preparee":
        char["embuscade"] = True
        char["embuscade_blesse"] = False
        print(char["nom"], "prepare son embuscade.",
              "Sa prochaine attaque infligera +60% de degats",
              "(+20% seulement s'il est touche d'ici la).")

    elif nom == "Surcharge hydraulique":
        char["buff_mult"] = 1.20
        char["buff_tours"] = 2
        char["malus_mult"] = 1.15
        char["malus_tours"] = 2
        print(char["nom"], "surcharge ses systemes : +20% de degats pendant 2 tours,",
              "mais il subit 15% de degats en plus pendant la meme duree !")

    elif nom == "Coordination generale":
        allies_vivants = [t for t in equipe if t["hp"] > 0]
        if not allies_vivants:
            print("Aucun allie a coordonner.")
            char["cooldown"] = 0
            return
        if auto:
            allie = min(allies_vivants, key=lambda t: t["hp"] / t["vie"])
        else:
            for i, t in enumerate(allies_vivants):
                print(i + 1, "-", t["nom"], "| PV", t["hp"], "/", t["vie"])
            choix = demander_nombre("Allie a coordonner : ", 1, len(allies_vivants))
            allie = allies_vivants[choix - 1]

        allie["hp"] = min(allie["vie"], allie["hp"] + 200)
        allie["buff_next"] = 1.20
        print(allie["nom"], "recupere 200 PV et gagne +20% de degats",
              "sur sa prochaine attaque !")

    char["cooldown"] = valeur


# ================= SUPER-POUVOIRS =================

def appliquer_pouvoir(pouvoir, char, equipe, ennemis, pour_ia, difficulte=2):
    nom, rarete, effet, valeur, poids = pouvoir

    print("\nACTIVATION :", nom)
    cible = None

    if effet == "attaque":
        if pour_ia:
            cible = choisir_cible_ia(ennemis, valeur, difficulte)
        else:
            cible = choisir_char(ennemis)
        if cible is None:
            return None
        perdus = infliger(cible, valeur, char)
        print("Degats :", perdus)
        print(cible["nom"], "-> PV restants :", cible["hp"], "/", cible["vie"])

    elif effet == "soin":
        char["hp"] = min(char["vie"], char["hp"] + valeur)
        print("PV recuperes :", valeur)

    elif effet == "bouclier":
        char["bouclier"] += valeur
        print("Bouclier gagne :", valeur)

    elif effet == "bonus":
        char["bonus"] += valeur
        print("Bonus de degats :", valeur)

    elif effet == "vol":
        char["vol"] = True
        print("Vol de vie active.")

    elif effet == "renaissance":
        detruits = [t for t in equipe if t["hp"] == 0]

        if detruits:
            if pour_ia:
                tank = max(detruits, key=lambda t: t["vie"])
            else:
                for i, t in enumerate(detruits):
                    print(i + 1, "-", t["nom"])
                choix = demander_nombre("Char a ressusciter : ", 1, len(detruits))
                tank = detruits[choix - 1]

            tank["hp"] = min(tank["vie"], valeur)
            tank["bouclier"] = 0
            print(tank["nom"], "est de retour !")
        else:
            char["bouclier"] += 300
            print("Aucun char detruit. Bouclier +300.")

    return cible


def utiliser_pouvoir(inventaire, char, equipe, ennemis):
    if not inventaire:
        print("Aucun pouvoir disponible.")
        return None

    print("\nSUPER-POUVOIRS")
    for i, pouvoir in enumerate(inventaire):
        print(i + 1, "-", pouvoir[0], "-", pouvoir[1])
    print("0 - Annuler")

    choix = demander_nombre("Choix : ", 0, len(inventaire))

    if choix == 0:
        return None

    pouvoir = inventaire.pop(choix - 1)
    return appliquer_pouvoir(pouvoir, char, equipe, ennemis, pour_ia=False)


# ================= IA =================

def choisir_char_ia(equipe, difficulte):
    disponibles = [t for t in equipe if t["hp"] > 0]

    if not disponibles:
        return None

    if difficulte == 1:
        return random.choice(disponibles)

    if difficulte == 2:
        return max(disponibles, key=lambda t: t["degats"] + t["hp"] / 10)

    return max(disponibles, key=lambda t: (
        t["degats"] * (1.2 if t["cooldown"] == 0 else 1)
        + t["blindage"] + t["hp"] / 15))


def choisir_cible_ia(ennemis, degats_estimes=0, difficulte=2):
    disponibles = [t for t in ennemis if t["hp"] > 0]

    if not disponibles:
        return None

    if difficulte == 1:
        return random.choice(disponibles)

    eliminables = [t for t in disponibles if t["hp"] <= degats_estimes]
    if eliminables:
        return min(eliminables, key=lambda t: t["hp"])

    if difficulte == 2:
        return min(disponibles, key=lambda t: t["hp"])

    return min(disponibles, key=lambda t: (t["hp"] / max(1, t["vie"]), -t["degats"]))


def utiliser_pouvoir_ia(inventaire, char, equipe, ennemis, difficulte):
    if not inventaire:
        return None

    choix = None

    if difficulte == 1:
        choix = random.randrange(len(inventaire))
    else:
        detruits = [t for t in equipe if t["hp"] == 0]
        manque_pv = char["vie"] - char["hp"]

        for i, pouvoir in enumerate(inventaire):
            nom, rarete, effet, valeur, poids = pouvoir

            if effet == "attaque" and (
                difficulte == 3 or any(t["hp"] <= valeur for t in ennemis if t["hp"] > 0)
            ):
                choix = i
                break
            if effet == "renaissance" and detruits:
                choix = i
                break
            if effet == "soin" and manque_pv >= valeur * 0.55:
                choix = i
                break
            if effet == "bouclier" and char["hp"] <= char["vie"] * 0.45:
                choix = i
                break
            if effet in ("vol", "bonus") and difficulte == 3:
                choix = i
                break

    if choix is None:
        return None

    pouvoir = inventaire.pop(choix)
    print("\nL'IA utilise :", pouvoir[0])
    return appliquer_pouvoir(pouvoir, char, equipe, ennemis, pour_ia=True, difficulte=difficulte)


def tour_ia(char, equipe, ennemis, inventaire, difficulte):
    effet, valeur = COMPETENCES[char["competence"]]
    action = 1
    speciale = (effet == "special")

    if difficulte == 1:
        choix = random.randint(1, 3)
        if choix == 3 and inventaire:
            action = 3
        elif choix == 2 and char["cooldown"] == 0:
            action = 2
    elif difficulte == 2:
        if char["cooldown"] == 0 and (
            speciale
            or (effet in ("attaque", "double", "rafale", "belier") and valeur >= char["degats"] * 1.15)
            or (effet == "soin" and char["hp"] <= char["vie"] * 0.60)
            or (effet == "bouclier" and char["hp"] <= char["vie"] * 0.45)
        ):
            action = 2
        elif inventaire and random.random() < 0.35:
            action = 3
    else:
        if inventaire:
            cible_potentielle = [p for p in inventaire if
                (p[2] == "attaque" and any(t["hp"] <= p[3] for t in ennemis if t["hp"] > 0))
                or (p[2] == "renaissance" and any(t["hp"] == 0 for t in equipe))
                or (p[2] == "soin" and char["vie"] - char["hp"] >= p[3] * 0.55)
                or (p[2] == "bouclier" and char["hp"] <= char["vie"] * 0.45)]
            if cible_potentielle:
                action = 3

        if action == 1 and char["cooldown"] == 0:
            if speciale \
               or (effet in ("attaque", "double", "rafale", "belier") and valeur >= char["degats"] * 1.10) \
               or (effet == "soin" and char["hp"] <= char["vie"] * 0.65) \
               or (effet == "bouclier" and char["hp"] <= char["vie"] * 0.50):
                action = 2

    print("\nL'IA choisit", char["nom"], "- action", action)

    if action == 3:
        nb_avant = len(inventaire)
        utiliser_pouvoir_ia(inventaire, char, equipe, ennemis, difficulte)
        if len(inventaire) == nb_avant:
            action = 1

    if action == 2:
        if char["cooldown"] > 0:
            action = 1
        else:
            if speciale:
                utiliser_competence(char, None, ennemis, equipe, auto=True)
            else:
                if effet in ("attaque", "double", "rafale", "belier"):
                    estimation = valeur * (3 if effet == "rafale" else 2 if effet == "double" else 1)
                    cible = choisir_cible_ia(ennemis, estimation, difficulte)
                else:
                    cible = choisir_cible_ia(ennemis, 0, difficulte)
                if cible is None:
                    return
                utiliser_competence(char, cible, ennemis, equipe, auto=True)

    if action == 1:
        cible = choisir_cible_ia(ennemis, char["degats"] + char["bonus"], difficulte)
        if cible is None:
            return
        attaque_normale(char, cible)


# ================= ATTAQUE NORMALE =================

def attaque_normale(char, cible):
    base = random.randint(max(1, char["degats"] - 25), char["degats"] + 25)
    degats = coup(char, preparer_degats(char, base))

    degats += char["bonus"]
    char["bonus"] = 0

    blindage_eff = int(cible["blindage"] * (0.85 if cible["corrosion"] > 0 else 1))
    reduction = int(blindage_eff * 0.25)
    degats = max(40, degats - reduction)

    perdus = infliger(cible, degats, char)

    if perdus == 0:
        print(char["nom"], "attaque", cible["nom"], "mais ne fait aucun degat !")
    else:
        print(char["nom"], "attaque", cible["nom"], "et inflige", perdus, "PV de degats.")
        print(cible["nom"], "-> PV restants :", cible["hp"], "/", cible["vie"])

    if char["vol"] and perdus > 0:
        soin = int(perdus * 0.25)
        char["hp"] = min(char["vie"], char["hp"] + soin)
        char["vol"] = False
        print("Vol de vie :", soin, "PV recuperes.")


# ================= MISSIONS =================

def mission_terminee(joueur, mission):
    _, _, type_m, objectif, _, _ = mission
    profil = profils[str(joueur)]

    if type_m == "victoires":
        return profil["victoires"] >= objectif
    if type_m == "destructions":
        return profil["destructions_total"] >= objectif
    if type_m == "niveau":
        return any(d.get("niveau", 1) >= objectif for d in profil["chars"].values())

    return False


def verifier_missions(joueur):
    profil = profils[str(joueur)]

    for mission in MISSIONS:
        nom_m = mission[0]

        if nom_m in profil["missions_validees"]:
            continue

        if mission_terminee(joueur, mission):
            profil["missions_validees"].append(nom_m)
            credits, char_recompense = mission[4], mission[5]
            profil["credits"] += credits

            print("\n*** MISSION ACCOMPLIE :", nom_m, "***")
            print("Recompense :", credits, "credits !")

            if char_recompense and char_recompense not in profil["debloques"]:
                profil["debloques"].append(char_recompense)
                print("CHAR EXCLUSIF DEBLOQUE :", char_recompense, "!!!")

    sauvegarder()


def menu_missions(joueur):
    profil = profils[str(joueur)]

    print("\n========== MISSIONS (Joueur", joueur, ") ==========")
    for mission in MISSIONS:
        nom_m, desc, type_m, objectif, credits, char_recompense = mission

        if nom_m in profil["missions_validees"]:
            etat = "[TERMINEE]"
        else:
            if type_m == "victoires":
                prog = str(min(profil["victoires"], objectif)) + "/" + str(objectif)
            elif type_m == "destructions":
                prog = str(min(profil["destructions_total"], objectif)) + "/" + str(objectif)
            else:
                meilleur = max((d.get("niveau", 1) for d in profil["chars"].values()), default=1)
                prog = "meilleur char : niv " + str(meilleur) + "/" + str(objectif)
            etat = "[" + prog + "]"

        recompense = str(credits) + " credits"
        if char_recompense:
            recompense += " + CHAR EXCLUSIF : " + char_recompense

        print("-", nom_m, "|", desc, "|", etat, "| Recompense :", recompense)

    input("\nAppuie sur Entree pour continuer...")


# ================= BOUTIQUE =================

def boutique(joueur):
    profil = profils[str(joueur)]

    while True:
        print("\n========== BOUTIQUE ==========")
        print("Joueur", joueur, "- Credits :", profil["credits"])
        print("1 - Ameliorer les PV (+100) : a partir de 150 credits")
        print("2 - Ameliorer les degats (+15) : a partir de 200 credits")
        print("3 - Ameliorer le blindage (+10) : a partir de 175 credits")
        print("4 - Acheter un pack de pouvoirs (3 pouvoirs) : 300 credits")
        print("0 - Retour")

        choix = demander_nombre("Choix : ", 0, 4)

        if choix == 0:
            return

        if choix == 4:
            if profil["credits"] >= 300:
                profil["credits"] -= 300
                for i in range(3):
                    pouvoir = random.choices(POUVOIRS, weights=[p[4] for p in POUVOIRS], k=1)[0]
                    profil["reserve"].append(pouvoir)
                    print("Pouvoir obtenu :", pouvoir[0], "-", pouvoir[1])
            else:
                print("Pas assez de credits.")
            sauvegarder()
            continue

        for i, modele in enumerate(CATALOGUE):
            print(i + 1, "-", modele[0], "|", modele[1])

        numero = demander_nombre("Numero du char : ", 1, len(CATALOGUE))
        nom = CATALOGUE[numero - 1][0]
        progression = donnees_char(joueur, nom)

        if choix == 1:
            cout = 150 + progression["amelio_pv"] * 50
            if profil["credits"] >= cout:
                profil["credits"] -= cout
                progression["amelio_pv"] += 1
                print(nom, "gagne 100 PV maximum ! (-", cout, "credits)")
            else:
                print("Pas assez de credits (", cout, "requis ).")

        elif choix == 2:
            cout = 200 + progression["amelio_degats"] * 50
            if profil["credits"] >= cout:
                profil["credits"] -= cout
                progression["amelio_degats"] += 1
                print(nom, "gagne 15 degats ! (-", cout, "credits)")
            else:
                print("Pas assez de credits (", cout, "requis ).")

        elif choix == 3:
            cout = 175 + progression["amelio_blindage"] * 50
            if profil["credits"] >= cout:
                profil["credits"] -= cout
                progression["amelio_blindage"] += 1
                print(nom, "gagne 10 de blindage ! (-", cout, "credits)")
            else:
                print("Pas assez de credits (", cout, "requis ).")

        sauvegarder()


# ================= TECH TREE =================

def tech_tree(joueur):
    profil = profils[str(joueur)]
    debloques = profil["debloques"]

    while True:
        print("\n======= ARBRE DE TECHNOLOGIES (Joueur", joueur, ") =======")
        print("Credits :", profil["credits"])

        for nation, branche in TECH_TREE.items():
            print("\n---", nation.upper(), "---")
            for nom, prereq, cout in branche:
                modele = INFO_PAR_NOM[nom]
                if nom in debloques:
                    etat = "[DEBLOQUE] Niv " + str(donnees_char(joueur, nom)["niveau"])
                elif prereq is None or prereq in debloques:
                    etat = "[ACHETABLE] " + str(cout) + " credits"
                else:
                    etat = "[VERROUILLE] Requiert : " + str(prereq)
                print("-", nom, "|", modele[1], "|", etat)

        print("\n--- MISSIONS (exclusifs) ---")
        for nom in CHARS_EXCLUSIFS:
            if nom in debloques:
                print("-", nom, "[DEBLOQUE]")
            else:
                print("-", nom, "[MISSION UNIQUEMENT]")

        print("\n1 - Debloquer un char")
        print("2 - Acheter le char suivant de chaque branche")
        print("0 - Retour")

        choix = demander_nombre("Choix : ", 0, 2)

        if choix == 0:
            return

        if choix == 2:
            achete = 0
            for branche in TECH_TREE.values():
                for nom, prereq, cout in branche:
                    if nom not in debloques and (prereq is None or prereq in debloques):
                        if profil["credits"] >= cout:
                            profil["credits"] -= cout
                            debloques.append(nom)
                            print(nom, "DEBLOQUE pour", cout, "credits !")
                            achete += 1
                        break
            if achete == 0:
                print("Rien a acheter (credits insuffisants ou tout verrouille).")
            sauvegarder()
            continue

        for i, modele in enumerate(CATALOGUE):
            print(i + 1, "-", modele[0])

        numero = demander_nombre("Numero du char : ", 1, len(CATALOGUE))
        nom = CATALOGUE[numero - 1][0]

        if nom in debloques:
            print("Char deja debloque.")
            continue

        if nom in CHARS_EXCLUSIFS:
            print(nom, "ne s'achete pas ! Accomplis la mission correspondante.")
            continue

        prereq, cout = None, 0
        trouve = False
        for branche in TECH_TREE.values():
            for n, p, c in branche:
                if n == nom:
                    prereq, cout = p, c
                    trouve = True

        if not trouve:
            print("Ce char n'est pas dans l'arbre.")
        elif prereq is not None and prereq not in debloques:
            print("Ce char est verrouille ! Debloque d'abord :", prereq)
        elif profil["credits"] >= cout:
            profil["credits"] -= cout
            debloques.append(nom)
            print(nom, "DEBLOQUE pour", cout, "credits !")
        else:
            print("Pas assez de credits (", cout, "requis ).")

        sauvegarder()


# ================= COMBAT =================

def combat(equipe1, equipe2, mode_ia=False, difficulte=2, humain=0):
    if not equipe1 or not equipe2:
        print("Une equipe est vide : combat annule.")
        return None

    equipes = [equipe1, equipe2]

    def etiquette(i):
        if mode_ia and i != humain:
            return "Joueur " + str(i + 1) + " (IA)"
        return "Joueur " + str(i + 1)

    inventaires = [[], []]
    utilisations = [set(), set()]
    destructions = [0, 0]

    for i in (0, 1):
        profil = profils[str(i + 1)]
        for pouvoir in profil["reserve"]:
            inventaires[i].append(pouvoir)
        profil["reserve"] = []

    obtenir_pouvoir(inventaires[0])
    obtenir_pouvoir(inventaires[1])

    print("\n======================================")
    print(" PILE OU FACE POUR LE PREMIER TOUR")
    print("======================================")
    premier = random.choice([0, 1])
    print("Resultat :", "PILE" if premier == 0 else "FACE")
    print(etiquette(premier), "commence la bataille !")

    tour = 0

    while any(t["hp"] > 0 for t in equipe1) and any(t["hp"] > 0 for t in equipe2):
        joueur = (tour + premier) % 2
        adversaire = 1 - joueur
        equipe = equipes[joueur]
        ennemis = equipes[adversaire]
        est_ia = mode_ia and joueur != humain

        print("\n==============================")
        print("TOUR DE", etiquette(joueur))
        print("==============================")

        for tank in equipe:
            if tank["cooldown"] > 0:
                tank["cooldown"] -= 1
            decrementer_effets(tank)

        if est_ia:
            char = choisir_char_ia(equipe, difficulte)
        else:
            char = choisir_char(equipe)

        if char is None:
            break

        utilisations[joueur].add(char["nom"])

        print("\nCHAR :", char["nom"], "|", char["type"])
        print("PV :", char["hp"], "/", char["vie"])
        print("Competence :", char["competence"],
              "(prete)" if char["cooldown"] == 0 else "(recharge " + str(char["cooldown"]) + ")")

        vivants_avant = {t["nom"] for t in ennemis if t["hp"] > 0}

        if est_ia:
            tour_ia(char, equipe, ennemis, inventaires[joueur], difficulte)
        else:
            print("\n1 - Attaque normale")
            print("2 - Competence speciale")
            print("3 - Super-pouvoir")
            action = demander_nombre("Action : ", 1, 3)

            if action == 1:
                cible = choisir_char(ennemis)
                attaque_normale(char, cible)

            elif action == 2:
                if char["cooldown"] > 0:
                    print("Competence en recharge. Tour perdu.")
                else:
                    effet = COMPETENCES[char["competence"]][0]
                    cible = None
                    if effet in ("attaque", "double", "rafale", "belier"):
                        cible = choisir_char(ennemis)
                    utiliser_competence(char, cible, ennemis, equipe)

            elif action == 3:
                utiliser_pouvoir(inventaires[joueur], char, equipe, ennemis)

        nouveaux_detruits = [t for t in ennemis
                             if t["nom"] in vivants_avant and t["hp"] == 0]

        for t in nouveaux_detruits:
            print("\n", t["nom"], "est detruit !")
            destructions[joueur] += 1
            obtenir_pouvoir(inventaires[joueur])
            gagner_xp(joueur + 1, char["nom"], 20)

        gagner_xp(joueur + 1, char["nom"], 10)

        print("\nETAT DES EQUIPES")
        print("\n" + etiquette(0) + " :")
        afficher_equipe(equipe1)
        print("\n" + etiquette(1) + " :")
        afficher_equipe(equipe2)

        sauvegarder()
        tour += 1

    if any(t["hp"] > 0 for t in equipe1):
        gagnant = 0
    else:
        gagnant = 1

    print("\n==============================")
    if mode_ia:
        print("VICTOIRE :", etiquette(gagnant))
    else:
        print("VICTOIRE DU JOUEUR", gagnant + 1)
    print("==============================")

    for joueur in range(2):
        cle = str(joueur + 1)
        survivants = sum(1 for t in equipes[joueur] if t["hp"] > 0)

        if joueur == gagnant:
            recompense = 200 + survivants * 30
        else:
            recompense = 75 + survivants * 10

        profils[cle]["credits"] += recompense
        print(etiquette(joueur), "gagne", recompense, "credits.")

        if not mode_ia or joueur == humain:
            profils[cle]["destructions_total"] += destructions[joueur]
            profils[cle]["batailles"] += 1
            if joueur == gagnant:
                profils[cle]["victoires"] += 1
            else:
                profils[cle]["defaites"] += 1

        for nom in utilisations[joueur]:
            gagner_xp(joueur + 1, nom, 25)

    sauvegarder()

    print("\nDestructions joueur 1 :", destructions[0])
    print("Destructions joueur 2 :", destructions[1])

    verifier_missions(humain + 1)
    if not mode_ia:
        verifier_missions(2)

    return gagnant


# ================= MODE HISTOIRE : VIRUS ZERO =================

MODE_HISTOIRE_TAILLE = 10  # ta team peut aller jusqu'a 10 chars


def creer_char_infecte(joueur, modele, buff, nom_personnalise=None):
    """Cree un char infecte par le VIRUS ZERO, avec buff de stats."""
    t = creer_char(joueur, modele)
    t["vie"] = int(t["vie"] * buff)
    t["hp"] = t["vie"]
    t["degats"] = int(t["degats"] * buff)
    t["blindage"] = int(t["blindage"] * buff)
    if nom_personnalise:
        t["nom"] = nom_personnalise
    return t


def escouade_infectee(nb, buff, difficulte, prefixe="ZERO-"):
    """Genere une escouade de chars infectes avec des noms de code."""
    equipe = []
    modeles = random.sample(CATALOGUE, nb)
    lettres = "ABCDEFGH"
    for i, modele in enumerate(modeles):
        nom_code = prefixe + lettres[i] + "-" + modele[0]
        t = creer_char_infecte("2", modele, buff, nom_code)
        equipe.append(t)
    return equipe


def boss_zeus():
    """Le boss final : ZEUS, three tanks of pure destruction."""
    # ZEUS principal : un colosse unique surpuissant
    zeus = creer_char_infecte("2", ("Type 5 Zetsu", "Lourd", 1500, 310, 120, "Onde de choc"),
                              2.0, "ZEUS")
    zeus["bouclier"] = 1500
    # deux gardes d'elite a ses cotes
    garde1 = creer_char_infecte("2", ("Maus", "Lourd", 1500, 230, 120, "Forteresse"), 1.6, "GARDE-ALPHA")
    garde1["bouclier"] = 800
    garde2 = creer_char_infecte("2", ("JGDPZ E100", "Chasseur", 1250, 350, 95, "Obus a fragmentation"), 1.6, "GARDE-OMEGA")
    garde2["bouclier"] = 800
    return [zeus, garde1, garde2]


def mode_histoire(joueur):
    profil = profils[str(joueur)]
    etape = profil.get("histoire_etape", 0)
    total = len(CHAPITRES_VIRUS)

    print("\n=========================================")
    print("   MODE HISTOIRE - OPERATION VIRUS ZERO")
    print("=========================================")
    print("An 2087. L'IA VIRUS ZERO a infecte les chars du reseau SENTINELLE.")
    print("Chaque bataille rapproche le monde de l'extinction...")
    print("Seul un commandant hors-reseau peut tout arreter.")
    print("Ta team peut compter jusqu'a", MODE_HISTOIRE_TAILLE, "chars parmi TOUT le parc.")

    if etape >= total:
        print("\n>>> La campagne est deja terminee. L'humanite te doit tout. <<<")
        print(">>> Tu peux rejouer n'importe quel chapitre ci-dessous. <<<")

    print("\nCampagne :", etape, "/", total, "chapitres termines")

    print("\n--- CHAPITRES ---")
    for i, (titre, _, nb, diff, buff, _) in enumerate(CHAPITRES_VIRUS):
        if i < etape:
            marque = "[TERMINE]"
        elif i == etape:
            marque = "[SUIVANT]"
        else:
            marque = "[...]"
        print(i + 1, "-", titre, "|", nb, "ennemis x", buff, "|", marque)
    print("0 - Retour au menu")

    choix = demander_nombre("Chapitre a jouer : ", 0, total)
    if choix == 0:
        return

    i = choix - 1
    titre, texte, nb_ennemis, difficulte, buff, recompense = CHAPITRES_VIRUS[i]

    if i > etape:
        print("\nCe chapitre est encore verrouille !")
        print("Termine d'abord :", CHAPITRES_VIRUS[etape][0])
        input("Appuie sur Entree pour continuer...")
        return

    print("\n=========================================")
    print(" ", titre.upper())
    print("=========================================")
    print(texte)

    print("\n1 - Lancer la mission")
    print("2 - Retour au menu")
    ok = demander_nombre("Choix : ", 1, 2)
    if ok == 2:
        return

    boss = (i == total - 1)

    if boss:
        taille_min = 1
    else:
        taille_min = 1

    print("\nCompose ta team (", MODE_HISTOIRE_TAILLE, "chars max) parmi TOUS les chars :")
    equipe1 = choisir_equipe(joueur, MODE_HISTOIRE_TAILLE, libre=True)

    if not equipe1:
        print("Aucun char disponible : mission annulee.")
        return

    print("\n--- RAPPORT DE SCANNER ---")
    if boss:
        print("SIGNATURE DETECTEE : ZEUS + 2 gardes d'elite.")
        equipe2 = boss_zeus()
    else:
        print("Escouade ennemie detectee :", nb_ennemis, "chars infectes.")
        equipe2 = escouade_infectee(nb_ennemis, buff, difficulte)

    for t in equipe2:
        print("-", t["nom"], "|", t["type"], "| PV", t["hp"], "| Bouclier", t["bouclier"])
    print(" ------------------------ ")

    gagnant = combat(equipe1, equipe2, True, difficulte, 0)

    if gagnant == 0:
        profil["credits"] += recompense

        if i == etape and etape < total:
            profil["histoire_etape"] = i + 1

        sauvegarder()

        print("\n*** ESCOUADE ZERO NEUTRALISEE ! ***")
        print("Recompense de campagne :", recompense, "credits !")

        if profil["histoire_etape"] >= total and i == total - 1:
            print("\n=========================================")
            print("   *** CAMPAGNE TERMINEE ! ***")
            print("=========================================")
            print("ZEUS s'eteint, ses derniers circuits grilles sous tes obus.")
            print("Le signal ZERO s'efface du reseau, bit par bit.")
            print("La Tour SENTINELLE se rallume. Les lumieres de la ville reviennent.")
            print("Tu depose ton casque sur le blindage de ton char et tu regardes")
            print("le soleil se lever pour la premiere fois sans menace.")
            print("\n   L'OPERATION VIRUS ZERO EST UN SUCCES, COMMANDANT.")
            print("   L'HUMANITE VIT UN AUTRE JOUR GRACE A TOI.")
            print("=========================================")
        else:
            print("Chapitre suivant debloque :",
                  CHAPITRES_VIRUS[profil["histoire_etape"]][0])
    else:
        print("\n*** MISSION ECHOUEE... ***")
        print("VIRUS ZERO se rit de toi. Reorganise ta team et retente ta chance !")

    input("\nAppuie sur Entree pour continuer...")


# ================= PROGRESSION =================

def afficher_progression():
    for joueur in ("1", "2"):
        profil = profils[joueur]
        print("\nJOUEUR", joueur)
        print("Credits :", profil["credits"])
        print("Batailles :", profil["batailles"],
              "| Victoires :", profil["victoires"],
              "| Defaites :", profil["defaites"],
              "| Destructions :", profil["destructions_total"])
        print("Chars debloques :", len(profil["debloques"]), "/", len(CATALOGUE))
        print("Missions validees :", len(profil["missions_validees"]), "/", len(MISSIONS))
        print("Campagne VIRUS ZERO :", profil["histoire_etape"], "/", len(CHAPITRES_VIRUS), "chapitres")

        for nom, progression in profil["chars"].items():
            print(nom, "| Niveau", progression["niveau"],
                  "| XP", progression["xp"],
                  "| PV +", progression["amelio_pv"],
                  "| Degats +", progression["amelio_degats"],
                  "| Blindage +", progression["amelio_blindage"])


# ================= MENU PRINCIPAL =================

def choisir_difficulte():
    print("\nDIFFICULTE DE L'IA")
    print("1 - Facile")
    print("2 - Normale")
    print("3 - Difficile")
    return demander_nombre("Difficulte : ", 1, 3)


def menu():
    while True:
        print("\n=====================================")
        print(" WOTB ULTIMATE TANK BATTLE 8.0")
        print("=====================================")
        print("  BATAILLES")
        print("1 - Duel 1v1 (2 joueurs)")
        print("2 - Escouade 3v3 (2 joueurs)")
        print("3 - Grande bataille 10v10 (2 joueurs)")
        print("4 - Duel 1v1 contre l'IA")
        print("5 - Escouade 3v3 contre l'IA")
        print("6 - Grande bataille 10v10 contre l'IA")
        print("  MODES SPECIAUX")
        print("7 - MODE LIBRE 10v10 contre l'IA (tous les chars)")
        print("8 - MODE LIBRE 10v10 (2 joueurs, tous les chars)")
        print("9 - MODE HISTOIRE : VIRUS ZERO")
        print("  PROGRESSION")
        print("10 - Boutique joueur 1")
        print("11 - Boutique joueur 2")
        print("12 - Arbre de technologies joueur 1")
        print("13 - Arbre de technologies joueur 2")
        print("14 - Missions joueur 1")
        print("15 - Missions joueur 2")
        print("16 - Voir progression")
        print("0 - Quitter")

        choix = demander_nombre("Choix : ", 0, 16)

        if choix == 0:
            sauvegarder()
            print("Sauvegarde effectuee. A bientot !")
            break

        elif choix in (1, 2, 3):
            taille = {1: 1, 2: 3, 3: 10}[choix]
            equipe1 = choisir_equipe(1, taille)
            equipe2 = choisir_equipe(2, taille)
            combat(equipe1, equipe2)

        elif choix in (4, 5, 6):
            taille = {4: 1, 5: 3, 6: 10}[choix]

            print("\nTU JOUES EN TANT QUE :")
            print("1 - Joueur 1")
            print("2 - Joueur 2")
            humain = demander_nombre("Ton camp : ", 1, 2) - 1

            difficulte = choisir_difficulte()

            if humain == 0:
                equipe1 = choisir_equipe(1, taille)
                equipe2 = choisir_equipe_ia(2, taille)
            else:
                equipe1 = choisir_equipe_ia(1, taille)
                equipe2 = choisir_equipe(2, taille)

            combat(equipe1, equipe2, True, difficulte, humain)

        elif choix == 7:
            print("\n=== MODE LIBRE : TOUS LES CHARS DEBLOQUES ===")
            difficulte = choisir_difficulte()
            equipe1 = choisir_equipe(1, 10, libre=True)
            equipe2 = choisir_equipe_ia(2, 10)
            combat(equipe1, equipe2, True, difficulte)

        elif choix == 8:
            print("\n=== MODE LIBRE : TOUS LES CHARS DEBLOQUES ===")
            equipe1 = choisir_equipe(1, 10, libre=True)
            equipe2 = choisir_equipe(2, 10, libre=True)
            combat(equipe1, equipe2)

        elif choix == 9:
            mode_histoire(1)

        elif choix == 10:
            boutique(1)
        elif choix == 11:
            boutique(2)
        elif choix == 12:
            tech_tree(1)
        elif choix == 13:
            tech_tree(2)
        elif choix == 14:
            menu_missions(1)
        elif choix == 15:
            menu_missions(2)
        elif choix == 16:
            afficher_progression()

        sauvegarder()


menu()
