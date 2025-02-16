#coding:utf-8

"""
module pour joueur
"""

def parler(personnage,message):
    print("{} : {}".format(personnage,message))

def au_revoir():
    print("Au revoir :)!")

if __name__ == "__main__":
    parler("jason","bonjour tout le monde")
    au_revoir    