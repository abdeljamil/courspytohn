#coding:utf-8

#classe str : string (chaîne de caractère )

"""
NOTES
Une Méthode de la chaîne travaille sur une copie, et pas sur la chaîne elle-même.
str.upper();str.lower();str.capitalize();str.title();
str.center(<largeur>;<caractere_remplisage>)
str.find(<chaine>;<debut>;<fin>)
str.index(<chaine>;<debut>;<fin>)
str.replace(<ancien>,<nouvelle>,<occurences>)
str.isalpha(),str.isdecimal(),str.isnumeric()
str.isalphanum()
str.islowwer(),str.isupper()
str.isidentifier(),str.isKeyword()
"""


# ma_chaine = "bonjour tout le monde"

# ma_chaine = ma_chaine.upper() 
# print(ma_chaine)


# ma_chaine = ma_chaine.lower() 
# print(ma_chaine)

# ma_chaine = ma_chaine.capitalize() 
# print(ma_chaine)

# ma_chaine = ma_chaine.title() 
# print(ma_chaine)



# ch1 = "bonjour"
# ch2 = ch1


# print(ch1)
# print(ch2)

# ch1 = ch1.upper()

# print(ch1)
# print(ch2)




# ma_chaine = "MonsuperProgramme"
# print(ma_chaine)

# ma_chaine = ma_chaine.center(50,"-")

# print(ma_chaine)


# ma_chaine = "MonSuperProgramme"

# print(ma_chaine.find("Super"))


# ma_chaine = "MonSuperProgramme"
# try:
#   print(ma_chaine.index("super"))
# except:
#   print("Je n'ai pas trouvé cette chaîne de caractére")



# ma_chaîne = "[  MonSuperProgramme    ]"

# print(ma_chaîne)
# print(ma_chaîne.strip())



# ma_chaine = "abababab"
# print(ma_chaine)
# ma_chaine = ma_chaine.replace("a","z")
# print(ma_chaine.strip())



# ma_chaine = "abababab"
# print(ma_chaine)
# ma_chaine = ma_chaine.replace("a","z",1)
# print(ma_chaine)


# phrase = "Magicien|10|5"

# print(phrase.split("|"))




# ch = "bonjour"

# if ch.islower():
#     print("Minuscule")
# else:
#     print("La chaîne contient des majuscules")




# ch = "class"

# if ch.isidentifier():
#     print("Réservé")
# else:
#     print("Libre")



# ch = "18"

# if ch.isidentifier():
#     print("Réservé")
# else:
#     print("Libre")



ch = "Le langage Python"

if "langage" in ch:
    print("Trouvé")
else:
    print("Non trouvé")