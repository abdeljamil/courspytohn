 #coding:utf-8

#classe
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


class vehicule:
    def __init__(self,nom_vehicule,quantite_essence):
        self.nom = nom_vehicule
        self.essence = quantite_essence

    def se_deplacer(self):
        print("Le vehicule {} se deplace....".format(self.nom))
    
#classe fille  
class voiture(vehicule):
    def __init__(self, nom_vehicule, essence,puissance):
        #super().__init__(nom_vehicule, essence,puissance)
        vehicule.__init__(nom_vehicule,essence)
        self.puissance = puissance 

#Programme Principal 
voiture1 =voiture("Toyota Supra",90 ,420)