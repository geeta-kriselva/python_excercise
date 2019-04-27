import socket
#Establish connetion
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
#sending request to get data
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
#receiving data
while True:
    data = mysock.recv(1000)
    #checking end of data
    if (len(data) < 1):
        break
    print(data.decode(), end = '')
#closing connection
mysock.close()
