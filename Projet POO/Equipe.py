import random
import Joueur
print(Joueur.joueur1)
class Equipe:
    def __init__(self,nomclub):
        self.nomclub=nomclub

    def joueurdansequipe(self):
        nombrejoueurclub=0
        self.listedejoueur=[]
        for i in range(1,5):
            self.nombrechoisi=[]
            print(self.nombrechoisi)
            if nombrejoueurclub<5:

                self.joueurajoute=int(input("Choisissez un nombre entre 1 et 25 pour ajouter le joueur correspondant au numéro du joueur dans le club : "+self.nomclub))
                while self.joueurajoute>25:
                    self.joueurajoute=int(input("Choisissez uniquement un nombre entre 1 et 25 pour ajouter le joueur correspondant au numéro du joueur dans le club : "+self.nomclub))


                if self.joueurajoute in self.nombrechoisi:
                        joueurajoute=int(input("Vous avez déjà choisi se nombre choisissez en un différent entre 1 et 25 dans le club : "+self.nomclub))
                elif self.joueurajoute==1:
                    self.listedejoueur.append(str(Joueur.joueur1))
                    self.nombrechoisi.append(self.joueurajoute)
                elif self.joueurajoute==2:
                    self.listedejoueur.append(str(Joueur.joueur2))
                    self.nombrechoisi.append(self.joueurajoute)
                elif self.joueurajoute==3:
                    self.listedejoueur.append(str(Joueur.joueur3))
                    self.nombrechoisi.append(self.joueurajoute)
                elif self.joueurajoute==4:
                    self.listedejoueur.append(str(Joueur.joueur4))
                    self.nombrechoisi.append(self.joueurajoute)
                elif self.joueurajoute==5:

                    self.listedejoueur.append(str(Joueur.joueur5))
                    self.nombrechoisi.append(self.joueurajoute)


                nombrejoueurclub+=1
        return self.listedejoueur
    def __str__ (self):
        texteAffichage= self.nomclub+" "+str(self.joueurdansequipe())

        return texteAffichage
equipe1= Equipe("Real Madrid")
print(equipe1)




