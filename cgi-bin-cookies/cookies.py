# #!/usr/bin/env python3
# import cgi
# import datetime
# import http.cookies

# expiration = datetime.datetime.now() + datetime.timedelta(days=365)
# expiration = expiration.strftime("%a,%d-%b-%Y %H:%M:%S")
# my_cookies = http.cookies.SimpleCookie()
# my_cookies["pref_lang"]="fr"
# my_cookies["pref_lang"]["expires"]=expiration
# my_cookies["pref_lang"]["httponly"]=True
# print(my_cookies.output())

# """
# expires
# path
# comment
# domain
# max-age
# secure
# verion
# httponly
# set-cookies: pref_lang=fr;secure httponly
# """


# print("Content-type: text/html;charset=utf-8\n")


# html = """<!DOCTYPE html>
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Ma Page Web Simple</title>
# </head>
# <body>
#         <h1>Cookies avec Python</h1>
# """
# print(html)
# print("<p>Bonjour !:</p>")
# html = """
# </body>
# </html>

# """

# print(html)










# #!/usr/bin/env python3
# import cgi
# import http.cookies
# import os

# print("Content-type: text/html;charset=utf-8\n")

# html = """<!DOCTYPE html>
# <html lang="fr">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Ma Page Web Simple</title>
# </head>
# <body>
#     <h1>Cookies avec Python</h1>
# """

# print(html)

# # Vérifier si des cookies existent
# if "HTTP_COOKIE" in os.environ:
#     print("Cookies reçus : ", os.environ["HTTP_COOKIE"])
# else:
#     print("Aucun cookie n'existe.")

# html = """
# </body>
# </html>
# """

# print(html)










#!/usr/bin/env python3

import cgi
import codecs
import http.cookies
import os
import sys

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("Content-type: text/html;charset=utf-8\n")

html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma Page Web Simple</title>
</head>
<body>
    <h1>Cookies avec Python</h1>
"""

print(html)

try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTT_COOKIE"])
    print("La langue choisie par l'utilisateur est :",user_lang["pref_lang"].value)
except(http.cookies.CookieError,KeyError):
    print("Non trouvé")
html = """ <p> Il était une fois ....</p>
</body>
</html>
"""

print(html)














