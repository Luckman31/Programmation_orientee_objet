
import random
class Joueur:

    def __init__(self,prenom,nom,nationalite,piedfort):
        self.prenom=prenom
        self.nom=nom
        self.nationalite=nationalite
        self.piedfort=piedfort
        self.caracteristiques = {}
        self.ajouterCarac()
        self.poste=""

    def ajouterCarac(self):
        caracteristique={"Vitesse":random.randint(30,99), "tir":random.randint(30,99),"passe":random.randint(30,99),"dribble":random.randint(30,99),"defense":random.randint(30,99),"physique":random.randint(30,99)}
        print(caracteristique)
        reponse=str(input("Est-ce que les caractéristiques de "+self.prenom +" "+self.nom+" te conviennent (o ou n) "))
        while reponse=="n":
            caracteristique={"Vitesse":random.randint(30,99), "tir":random.randint(30,99),"passe":random.randint(30,99),"dribble":random.randint(30,99),"defense":random.randint(30,99),"physique":random.randint(30,99)}
            print(caracteristique)
            reponse=str(input("Est-ce que les caractéristiques te conviennent (o ou n) "))

        self.caracteristiques = caracteristique



    def definirposte(self):
        poste=""
        while poste!="att" and poste!="mil" and poste !="def":
            poste=input("Choisissez le poste de "+self.prenom+" "+self.nom+" entre att, mil et def ")

            if poste!="att" and poste!="mil" and poste !="def":
                print("ERREUR!!!!! Tu peux seulement choisir entre att, mil et def " )

        return poste
    def __str__ (self):
        texteAffichage= self.prenom+" "+self.nom+" "+self.nationalite+" "+self.piedfort+" "+ str(self.definirposte())+" "
        somme=0
        for cle, valeur in self.caracteristiques.items():
            texteAffichage += cle + " : " + str(valeur) + " "
            somme += valeur
        note=somme/6
        texteAffichage += "Note : " + str(note)
        return texteAffichage

joueur1= Joueur("Karim", "Benzema", "France", "Droitier")



joueur2= Joueur("Vinicius", "Junior", "Bresil", "Droitier")


joueur3= Joueur("David", "Alaba", "Autriche", "Gaucher")


joueur4= Joueur("Luka", "Modric", "Croatie", "Droitier")


joueur5= Joueur("Eder", "Militao", "Bresil", "Droitier")

"""
joueur6= Joueur("Iago", "Aspas", "Espagne", "Gaucher")
print(joueur6)

joueur7= Joueur("Jason", "Murillo", "Colombie", "Droitier")
print(joueur7)

joueur8= Joueur("Denis", "Suarez", "Espagne", "Droitier")
print(joueur8)

joueur9= Joueur("Thiago", "Galhardo", "Bresil", "Droitier")
print(joueur9)

joueur10= Joueur("Hugo", "Mallo", "Espagne", "Droitier")
print(joueur10)

joueur11= Joueur("Memphis", "Depay", "Pays-Bas", "Droitier")
print(joueur11)

joueur12= Joueur("Frenkie", "De Jong", "Pays-bas", "Droitier")
print(joueur12)

joueur13= Joueur("Jordi", "Alba", "Espagne", "Gaucher")
print(joueur13)

joueur14= Joueur("Gerard", "Pique", "Espagne", "Droitier")
print(joueur14)

joueur15= Joueur("Ansu", "Fati", "Espagne", "Droitier")
print(joueur15)

joueur16= Joueur("Marcos", "LLorente", "Espagne", "Droitier")
print(joueur16)

joueur17= Joueur("Luis", "Suarez", "Uruguay", "Droitier")
print(joueur17)

joueur18= Joueur("Antoine", "Griezmann", "France", "Gaucher")
print(joueur18)

joueur19= Joueur("Kylian", "Mbappe", "France", "Droitier")
print(joueur19)

joueur20= Joueur("Lionel", "Messi", "Argentine", "Gaucher")
print(joueur20)

joueur21= Joueur("Robert", "Lewandowski", "Pologne", "Droitier")
print(joueur21)

joueur22= Joueur("Erling", "Haaland", "Norvege", "Gaucher")
print(joueur22)

joueur23= Joueur("Eden", "Hazard", "Belgique", "Droitier")
print(joueur23)

joueur24= Joueur("Neymar", "Junior", "Bresil", "Droitier")
print(joueur24)

joueur25= Joueur("Cristiano", "Ronaldo", "Portugal", "Droitier")
print(joueur25)
"""