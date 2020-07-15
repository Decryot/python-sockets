import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(),1234))
server.listen(5)

while True:
    clientsocket, address = server.accept()
    print("connection from ",address)
    clientsocket.send(bytes("welcome to the server","utf-8"))
