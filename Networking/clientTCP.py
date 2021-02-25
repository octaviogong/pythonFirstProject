import socket
s = socket.socket()
#host = socket.gethostname()
host = 'localhost'
port = 9999
s.connect((host, port))

msj_recibido = s.recv(1024).decode()

s.close