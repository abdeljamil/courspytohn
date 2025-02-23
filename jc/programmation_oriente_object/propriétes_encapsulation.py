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


# class Humain:
#     def __init__(self,nom,age):
#         print("Création d'un Humain....")
#         self.nom = nom
#         self._age = age
#     def _getage(self):
#         return self._age
#     def _getage(self):
#         return self._age
#     def _setage(self,nouvel_age):
#         self._age = nouvel_age
#     #property(<getter>,<setter>,<deleter>,<helper>)
#     age = property(_getage,_setage)

# #Programme principal 

# h1 = Humain("Jason",26)

# print(h1.age)
# h1.age = 20
# print(h1.age)
# # h1.age = 14
# # print(h1.age) 




# class Humain:
#     def __init__(self,nom,age):
#         print("Création d'un Humain....")
#         self.nom = nom
#         self._age = age
#     def _getage(self):
#         return self._age
#     # def _getage(self):
#     #     return self._age
#     def _setage(self,nouvel_age):
#         if nouvel_age < 0:
#             self._age = 0
#         else:
#             self._age = nouvel_age
        
#     #property(<getter>,<setter>,<deleter>,<helper>)
#     age = property(_getage,_setage)

# #Programme principal 

# h1 = Humain("Jason",26)

# print(h1.age)
# h1.age = -5
# print(h1.age)
# # h1.age = 14
# # print(h1.age) 




# class Humain:
#     def __init__(self,nom,age):
#         print("Création d'un Humain....")
#         self.nom = nom
#         self._age = age
#     def _getage(self):
#         try:
#          return self._age
#         except AttributeError:
#             print("L'age n'existe pas !")
    
#     def _setage(self,nouvel_age):
#         if nouvel_age < 0:
#             self._age = 0
#         else:
#             self._age = nouvel_age

#     def _delage(self):
#         del self._age
#     #property(<getter>,<setter>,<deleter>,<helper>)
#     age = property(_getage,_setage,_delage)

# #Programme principal 

# h1 = Humain("Jason",26)

# print(h1.age)
# del h1.age
# print(h1.age)
# # h1.age = 14
# # print(h1.age) 









# class Humain:
#     """Cette classe represente un Humain"""
#     def __init__(self,nom,age):
#         print("Création d'un Humain....")
#         self.nom = nom
#         self._age = age
#     def _getage(self):
#         try:
#          return self._age
#         except AttributeError:
#             print("L'age n'existe pas !")
    
#     def _setage(self,nouvel_age):
#         if nouvel_age < 0:
#             self._age = 0
#         else:
#             self._age = nouvel_age

#     def _delage(self):
#         del self._age
#     #property(<getter>,<setter>,<deleter>,<helper>)
#     age = property(_getage,_setage,_delage,"Je suis l'age d'un humain")

# #Programme principal 

# help(Humain.age)








class Humain:
    """Cette classe represente un Humain"""
    def __init__(self,nom,age):
        print("Création d'un Humain....")
        self.nom = nom
        self._age = age

    def _getage(self):
        if self._age <= 1:
           return str(self._age) + "an"
        else:
             return str(self._age) + "ans"
        
    
   
    #property(<getter>,<setter>,<deleter>,<helper>)
    age = property(_getage)

#Programme principal 
h1 = Humain("Robert",45)

print("{} a {} ".format(h1.nom,h1.age))