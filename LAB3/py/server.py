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

pattern = "00000000"
encodingPatterns = ["000-+0+-", "000+-0-+"]

def decoding(val):
    value = val
    # Replace any encoding pattern found in the string by "00000000"
    value = value.replace(encodingPatterns[0], pattern,
                          value.count(encodingPatterns[0]))
    value = value.replace(encodingPatterns[1], pattern,
                          value.count(encodingPatterns[1]))
    # Replace + and - by 1
    value = value.replace("+", "1", value.count("+"))
    value = value.replace("-", "1", value.count("-"))
    return value

while True:
    conn, address = server.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle, args=(conn,))
    thread.start()