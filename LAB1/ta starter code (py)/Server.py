import socket

# le serveur n'as besoind d'adresse car il ne va qu'ecouter
host, port = ("", 4444)
# on cree le socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# pour se connecter avec une adresse (on associe le socket avec l'adresse )
serverSocket.bind((host, port))
print("Le serveur est en marche ... ")

# on va faire ecouter le serveur sur le port continuellement
while True:
    # en lui passe en parametre le nombre de connexion qui peuvent echouer avant de le refuser (facultatif pour py 3.5)
    serverSocket.listen(5)
    # on va initialiser les connexion pour pouvoir les accepter
    conn, adress = serverSocket.accept()  # adresse = adresse IP + port
    print("Un client vient de se connecter ...")

    # on recois la donner
    data = conn.recv(1024)  # la taille de buffer pour receptioner l'info multiple de 2

    # on decode la donner
    message = data.decode("utf8")
    print(message)


conn.close()
serverSocket.close()
