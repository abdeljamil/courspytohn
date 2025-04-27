#coding:utf-8

"""
Modes d'ouverture : r (lecture seule)
                    w (écriture avec remplacement)
                    a (écriture avec ajout en fin de fichier)
                    r+(lecture/écriture dans un même fichier)

                    
Lecture           : read(),readline(),readlines()
"""

# fic = open("docs/donnees.txt","r")
# print(fic.read())
# fic.close()



# fic = open("docs/donnees.txt","r")
# content = fic.read()
# print(content)
# fic.close()

# fic = open("docs/donnees.txt","r")
# line = fic.readline()
# print(line)
# fic.close()

# fic = open("docs/donnees.txt","r")
# line = fic.readline()
# print(line)
# line = fic.readline()
# print(line)
# line = fic.readline()
# print(line)
# line = fic.readline()
# print(line)
# fic.close()

# fic = open("docs/donnees.txt","r")
# line = fic.readline()
# print(line)
# line = fic.readline()
# print(line)
# line = fic.readline()
# print(line)
# line = fic.readlines()
# print(line)
# fic.close()


# fic = open("docs/donnees.txt","r")
# nombre = 15
# content = fic.read()
# content = int(content)
# print(content)
# fic.close()


with open("docs/donnees.txt","r") as fic:
    content = fic.read()
    print(content)
# Pas besoin de fermer le fichier avec with fic.close()