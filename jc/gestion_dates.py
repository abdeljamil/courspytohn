# import datetime

# d1 = datetime.datetime(2018, 2 , 28, 9 , 36 , 42)
# print(d1)





# import datetime

# d1 = datetime.datetime(2018, 2 , 28, 9 , 36 , 42)
# d2 = datetime.datetime(2018, 2 , 27, 9 , 36 , 42)

# if d1 < d2:
#     print("d1 est plus ancien que d2")
# else:
#     print("d1 est plus récent que d2")




# import datetime

# d1 = datetime.date(2018, 3 , 1)
# d2 = datetime.date(2018, 2 , 27)

# if d1 < d2:
#     print("d1 est plus ancien que d2")
# else:
#     print("d1 est plus récent que d2")






# import datetime

# d1 = datetime.date(2018, 3 , 1)
# d2 = datetime.date(2018, 2 , 27)

# print(d1.year)
# print(type(d1))





# import datetime

# t1 = datetime.time(23,00,46)

# print(t1)






# from datetime import datetime

# print(datetime.now())





# from datetime import date

# now = date.today()

# print(now)




import datetime
from datetime import date

now = date.today()
born = datetime.date(1998,2,10)
print(f"{now.year - born.year} ans.")