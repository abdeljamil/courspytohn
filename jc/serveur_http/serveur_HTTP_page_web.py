# import http.server

# port = 90

# address = ("",port)
# server = http.server.HTTPServer

# handler = http.server.CGIHTTPRequestHandler
# handler.cgi_directories = ["/"]

# httpd = server(address,handler)

# print(f"Serveur démarré sur le PORT {port}")

# httpd.serve_forever()
 

import http.server

port = 8000  # Changed from 90 to a non-privileged port

address = ("", port)
server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
# handler.cgi_directories = ["/"]
handler.cgi_directories = ["/cgi-bin"]

httpd = server(address, handler)

print(f"Serveur démarré sur le PORT {port}")

httpd.serve_forever()