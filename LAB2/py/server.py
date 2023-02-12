# server

import socket

host, port = ("127.0.0.1", 4444)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print(f"\nServer is running on host: {host}, on port: {port}")

def handle_graph(conn):
    while True:
        data = conn.recv(1024)
        if data.decode().startswith('get'):
            graph = data.decode().split(' ', 2)[1:]
            get_graph(graph)

def get_graph(graph):
    if graph[0] == 'square_wave':
        import square_wave
    elif graph[0] == 'triangular_wave':
        import triangular_wave
    elif graph[0] == 'sawtooth_wave':
        import sawtooth_wave
    elif graph[0] == 'full_wave_rectified_sine':
        import full_wave_rectified_sine
    elif graph[0] == 'half_wave_rectified_sine':
        import half_wave_rectified_sine
    elif graph[0] == 'rectangular_pulse_train':
        import rectangular_pulse_train

while True:
    conn, address = server.accept()
    handle_graph(conn)