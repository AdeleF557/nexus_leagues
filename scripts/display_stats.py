from generate_player import generer_tous_les_joueurs
from statistics import mean

# --------------------------------------
# Fonction pour calculer la valeur moyenne par poste
# --------------------------------------
def valeur_moyenne_par_poste(joueurs):
    salaires = {}

    for joueur in joueurs:
        poste = joueur["poste"]
        valeur = joueur["valeur_marchande"]

        if poste not in salaires:
            salaires[poste] = []

        salaires[poste].append(valeur)

    # Calcul de la moyenne par poste
    moyenne = {}
    for poste, valeurs in salaires.items():
        moyenne[poste] = mean(valeurs)

    return moyenne

# --------------------------------------
# Fonction pour récupérer les N joueurs les plus chers
# --------------------------------------
def top_n_joueurs(joueurs, n):
    top = sorted(
        joueurs,
        key=lambda j: j["valeur_marchande"],
        reverse=True
    )[:n]

    return top

# --------------------------------------
# Fonction pour lister les joueurs par club
# --------------------------------------
def joueurs_par_club(joueurs):
    clubs = {}

    for joueur in joueurs:
        club = joueur["club"]

        if club not in clubs:
            clubs[club] = []  # création d'une liste vide pour le club

        # ajout du joueur à la liste du club
        clubs[club].append(f"{joueur['prenom']} {joueur['nom']} ({joueur['poste']})")

    return clubs

# --------------------------------------
# Test rapide si on exécute directement le fichier
# --------------------------------------
if __name__ == "__main__":
    joueurs = generer_tous_les_joueurs()

    print("\n--- Valeur moyenne par poste ---")
    stats = valeur_moyenne_par_poste(joueurs)
    for poste, val in stats.items():
        print(poste, ":", val)

    print("\n--- Top 5 joueurs ---")
    top5 = top_n_joueurs(joueurs, 5)
    for i, joueur in enumerate(top5, start=1):
        print(f"{i}. {joueur['prenom']} {joueur['nom']} | {joueur['club']} | {joueur['poste']} | {joueur['valeur_marchande']}")

    print("\n--- Joueurs par club ---")
    clubs = joueurs_par_club(joueurs)
    for club, liste_joueurs in clubs.items():
        print(f"\n{club}:")
        for joueur in liste_joueurs:
            print(" -", joueur)