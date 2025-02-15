#coding:utf-8

"""
Importer un module : import <nom_module>
                     from <nom_module> import
                     from <nom_du_module> import *
"""
 
#les fonctions lambdas

# coucou = lambda:print("Bonjour") 
# coucou()

# ttc = lambda prixHT:prixHT+(prixHT * 20/100)
# print(ttc(24))


# calculer = lambda a, b : a + b
# print(calculer(14 , 27))


#Modularité

# import math

# resultat = math.sqrt(100)

# print(resultat)

from  math import *

resultat = sqrt(255)
print(resultat)