import socket
import threading
import time

host, port = ("127.0.0.1", 4444)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print(f"\nB8ZS SERVER using Address: {host}:{port}\n")
clients = []
ids = {}

def handle(conn):
    while True:
        data = conn.recv(1024)
        message = data.decode()
        decoded = decoding(message)
        if data.decode().startswith('+') or data.decode().startswith('-'):       
            print('Sending request from client received')
            print('Sending message acception...')
            time.sleep(0.5)
            conn.sendall(f'OK'.encode())
            time.sleep(0.5)
            conn.sendall(f'RECEIVED'.encode())
            
            print(f'New message from Client : {message}')
            print(f'Encoded Message : {message}')
            print(f'Decoded Message : {decoded}')
            print('Sending confirmation of reception to the client.\n')
            time.sleep(0.5)
            conn.sendall(f'Message received!\n'.encode())

def decoding(message):
    output = []
    outString = ''
    b = message
    i=0
    while(i<len(b)):
        if(i == 0):
            if(b[i] == '+' or b[i] == '-'):
                output.append(1)
                i+=1
        if(i<=(len(b)-8) and b[i]=='0' and b[i+1]=='0' and b[i+2]=='0' and b[i+3]=='+' and b[i+4]=='-' and b[i+5]=='0' and b[i+6]=='-' and b[i+7]=='+' and i!=0):
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            output.append(0)
            i+=8
        elif(i<=(len(b)-8) and b[i]=='0' and b[i+1]=='0' and b[i+2]=='0' and b[i+3]=='-' and b[i+4]=='+' and b[i+5]=='0' and b[i+6]=='+' and b[i+7]=='-' and i!=0):
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
            i+=1
        elif (b[i] == '0'):
            output.append(0)
            i+=1
    outString = ''.join(str(e) for e in output)
    return outString

while True:
    conn, address = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle, args=(conn,))
    thread.start()