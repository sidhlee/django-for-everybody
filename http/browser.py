import socket

# 1. Create a socket - make a phone!
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. Dial up
mysock.connect(("data.pr4e.org", 80))

# 3. Send command
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()  # to utf8
mysock.send(cmd)

while True:
    # wait and receive up to 512 characters
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mysock.close()

# HTTP/1.1 200 OK
# Date: Sat, 13 Nov 2021 21:45:07 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Mon, 15 May 2017 11:11:47 GMT
# ETag: "80-54f8e1f004857"
# Accept-Ranges: bytes
# Content-Length: 128
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/html

# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://data.pr4e.org/page2.htm">
# Second Page</a>.
# </p>
