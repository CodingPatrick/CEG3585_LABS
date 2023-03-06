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

def encoding(message):
    output = []
    b = message
    change = 1
    i=0
    while(i<len(b)):
        if(i<=(len(b)-8) and b[i]=='0' and b[i+1]=='0' and b[i+2]=='0' and b[i+3]=='0' and b[i+4]=='0' and b[i+5]=='0' and b[i+6]=='0' and b[i+7]=='0' and i!=0  ):
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
            output.append(change)
            i+=1
            if(change == 1):
                change = -1
            else:
                change = 1
    return output

sending = threading.Thread(target=send)
sending.start()
receiving = threading.Thread(target=get)
receiving.start()