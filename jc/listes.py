#coding:utf-8

#Création d'une liste

"""
NOTES 
liste[X] = Affiche élément d'indixe X
liste[-X] = Affiche Xéme élément en partant de la fin 

list[:] = Affiche tous les éléments 
list[:X] = Affiche les X premiers éléments 
list[X:] = Affiche les X derniers éléments
list [A:B] = Affiche de l'élément d'indice A à l'élément indice B (exclus)

"""

# inventaire = list()

# print(type(inventaire)) 


# inventaire = list()

# print(inventaire)


# inventaire = []

# print(inventaire)


# inventaire = [1,6,15,"voiture"]

# print(inventaire)




# inventaire = [0]*10

# print(inventaire)

# inventaire = [1,6,15,"voiture"]*10

# print(inventaire)


# inventaire = range(20)
# print(inventaire)



# inventaire = range(20)

# i = 0
# while i < len(inventaire):
#     print(inventaire[i])
#     i += 1


# inventaire = ["Arc","épée","bouclier"]

# for valeur in inventaire:
#     print(valeur)



# inventaire = ["Arc","épée","bouclier"]

# for valeur in inventaire:
#     print(valeur)


# inventaire = ["Arc","épée","bouclier"]

# print(inventaire[1])

# inventaire = ["Arc","épée","bouclier"]

# print(inventaire[:])

# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]

# print(inventaire[3:])

# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]

# print(inventaire[-3])

# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]

# print(inventaire[-1])

# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]

# print(inventaire[0])


# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]

# print(inventaire[-4])

# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]

# print(inventaire[2:4])


# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]

# print(inventaire[2:5])


# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]
# print(inventaire[:])
# inventaire[2] = "bouclier d'acier"
# print(inventaire[:])


# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]
# print(inventaire[:])
# inventaire[:] = "bouclier d'acier"
# print(inventaire[:])


# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]
# print(inventaire[:])
# inventaire[:2] = "bouclier d'acier"
# print(inventaire[:])

# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]
# print(inventaire[:])
# inventaire[:] = "bouclier d'acier"
# print(inventaire[:])



# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]
# print(inventaire[:])
# inventaire[:2] = ["bouclier d'acier"] * 2
# print(inventaire[:])


# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]
# print(inventaire[:])
# inventaire[:] = ["bouclier d'acier"] * 4 
# print(inventaire[:])

# inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]
# print(inventaire[:])
# inventaire[:] = ["bouclier d'acier"] * len(inventaire) 
# print(inventaire[:])


inventaire = ["Arc","épée","bouclier","potion","fléches","tunique"]
print(inventaire[:])
inventaire[2:4] = ["bouclier d'acier"] * 2 
print(inventaire[:])