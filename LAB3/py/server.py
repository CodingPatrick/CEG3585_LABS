import socket
import threading

host, port = ("127.0.0.1", 4444)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print(f"\nServer is running on host: {host}, on port: {port}")
clients = []
ids = {}

def send(conn):
    while True:
        data = conn.recv(1024)
        if data.decode().startswith('pm'):
            receiver, message = data.decode().split(' ', 2)[1:]
            pm(receiver, message, conn)
        elif data.decode().startswith('conn'):
            client(conn)
        else:
            broadcast(data, conn)

def client(conn):
    connections = ''
    for i in clients:
        connections = connections + str(ids[i])
    conn.sendall(f'Active clients: {connections}'.encode())

def pm(receiver, message, conn):
    for i in ids.keys():
        if ids[i][1] == int(receiver):
            i.sendall(f'Message from {ids[conn]}: {message}'.encode())
            return

def broadcast(data, conn):
    for i in clients:
        if i != conn:
            i.sendall(f'Message from {ids[conn]}: {data.decode()}'.encode())

def decoding(message):
    output = []
    outString = ''
    b = message
    change = 1
    i=0
    while(i<len(b)):
        if(i == 0):
            if(b[i] == '+' or b[i] == '-'):
                 output.append(1)

        if(i<=(len(b)-8) and b[i]=='0' and b[i+1]=='0' and b[i+2]=='0' and b[i+3]=='+' and b[i+4]=='-' and b[i+5]=='0' and b[i+6]=='-' and b[i+7]=='+' and i!=0  ):
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            i+=8
        elif(i<=(len(b)-8) and b[i]=='0' and b[i+1]=='0' and b[i+2]=='0' and b[i+3]=='-' and b[i+4]=='+' and b[i+5]=='0' and b[i+6]=='+' and b[i+7]=='-' and i!=0  ):
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            i+=8
        elif(b[i]=='+' or b[i]=='-'):
            output.append(1)
    outString = ''.join(str(e) for e in output)
    return outString

while True:
    conn, address = server.accept()
    clients.append(conn)
    ids[conn] = address
    print(f'{address} connected.')
    conn.sendall(f'\nWelcome {address}!'.encode())
    thread = threading.Thread(target=send, args=(conn,))
    thread.start()