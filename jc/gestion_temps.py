# import time

# print("Le prelier text")

# time.sleep(5)

# print("Le second text")





# import time

# # 1 er janvier 1970 à 00h00

# print(time.time())




# import time

# begin = time.time()
# print("Début")

# time.sleep(5)

# end = time.time()
# print("Fin")




# import time

# begin = time.time()
# print("Début")

# time.sleep(5)

# end = time.time()
# print("Fin")

# print(f"Temps éxecuté:{end-begin}s")





# import time

# print(time.localtime())






# import time

# """
#                localtime()
# (TIMESTAMP)--------------->structure de temps
#            <---------------
#              mktime()                
# """


# tps = time.localtime()

# print(tps)

# tps = time.mktime(tps)
# print(tps)






import time

"""
%d :jour(01 à 31)
%m :mois(01 à 12)
%Y :année(ex:2018) - %y (00 à 99)
%H :Heure (00 à 23)
%I :minute (00 à 59)
%S :secondes (00 à 59)
%P :AM/PM

%A : jour de la semaine / %a (jour abrégé)
%B : mois / %b (mois abrégé)
%Z : fuseau horaire (timezone)
"""


"""
time.sleep()
    .time()
    .localtime()
    .mktime()
    .strftime()
"""


# print(time.strftime("%A"))
# print(time.strftime("%d"))
# print(time.strftime("%d/%m/%Y"))
# print(time.strftime("%Y-%m-%d"))

print(time.strftime("%Z"))