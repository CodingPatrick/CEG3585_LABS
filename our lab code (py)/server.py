import socket
import threading

host, port = ("127.0.0.1", 4444)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print(f"\nServer is running on host: {host}, on port: {port}")
clients = []
ids = {}

def add(conn):
    while True:
        data = conn.recv(1024)
        if data.decode().startswith('find'):
            find(conn)
        elif data.decode().startswith('to'):
            receiver, message = data.decode().split(' ', 2)[1:]
            to(receiver, message, conn)
        else:
            broadcast(data, conn)

def find(conn):
    connections = ''
    for i in clients:
        connections = connections + str(ids[i])
    conn.sendall(f'The client ids currently connected to the server are: {connections}'.encode())

def to(receiver, message, conn):
    for i in ids.keys():
        if ids[i][1] == int(receiver):
            i.sendall(f'Message from {ids[conn]}: {message}'.encode())
            return

def broadcast(data, conn):
    for i in clients:
        if i != conn:
            i.sendall(f'Message from {ids[conn]}: {data.decode()}'.encode())

while True:
    conn, address = server.accept()
    clients.append(conn)
    ids[conn] = address
    print(f'{address} connected.')
    conn.sendall(f'\nWelcome {address}!'.encode())
    thread = threading.Thread(target=add, args=(conn,))
    thread.start()