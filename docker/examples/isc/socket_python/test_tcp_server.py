import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 12345))
sock.listen()

conn, addr = sock.accept()
with conn:
    print(f'Connection de {addr} etablie')
    data = conn.recv(1024)
    print(f'Recu : {data}')