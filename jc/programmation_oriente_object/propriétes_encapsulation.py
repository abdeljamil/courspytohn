#coding:utf-8

"""
Propriété : Maniére de manipuler/contrôler des attributs
            principe d'encapsulation !
"""


class Humain:
    def __init__(self,nom,age):
        self.nom = nom
        self._age = age

    #property(<getter>,<setter>,<deleter>,<helper>)

#Programme principal 

h1 = Humain("Jason",26)

print(h1.age)
h1.age = 14
print(h1.age) 