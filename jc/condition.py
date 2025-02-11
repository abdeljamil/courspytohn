"""
Operateurs de comparaison : == (égal à)
                            != (difference de)
                            < (plus petit que)
                            > (plus grand que)
                            <= (plus petit ou égal à)
                            >=(plus grand ou égal à)
"""






identifiant = "jason"
mot_de_passe = "passeword123"

print("Interface de connexion")

user_id = input("Entrez votre identifiant : ")
user_password = input("Entrez votre mot de passe : ")

if user_password == mot_de_passe:
    print("Vous êtes connectés,Bienvenu",user_id) 

