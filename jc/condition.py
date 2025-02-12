"""
Operateurs de comparaison : == (égal à)
                            != (difference de)
                            < (plus petit que)
                            > (plus grand que)
                            <= (plus petit ou égal à)
                            >=(plus grand ou égal à)

Mots clés des conditions   : if/elif /else                          


condition multiples     : and(ET)
                        : or(OU)
                        : in/not in (DANS / PAS DANS)                       
"""






# identifiant = "jason"
# mot_de_passe = "passeword123"

# print("Interface de connexion")

# user_id = input("Entrez votre identifiant : ")
# user_password = input("Entrez votre mot de passe : ")

# if user_id== identifiant and user_password == mot_de_passe:
#     print("Vous êtes connectés,Bienvenu",user_id) 
# print("je ne suis pas dans le 'if'")




# lettre_hasard = "i"
# if lettre_hasard  in 'aeiouy':
#     print("c'est une consonne")
# if lettre_hasard not in 'aeiouy':
#     print("c'est une consonne")




# lettre_hasard = "i"

# if lettre_hasard in "aeiouy":
#     print("c'est une voyelle")
# else:
#     print("c'est une consonne")
    



# age = 60

# if age == 18:
#     print("Tu viens d'être majeur")
# elif age == 50:
#     print("tu viens d'avoir 50 ans")
# elif age == 60:
#     print("Tu viens d'avoir 60 ans")
# else :
#     print("Tu as",age ,"ans")    




# jeu_charge = False #True = vrai(=1)

# if jeu_charge:
#     print("Le jeu est en marche")
# else:
#     print("Le jeu a été quité")



# jeu_charge = True #True = vrai(=1)

# if jeu_charge:
#     print("Le jeu est en marche")
# else:
#     print("Le jeu a été quité")



# jeu_charge = False #True = vrai(=1)

# if not jeu_charge:
#     print("Le jeu est étient")
# else:
#     print("Le jeu est lancé")


age = input("Quel âge as-tu ??")
age = int(age)
"""
 age > 0 ET age <= 100 --> 0 < age <= 100
"""
if age > 0 and age <= 100:
    print("L'âge est validé")
else:
    print("L'âge est incorrect")    