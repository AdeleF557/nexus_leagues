ma_liste_dict = [
    {
        "nom":"club1",
        "ville":"ville1",
        "stade":"stade1",
        "budget":1000000,
        "annee_fondation":1900
    },
    {
        "nom":"club2",
        "ville":"ville2",
        "stade":"stade2",
        "budget":2000000,
        "annee_fondation":1901
    },
    {
        "nom":"club3",
        "ville":"ville3",
        "stade":"stade3",
        "budget":3000000,
        "annee_fondation":1902
    },
    {
        "nom":"club4",
        "ville":"ville4",
        "stade":"stade4",
        "budget":4000000,
        "annee_fondation":1903
    },
    {
        "nom":"club5",
        "ville":"ville5",
        "stade":"stade5",
        "budget":5000000,
        "annee_fondation":1904
    },
    {
        "nom":"club6",
        "ville":"ville6",
        "stade":"stade6",
        "budget":6000000,
        "annee_fondation":1905
    },
    {
        "nom":"club7",
        "ville":"ville7",
        "stade":"stade7",
        "budget":7000000,
        "annee_fondation":1906
    },
    {
        "nom":"club8",
        "ville":"ville8",
        "stade":"stade8",
        "budget":8000000,
        "annee_fondation":1907
    }
]

#fonction pour afficher les informations d'un club
def affiche_club(club):
    return (
        f"Nom du club est {club['nom']}\n"
        f"Ville du club est {club['ville']}\n"
        f"Stade du club est {club['stade']}\n"
        f"Budget du club est {club['budget']}\n"
        f"Annee de fondation du club est {club['annee_fondation']}"
    )

## fonction  trouver club par nom
def trouver_club_par_nom(nom_club,ma_liste_dict):
    for club in ma_liste_dict:
        if club['nom'] == nom_club:
            return affiche_club(club)
    return "ce club n'existe pas dans la liste "


    ## appel de mes fonctions 
if __name__== "__main__":
    # affichage des  8 clubs
    for club in ma_liste_dict:
        print(affiche_club(club))
    # affichage du club 1
    print(trouver_club_par_nom("club1",ma_liste_dict))  
## il est important de mettre le if __name__ == "__main__" pour que le code soit executer seulement si le fichier est executer directement et non pas si il est importe dans un autre fichier