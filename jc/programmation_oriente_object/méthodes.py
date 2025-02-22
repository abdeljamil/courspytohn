"""
Méthode d'instance     :Fonction sur une  instence (Objet)
Méthode de classe      :Fonction sur une classe 
Méthode statique       :Fonction indépendante mais "lié" à une classe 
"""

class Humain:
    """ Classe qui définit un Humain"""

    lieu_habitation = "Terre"

    def __init__(self,nom,age):
        self.nom = nom
        self.age = age

    def parler(self,message): #self = méthode standard
        print("{} a dit : {}".format(self.nom,message))

    def changer_planete(cls,Nouvelle_planete): #cls = méthode de classe 
        Humain.lieu_habitation = Nouvelle_planete

    changer_planete = classmethod(changer_planete)

    def definition():
        print("L'Humain est classé comme étant le plus haut être-vivant de la planète terre.......")

    definition = staticmethod(definition)

#Programme principal

h1 = Humain("Jason",26)

# h1.parler("Bonjour à tous  ! :)")
# h1.parler("Comment allez-vous ??")

# print("planète actuelle : {}".format(Humain.lieu_habitation))

# Humain.changer_planete("Mars")

# print("planète actuelle : {}".format(Humain.lieu_habitation))

Humain.definition()
