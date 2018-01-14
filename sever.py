import socket

host = socket.gethostname()
port = 5000
server_socket = socket.socket()

server_socket.bind((host,port))
server_socket.listen(2);

while True:
	conn,address = server_socket.accept()
	conn.send("lol")

server_socket.close()