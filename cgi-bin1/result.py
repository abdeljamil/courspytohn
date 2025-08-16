#!/usr/bin/env python3
import cgi
import cgitb

cgitb.enable()  # Active le mode de débogage pour afficher les erreurs

form = cgi.FieldStorage()



print("Content-type: text/html;charset=utf-8\n")

html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulaire Simple</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        header {
            background: #007bff;
            color: white;
            padding: 10px 20px;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            padding: 20px;
            background: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea {
            margin-bottom: 15px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px;
            font-size: 16px;
            color: white;
            background: #28a745;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #218838;
        }
    </style>
</head>
<body>
"""
print(html)

try:
    if form.getvalue("name"):
       name = form.getvalue("name")
       print(f"<p>Bonjour{name}</p>")
       print("<script>alert('OK')</script>")
    else:
       raise Exception("Pseudo non transmis")
except:
   print("<p> Pseudo non transmis </p>")


html = """
</body>
</html>
"""

print(html)
