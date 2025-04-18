#coding:utf-8

"""
création de dictionnaire : dico = {} #vide
                         : dico = {<cle>:<valeur>,<cle2>:<valeur>}

Accès à une valeur       : dico[<cle>]
Ajout et modification    : dico[<cle>] = <valeur>

Suppression              : dico.pop(<cle>)
                         : dico.del[<cle>]

Copie                    : dico1 = {1:11,2:22}
                           dico2 = dico.copy()                          
"""
# dico = {"prénom":"jacson"}
# print(dico["prénom"])

# dico = {1:"jacson"}
# print(dico[1])

# dico = {"prénom":"jason"}

# print(dico["prénom"])

# dico = {"Achat":"c'est un félin"}

# print(dico["Achat"])


# dico = {"Achat":"c'est un félin"}
# dico ["chien"] = "c'est un mammifére,le meilleur ami de l'homme "
# print(dico)



# dico = {"Achat":"c'est un félin"}
# dico ["chien"] = "c'est un mammifére,le meilleur ami de l'homme "
# print(dico)


# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# print(dico)
# dico.pop("chien")
# print(dico)

# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# print(dico)
# valeur_supprimer = dico.pop("chien")
# print(valeur_supprimer)


# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# print(dico)
# del dico["Achat"]
# print(dico)



# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# if "chien" in dico:
#     print("oui")
# else:
#     print("Nom") 



# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# for key in dico:
#     print(key)


# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# for key in dico.keys():
#     print(key)


# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# for truc in dico.values():
#     print(truc) 

# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# for k,v in dico.items():
#     print("clé {} - valeur {}".format(k,v))

# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# dico[(2,3)] = "Ok"
# print(dico)

# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# dico2 = dico 
# print(dico)
# print(dico2)
# dico ["ok"] = "ok"
# print(dico)
# print(dico2)


# dico = {"Achat":"c'est un félin","chien":"c'est un mammifére,le meilleur ami de l'homme "}
# dico2 = dico.copy()
# print(dico)
# print(dico2)
# dico ["ok"] = "ok"
# print(dico)
# print(dico2)

def mafonctionBizarre(**parametres):
    print(parametres)

mafonctionBizarre(p=154, nom="blabla")