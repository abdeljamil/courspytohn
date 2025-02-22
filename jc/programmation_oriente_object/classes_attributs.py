#coding:utf-8

# class Humain:
#    """
#    classes des être Humains
#    """
#    def __init__(self):
#         print("Création d'un humain...")

# print("Lancement du programme... ")

# h1 = Humain()
# h2 = Humain()




# class Humain:
#    """
#    classes des être Humains
#    """
#    def __init__(self):
#         print("Création d'un humain...")
#         self.prenom = "jojo"
#         self.age = 1

# print("Lancement du programme... ")

# h1 = Humain()
# print("Prénom de h1 -> {}".format(h1.prenom))
# h2 = Humain()  





# class Humain:
#    """
#    classes des être Humains
#    """
#    def __init__(self,c_prenom,c_age):
#         print("Création d'un humain...")
#         self.prenom = c_prenom
#         self.age = c_age
       
# print("Lancement du programme... ")
# h1 = Humain("jojo",34)
# print("Prénom h1 : {}".format(h1.prenom))
# print("Age de h1 : {}".format(h1.age))
# h2 = Humain("Albert",17)  
# print("Prénom h2 : {}".format(h2.prenom))
# print("Age de h2 : {}".format(h2.age))







# class Humain:
#    """
#    classes des être Humains
#    """
#    def __init__(self,c_prenom,c_age=1):
#         print("Création d'un humain...")
#         self.prenom = c_prenom
#         self.age = c_age
       
# print("Lancement du programme... ")
# h1 = Humain("jojo")
# print("Prénom h1 : {}".format(h1.prenom))
# print("Age de h1 : {}".format(h1.age))
# h2 = Humain("Albert",17)  
# print("Prénom h2 : {}".format(h2.prenom))
# print("Age de h2 : {}".format(h2.age))





# class Humain:
#    """
#    classes des être Humains
#    """
#    def __init__(self,c_prenom,c_age=1):
#         print("Création d'un humain...")
#         self.prenom = c_prenom
#         self.age = c_age
       
# print("Lancement du programme... ")
# h1 = Humain("jojo",34)
# print("Prénom h1 : {}".format(h1.prenom))
# print("Age de h1 : {}".format(h1.age))

# h1.prenom = "Thomas"
# h1.age = "26"
# print("Prénom h1 : {}".format(h1.prenom))
# print("Age de h1 : {}".format(h1.age))






class Humain:
   """
   classes des être Humains
   """
   humains_crees = 0
   def __init__(self,c_prenom,c_age=1):
        print("Création d'un humain...")
        self.prenom = c_prenom
        self.age = c_age
        Humain.humains_crees  +=1

print("Lancement du programme... ")
h1 = Humain("jojo",34)
print("Humaine existante : {}".format(Humain.humains_crees))
h2 = Humain("Albert",17)  
print("Humaine existante : {}".format(Humain.humains_crees)) 