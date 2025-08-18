# #coding:utf-8
# import sqlite3

# connection = sqlite3.connect("base.db")
# cursor = connection.cursor()

# my_username = ("jamil",)
# cursor.execute('SELECT * FROM tt_users WHERE user_name = ?',my_username)
# result = cursor.fetchone()[1]
# print(f"le nom d'utilisateur est : {result}")
# connection.close()





# #coding:utf-8
# import sqlite3

# connection = sqlite3.connect("base.db")
# cursor = connection.cursor()

# new_user = (cursor.lastrowid,"jabir",45)
# cursor.execute('INSERT INTO tt_users VALUES(?,?,?)',new_user)
# connection.commit()
# print("Nouvel utilisateur ajouté !")

# connection.close()






# #coding:utf-8
# import sqlite3

# connection = sqlite3.connect("base.db")
# cursor = connection.cursor()

# req = cursor.execute('SELECT * FROM tt_users')
# print(req.fetchall())

# connection.close()





# #coding:utf-8
# import sqlite3

# connection = sqlite3.connect("base.db")
# cursor = connection.cursor()

# req = cursor.execute('SELECT * FROM tt_users')
# for row in req.fetchall():
#     print(row[1])


# connection.close()




# #coding:utf-8
# import sqlite3

# try:
#     connection = sqlite3.connect("base.db")
#     cursor = connection.cursor()
#     req = cursor.execute('SELECT * FROM tt_users')
#     for row in req.fetchall():
#         print(row[1])
# except Exception as e:
#     print("[ERREUR]",e)
#     connection.rollback()
# finally:
#     connection.close()




#coding:utf-8
import sqlite3

try:
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()
    user = ("Toto",)
    req = cursor.execute('SELECT * FROM tt_users WHERE user_name = ?',user)
    for row in req.fetchall():
        print(row[1])
except Exception as e:
    print("[ERREUR]",e)
    connection.rollback()
finally:
    connection.close()