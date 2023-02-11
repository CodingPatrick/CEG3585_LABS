# client

import socket

host, port = ("127.0.0.1", 4444)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print(f"\nConnected to Server running on host: {host}, on port: {port}")

print('\n########################################')
print('# Command: <get> <graph>               #')
print('# Example: get square_wave             #')
print('# Graphs Types:                        #')
print('#         full_wave_rectified_sine     #')
print('#         half_wave_rectified_sine     #')
print('#         rectangular_pulse_train      #')
print('#         sawtooth_wave                #')
print('#         square_wave                  #')
print('#         triangular_wave              #')
print('########################################')
print(' ')

while True:
    message = input()
    client.sendall(message.encode())