import socket

# set l'adresse et e port pour communiquer avec le serveur
host, port = ("127.0.0.1", 4444)
# on cree le socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # on connect le client au serveur
    clientSocket.connect((host, port))
    print("Le client est connecte ")

    # Il faut encoder l'information avant de l'envoyer
    data = input("Client : ")
    data = data.encode("utf8")
    # on envoie l'information
    clientSocket.send(data)


except ConnectionRefusedError:
    print("La connexion au serveur a echoue ")
finally:
    clientSocket.close()
