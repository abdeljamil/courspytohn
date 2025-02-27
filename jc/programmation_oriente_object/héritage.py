 #coding:utf-8

"""
isinstance(<objet>,<class>):                  vérifi qu'un objet est de la classe renseignée
issubclass(<class_fille>,<classe_mere>):      vérifie qu'une classe est fille  d'une autre 
"""


#classe Mère
# class vehicule:
#     def __init__(self,nom,quantite_essence):
#         self.nom = nom
#         self.essence = quantite_essence

#     def se_deplacer(self):
#         print("Le vehicule se deplace....")
    
# #classe fille
# class voiture(vehicule):
#     pass
# #Programme Principal 
# v1 = vehicule("F22 Raptor",2400)
# print(v1.nom)
# v2 = vehicule("Toyota Supra",98)
# print(v2.nom)
# v1.se_deplacer()



# #classe Mère
# class vehicule:
#     def __init__(self,nom_vehicule,quantite_essence):
#         self.nom = nom_vehicule
#         self.essence = quantite_essence

#     def se_deplacer(self):
#         print("Le vehicule {} se deplace....".format(self.nom))
    
# #classe fille  
# class voiture(vehicule):
#     def __init__(self, nom_vehicule, essence,puissance):
#         #super().__init__(nom_vehicule, essence,puissance)
#         vehicule.__init__(self,nom_vehicule,essence)
#         self.puissance = puissance 
#     def se_deplacer(self):
#         print("Je roule....")
    

# class avion(vehicule):
#     def __init__(self, nom, essence,marchandise):
#         vehicule.__init__(self,nom, essence)
#         self.marchandise = marchandise
#     def se_deplacer(self):
#         print("Je survole les aires !!")

# #Programme Principal 
# voiture1 =voiture("Toyota Supra",90 ,420)
# voiture1.se_deplacer()
# print(voiture1.puissance,"CH")
# av1 = avion("F22 Raptor",2400,"Missilles")
#av1.se_deplacer()



# #Classe Mére 1

# class ObjetJeu:
#     pass

# #Classe Mére
# class Arme:
#     pass

# #classe Fille
# class Fusil(Arme,ObjetJeu):
#     pass

# #-------------------------------

# class Etudiant:
#     pass

# class Enseignant:
#     pass

# class Doctorant(Etudiant,Enseignant):
#     pass


class Animal:
    def __init__(self,nom):
        self.nom = nom

    def manger(self):
        print(self.nom,"mange.....")


class Reptile(Animal):
    def __init__(self, nom,regime_alimentaire):
        Animal.__init__(self,nom)
        self.regime = regime_alimentaire

    def manger(self):
        print("Le reptile mange....")


#code principal

Lezard = Reptile("Lézard","grenouilles")
# Lezard.manger()
#print(isinstance(Lezard,Animal))

# if isinstance(Lezard,Animal):
#     print("Lézard est un animal")

if issubclass(Reptile,Animal):
    print("Reptile hérite d'animal")