#!/usr/bin/env python3
import cgi

print("Content-type: text/html;charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma Page Web Simple</title>
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
        button {
            display: inline-block;
            padding: 10px 20px;
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
    <header>
        <h1>Bienvenue sur ma page web</h1>
    </header>
    <div class="container">
        <p>Ceci est un exemple simple d'une page web utilisant HTML et CSS.</p>
        <button>Cliquez-moi</button>
    </div>
</body>
</html>

"""

print(html)







