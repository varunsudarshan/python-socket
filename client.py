import socket

host = socket.gethostname()
port = 5000
cl_socket = socket.socket()

cl_socket.connect((host,port))
data = cl_socket.recv(1024).decode()
print data

cl_socket.close()