#coding:utf-8

"""
Modes d'ouverture : r (lecture seule)
                    w (écriture avec remplacement)
                    a (écriture avec ajout en fin de fichier)
                    r+(lecture/écriture dans un même fichier)

                    
Lecture           : read(),readline(),readlines()
Ecriture          : write()
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


# with open("docs/donnees.txt","r") as fic:
#     content = fic.read()
#     print(content)
# # Pas besoin de fermer le fichier avec with fic.close()

# if fic.closed:
#     print("fermé")



# with open("docs/donnees.txt","r") as fic:
#     content = fic.read()
#     print(content)
# # Pas besoin de fermer le fichier avec with fic.close()

# print("Le reste du programme.....")


# with open("docs/donnees.txt","w") as fic:
#     nombre = 15  
#     fic.write(str(nombre))
#     fic.write("Bonjour,Je suis une phrase")
#     fic.write("Et,une autre....")



# import pickle
# class player:
#     def __init__(self,name,level):
#         self.name = name
#         self.level = level

#     def whoami(self):
#         print("{}({})".format(self.name,self.level))

# P1 = player("Jason",10)
# # P1.whoami()
# with open("player.data","wb") as fic:
#     record = pickle.Pickler(fic)
#     record.dump(P1)


import pickle
class player:
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def whoami(self):
        print("{}({})".format(self.name,self.level))

# P1 = player("Jason",10)
# P1.whoami()
with open("player.data","rb") as fic:
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()
player_one.whoami()