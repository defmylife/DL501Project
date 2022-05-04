import socket
import os
from _thread import *
from urllib import response
ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0

# associate specific host and port
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
# queue up as many as 5 connect requests
ServerSideSocket.listen(5)

responseClinet = ''
def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(response))
        print(response)
    # responseClinet = response
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    # print(responseClinet)
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()