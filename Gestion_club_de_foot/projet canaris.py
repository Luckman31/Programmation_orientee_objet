import random
# -*- coding: utf-8 -*-
#### REPRESENTATION DES DONNEES

# Initialisation des grilles et autres variables de jeu
def creer_grille(taille):
    grille = []
    for i in range(taille):
        ligne = []
        for j in range(taille):
            ligne.append('_')       #On initie chaque case de la grille selon la taille saisie avec des "_"
        grille.append(ligne)
    return grille




# Fonction pour afficher la grille
def afficher_grille(grille):
    print("  ", end="")
    for i in range(len(grille)):
        print(chr(65 + i), end=" ") #Code ASCII des lettres
    print()  # Nouvelle ligne après l'affichage des lettres

    for i in range(len(grille)):
        print(str(i + 1) + "|", end="")
        for j in range(len(grille[i])):
            print(grille[i][j], end="|")
        print()  # Nouvelle ligne après l'affichage de chaque ligne de la grille
    print()  # Nouvelle ligne à la fin de l'affichage de la grille


def pion_joueur1():
    return "O"
def pion_joueur2():
    return "X"



def creer_grille_debut(grille):
    grille_debut=grille
    for i in range(0,len(grille_debut)):
        for j in range(0,len(grille_debut[i])):
            if i==0 or i==1:    #On initialise les pions du joueur 1 sur les 2 premières lignes
                grille_debut[i][j]=pion_joueur1()
            elif i==len(grille_debut)-2 or i==len(grille_debut)-1:  #On initialise les pions du joueur 2 sur les 2 dernières lignes
                grille_debut[i][j]=pion_joueur2()
    return grille_debut

def creer_grille_milieu(grille):
    grille_milieu=grille
    grille_milieu[2][0]=pion_joueur1()
    grille_milieu[0][1]=pion_joueur2()
    grille_milieu[0][3]=pion_joueur2()
    grille_milieu[2][2]=pion_joueur1()
    grille_milieu[1][0]=pion_joueur1()
    grille_milieu[1][1]=pion_joueur2()
    grille_milieu[3][2]=pion_joueur1()
    grille_milieu[1][3]=pion_joueur2()
    grille_milieu[3][0]=pion_joueur2()


    return grille_milieu
def creer_grille_fin(grille):
    grille_fin=grille
    grille_fin[2][0]=pion_joueur2()
    grille_fin[1][0]=pion_joueur1()
    grille_fin[3][0]=pion_joueur1()
    grille_fin[2][2]=pion_joueur1()
    grille_fin[2][1]=pion_joueur1()
    grille_fin[2][3]=pion_joueur2()
    grille_fin[3][3]=pion_joueur2()



    return grille_fin
#### SAISIE
# Fonction de vérification dans la grille
def est_dans_grille(ligne, colonne, grille):
    if ligne <= 0 or colonne < 'A':#verifier que les valeurs écrites ne soit pas inférieures a 0 et pas inferieur a A
        return False
    if ligne > len(grille) or ord(colonne) - ord('A') >= len(grille[0]):#verifie que les valeurs écrites ne soit pas superieure a la taille de la grille et que la difference entre le code ASCII de la colonne saisie soit bien superieur à 0 mais pas superieur à la taille de la grille
        return False
    return True



def test_est_dans_grille():
    assert est_dans_grille(5,"A",grille)==False
    assert est_dans_grille(2,"A",grille)==True
    assert est_dans_grille(3,"D",grille)==True
    assert est_dans_grille(1,"A",grille)==True
    assert est_dans_grille(0,"B",grille)==False



# Fonction de vérification du format de saisie
def est_au_bon_format(message):
    if len(message) != 2: #verifier que seulement 2 valeurs sont saisies
        return False
    colonne, ligne = message[0], message[1]
    if not ('A' <= colonne <= 'Z'): #verifier que la première valeur soit bien comprise entre A et Z sinon on retourne False
        return False
    if not ('1' <= ligne <= '9'): #verifier que la deuxième valeur soit bien comprise entre 1 et 9 sinon on retourne False
        return False
    return True




def saisir_coordonnees(grille):
    # Initialisation de coordonnees_valides à True pour entrer dans la boucle
    coordonnees_valides = True

    # Tant que les coordonnées ne sont pas valides
    while coordonnees_valides:
        # Demande à l'utilisateur de saisir les coordonnées
        coordonnees = input("Entrez les coordonnées (colonne-ligne) : ")

        # Vérifie si les coordonnées sont au bon format (lettres-chiffres)
        if est_au_bon_format(coordonnees):
            colonne, ligne = coordonnees[0], coordonnees[1]

            # Vérifie si les coordonnées sont à l'intérieur de la grille
            if not ('A' <= colonne <= chr(ord('A') + len(grille[0]) - 1) and '1' <= ligne <= chr(ord('1') + len(grille) - 1)):
                print("Les coordonnées sont hors de la grille.")
            else:
                # Si les coordonnées sont valides, met coordonnees_valides à False pour sortir de la boucle
                coordonnees_valides = False
        else:
            print("Les coordonnées doivent être de la forme colonne-ligne et être compris dans la grille.")

    # Retourne les coordonnées valides
    return coordonnees



#### REPRESENTATION DES DONNEES
# Initialisation des grilles et autres variables de jeu
taille=4
grille=creer_grille(taille)
grille_debut = creer_grille_debut(creer_grille(taille))
grille_milieu = creer_grille_milieu(creer_grille(taille))
grille_fin = creer_grille_fin(creer_grille(taille))

#### CODE PRINCIPAL
# Affichage sur les 3 grilles
print("Grille de début:")
afficher_grille(grille_debut)

#On choisit au hasard qui commence
Quicommence=random.randint(1,2)
if Quicommence==1:
    print("Le joueur avec les pions O commence")
elif Quicommence==2:
    print("Le joueur avec les pions X commence")



print("Grille de milieu:")
afficher_grille(grille_milieu)
print("C'est au tour du joueur 1 ("+pion_joueur1()+") de jouer")




print("Grille de fin:")
afficher_grille(grille_fin)
print("C'est au tour du joueur 1("+pion_joueur1()+") de jouer")


# Exécution des tests
test_est_dans_grille()



#affichage des coordonnees saisies
print(saisir_coordonnees(grille))
print(saisir_coordonnees(grille))

