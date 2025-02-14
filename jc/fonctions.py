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

def show_inventory(*items):
    show_inventory("épée")
    show_inventory("épée","arc","potion de nana","cape de Dragon rouge")
    