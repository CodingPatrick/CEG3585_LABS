import socket
import threading
import time

host, port = ("127.0.0.1", 4444)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print(f"\nConnected to the server!\n")

def send():
    while True:
        message = input()
        encoded = encoding(message)
        print('Sending request to server')
        time.sleep(0.5)
        client.sendall(encoded.encode())

def get():
    while True:
        data = client.recv(1024).decode()
        if not data: break
        elif data.startswith('OK'):
            print('OK')
            print('Request accepted sending message...')
            time.sleep(0.5)
            client.sendall('Request accepted sending message...'.encode())
        elif data.startswith('RECEIVED'):
            print('RECEIVED')
        else: 
            print(data)

def encoding(message):
    output = []
    outString = ''
    b = message
    change = 1
    i=0
    while(i<len(b)):
        if(i<=(len(b)-8) and b[i]=='0' 
           and b[i+1]=='0' and b[i+2]=='0' 
           and b[i+3]=='0' and b[i+4]=='0' 
           and b[i+5]=='0' and b[i+6]=='0' 
           and b[i+7]=='0' and i!=0):
            if change==-1:
                output.append(0)
                output.append(0)
                output.append(0)
                output.append('+')
                output.append('-')
                output.append(0)
                output.append('-')
                output.append('+')
                i+=8
            else:
                output.append(0)
                output.append(0)
                output.append(0)
                output.append('-')
                output.append('+')
                output.append(0)
                output.append('+')
                output.append('-') 
                i+=8
        elif (b[i] == '0'):
            output.append(0)
            i+=1
        else:
            if change ==-1:
                output.append('-')
            elif change == 1:
                output.append('+')
            i+=1
            if(change == 1):
                change = -1
            else:
                change = 1
    outString = ''.join(str(e) for e in output)
    return outString

sending = threading.Thread(target=send)
sending.start()
receiving = threading.Thread(target=get)
receiving.start()