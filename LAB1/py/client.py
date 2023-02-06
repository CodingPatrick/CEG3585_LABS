import socket
import threading

host, port = ("127.0.0.1", 4444)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print(f"\nConnected to Server running on host: {host}, on port: {port}")

print('\n###########################################')
print('# Commands:                               #')
print('#                                         #')
print('# Current connections: conn               #')
print('# Send private message: pm                #')
print('# Broadcast: <message>                    #')
print('###########################################')

def send():
    while True:
        message = input()
        client.sendall(message.encode())

def get():
    while True:
        data = client.recv(1024).decode()
        if not data: break
        print(data)

sending = threading.Thread(target=send)
sending.start()
receiving = threading.Thread(target=get)
receiving.start()