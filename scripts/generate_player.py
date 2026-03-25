import random
from generate_clubs import ma_liste_dict

prenoms_fictifs = [
    "Kael", "Nerio", "Sylan", "Ivo", "Marek",
    "Timo", "Elio", "Rayan", "Nolan", "Yanis",
    "Sacha", "Milo", "Lior", "Zayn", "Aksel"
]

noms_fictifs = [
    "Vardek", "Solari", "Nexon", "Draven", "Koric",
    "Belmond", "Aster", "Caldor", "Novak", "Rivaan",
    "Torin", "Velas", "Orsen", "Darik", "Zenko"
]


def generer_joueur(id, nom_club, poste) -> dict:
    return {
        "id": id,
        "nom": random.choice(noms_fictifs),
        "prenom": random.choice(prenoms_fictifs),
        "age": random.randint(18, 35),
        "valeur_marchande": random.randint(1_000_000, 10_000_000),
        "poste": poste,
        "club": nom_club
    }


def generer_equipe(nom_club) -> list:

    repartition = {
        "gardien": 2,
        "défenseur": 6,
        "milieu": 8,
        "attaquant": 6
    }

    equipe = []
    id_joueur = 1

    for poste, quantite in repartition.items():
        for _ in range(quantite):
            joueur = generer_joueur(id_joueur, nom_club, poste)
            equipe.append(joueur)
            id_joueur += 1

    return equipe


def generer_tous_les_joueurs():

    tous_les_joueurs = []

    for club in ma_liste_dict:
        nom_club = club["nom"]
        equipe = generer_equipe(nom_club)
        tous_les_joueurs.extend(equipe)

    return tous_les_joueurs


if __name__ == "__main__":

    joueurs = generer_tous_les_joueurs()

    top_3 = sorted(
        joueurs,
        key=lambda j: j["valeur_marchande"],
        reverse=True
    )[:3]

    print("Top 3 des joueurs les plus chers :")

    for i, joueur in enumerate(top_3, start=1):

        print(
            f"{i}. {joueur['prenom']} {joueur['nom']} | "
            f"{joueur['club']} | {joueur['poste']} | "
            f"{joueur['valeur_marchande']}"
        )

        