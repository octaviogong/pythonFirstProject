import socket

server_sock = socket.socket()
#host = socket.gethostname()
host = 'localhost'
print(server_sock)
print(host)
port = 9999

#print(server_sock.fileno())
#print(server_sock.family)
#print(server_sock.type)
#print(server_sock.proto)

server_sock.bind((host, port))

print("Esperando conexiones...")
server_sock.listen(1)

while True:
    client_sock, addr = server_sock.accept()
    print(addr)
    print(f"Cliente conectado de la dirección: {addr}")
    msj = 'Hola ' + addr[0] + ':' + str(addr[1])
    client_sock.send(msj.encode())
    client_sock.close()