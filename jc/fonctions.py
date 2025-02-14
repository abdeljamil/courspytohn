#coding:utf-8

"""
fonctions vues : print(),input()
                 type(),int(),float(),str(),bool()
"""


# print("Bonjour à tous ! :)")

# age = input("Quel âge as-tu?")
# age = int(age)
# print("Tu as {} ans.".format(age))


# def dire_bonjour ():
#         print("Bonjour tout le monde ! :)")
# #Je suis plus dans la fonction
# dire_bonjour()


# def dire(nom_personne,message_personne):
#     print("{} : {}".format(nom_personne,message_personne))
# dire("Jason","Bonjour à tous")
# dire("Tom","Salut!")    

# def dire(nom_personne="Tom",message_personne="salut!" ):
#     print("{}:{}".format(nom_personne,message_personne))
# dire("joson")

# def dire(nom_personne="Tom",message_personne="salut!" ):
#     print("{}:{}".format(nom_personne,message_personne))
# dire() 

# def dire(nom_personne="Tom",message_personne="salut!",age_personne="18" ):
#     print("{} ({} ans):{}".format(nom_personne,age_personne,message_personne))
# dire(message_personne="Yo!",age_personne=25,nom_personne="Roger") 

# def dire(nom_personne="Tom",message_personne="salut!",age_personne="18" ):
#     print("{} ({} ans):{}".format(nom_personne,age_personne,message_personne))
# dire(nom_personne="Jason",age_personne=25) 


# def show_inventory(*list_items):
#     for item in list_items:
#       print(item)



# show_inventory("épée")
# show_inventory("épée","arc","potion de nana","cape de Dragon rouge")



# def calculer_somme(nombre1,nombre2):
#     resultat = nombre1 + nombre2
#     return resultat

# print(calculer_somme(5,16))


# def calculer_somme(nombre1,nombre2):
#     resultat = nombre1 + nombre2
#     print("je ne serai jamais lu... :(")

# print(calculer_somme(5,16))

def le_plus_grand(nombre1, nombre2):
    if nombre1 > nombre2:
        return nombre1
    elif nombre1 < nombre2:
        return nombre2
    else:
        return "EGALIE"
print(le_plus_grand(5,16))