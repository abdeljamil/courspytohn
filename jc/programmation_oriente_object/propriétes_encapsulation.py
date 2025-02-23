#coding:utf-8

"""
Propriété : Maniére de manipuler/contrôler des attributs
            principe d'encapsulation !
"""


# class Humain:
#     def __init__(self,nom,age):
#         print("Création d'un Humain....")
#         self.nom = nom
#         self._age = age
#     def _getage(self):
#         return self._age
#     #property(<getter>,<setter>,<deleter>,<helper>)
#     age = property(_getage)

# #Programme principal 

# h1 = Humain("Jason",26)

# print(h1.age)
# # h1.age = 14
# # print(h1.age) 


class Humain:
    def __init__(self,nom,age):
        print("Création d'un Humain....")
        self.nom = nom
        self._age = age
    def _getage(self):
        return self._age
    def _getage(self):
        return self._age
    def _setage(self,nouvel_age):
        self._age = nouvel_age
    #property(<getter>,<setter>,<deleter>,<helper>)
    age = property(_getage,_setage)

#Programme principal 

h1 = Humain("Jason",26)

print(h1.age)
h1.age = 20
print(h1.age)
# h1.age = 14
# print(h1.age) 