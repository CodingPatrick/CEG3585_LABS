import socket
import sys
import selectors
import types

#selecteur
sel = selectors.DefaultSelector()

# le serveur n'as besoind d'adresse car il ne va qu'ecouter
host, port = ("", 4444)
# on cree le socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# pour se connecter avec une adresse (on associe le socket avec l'adresse )
serverSocket.bind((host, port))
print("Le serveur est en marche ... ")
serverSocket.listen()
print(f"Le serveur ecoute sur {(host, port)}")
#configurer le socket dans le non-blocking mode
serverSocket.setblocking(False)
#Enregistre le socket pour etre monitorer avec selectors
sel.register(serverSocket,selectors.EVENT_READ, data=None)


#accepter la connection
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    #Eviter le Hang State pour reduire l'attente
    conn.setblocking(False)
    #utiliser les donner pour name space pour savoir quand est ce que le client est pret a lire et écrire
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

#add comments
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print(f"Closing connection to {data.addr}")
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing {data.outb!r} to {data.addr}")
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

#FIXME
# on va faire ecouter le serveur sur le port continuellement
while True:
    # on va initialiser les connexion pour pouvoir les accepter
    conn, adress = serverSocket.accept()  # adresse = adresse IP + port
    print("Un client vient de se connecter ...")

    # on recois la donner
    data = conn.recv(1024)  # la taille de buffer pour receptioner l'info multiple de 2

    # on decode la donner
    message = data.decode("utf8")
    print(message)
    conn.send()


conn.close()
serverSocket.close()
