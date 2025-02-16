# coding:utf-8


"""
Gérer les exceptions : try/except (+ else,finaly)

Type d'exceptions  :ValueError
                    NameError
                    TypeError
                    ZeroDivisionError
                    OSError
                    AssertionError
"""
# ageUtilisateur = input("Quel âge as-tu ?")
# ageUtilisateur = int(ageUtilisateur)
# print("Tu as",ageUtilisateur,"ans")




# ageUtilisateur = input("Quel âge as-tu ?")
# try:
#     ageUtilisateur = int(ageUtilisateur)
# except:
#     print("L'âge indiqué est incorrect !")
# else:
#     print("Tu as",ageUtilisateur,"ans")
# finally:
#     print("FIN DU PROGRAMME")


# nombre1 = 150 
# nombre2 = input("choiser le nombre pour diviser :")
# nombre2=int (nombre2)
# print("Résultat = {}".format(nombre1/nombre2))





# nombre1 = 150
# nombre2 = input("Choisir le nombre pour diviser : ")
# try:
#     nombre2 = int(nombre2)
#     print("Résultat = {}".format(nombre1 / nombre2))
# except ZeroDivisionError:
#     print("Vous ne pouvez pas diviser par zero.")
# except ValueError:
#     print("Vous devez entrer un nombre.")
# except:
#     print("Valeur incorrect.")
# else:
#     print("Bravo, tu as noté un nombre valide !")
# finally:
#     print("Fin du programme...")




# try:
#     age = input("Quel âge as-tu ?")
#     age = int(age)

#     assert age > 26 #Je veux que age soit plus grand que 25

# except AssertionError:
#     print("J'ai attrapé l'exception")



try:
    age = input("Quel âge as-tu ?")
    age = int(age)
except:
    print("Age incorect")

    