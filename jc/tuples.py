#utf-8

"""
Création de tuple : mon_tuple = () #vide 
                    mon_tuple = 17, #une seule valeur 
                    mon_tuple = (17,) #Idem qu'au-dessus 
                    mon_tuple = (4,5) #Plusieurs   valeurs

Accés aux valeurs : mon_tuple[X]    #valeur d'indice X

"""
# liste = [1,2,3,4,5,6]

# for chose in enumerate(liste):
#     print(chose)


# mon_tuple = ()
# print(type(mon_tuple))


# mon_tuple = (45)
# print(type(mon_tuple))


# mon_tuple = (45,64)
# print(mon_tuple[1])


# mon_tuple = (45,64)
# try:
#     print(mon_tuple[2])
# except:
#     print("Dépassement du tuplet")


# (nombre1,nombre2) = (14,46)

# print(nombre1)
# print(nombre2)


# (nombre1,nombre2) = (14,46)
# print(nombre1)
# print(nombre2)
# nombre1 = 128
# print(nombre1)



# def get_player_position ():
#     posX = 148
#     posY = 86

#     return(posX,posY)

# #Programme principal

# coordX = 0
# coordY = 0

# print("Position du joueur :  ({}/{}) ".format(coordX,coordY))
# (coordX,coordY )= get_player_position()
# print("Position du joueur :  ({}/{}) ".format(coordX,coordY))



def get_player_position ():
    posX = 148
    posY = 86

    return(posX,posY)

#Programme principal

coordX = 0
coordY = 0

print("Position du joueur :  ({}/{}) ".format(coordX,coordY))
(coordX,coordY )= get_player_position()

coordX = 150
coordY = 150

print("Position du joueur :  ({}/{}) ".format(coordX,coordY))