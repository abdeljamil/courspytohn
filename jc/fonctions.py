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


def dire(nom_personne,message_personne):
    print("{} : {}".format(nom_personne,message_personne))
dire("Jason","Bonjour à tous")
dire("Tom","Salut!")    