from os import CLD_EXITED
from socket import *


def createServer():
    # 1. Make a socket (phone)
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # bind server address to socket
        serversocket.bind(("localhost", 9000))
        # queue up to 5 request
        serversocket.listen(5)
        while 1:
            # wait (blocking) until request is accepted
            (clientsocket, address) = serversocket.accept()

            # client will always talk first in http
            rd = clientsocket.recv(5000).decode()  # to unicode
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())  # to utf8
            clientsocket.shutdown(SHUT_WR)
            # client will have to close after server shuts down

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:\n")
        print(exc)

    serversocket.close()


print("Access http://localhost:9000")
createServer()

# ➜  http git:(main) ✗ python3 server.py
# Access http://localhost:9000
# GET / HTTP/1.1 # your request
# GET /favicon.ico HTTP/1.1 # browser asking for favicon to show
