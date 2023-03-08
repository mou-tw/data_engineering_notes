import socket

sk = socket.socket()

sk.bind(('127.0.0.1',9487))

sk.listen()

while 1:
    conn, _ = sk.accept()
    request_data = conn.recv(8096)
    request_data = str(request_data, encoding='utf-8')
    print(request_data)
    
    #http protocol
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')
    conn.send(b'<h1>hello</h1>')

    #close all connection
    conn.close()
    sk.close()

