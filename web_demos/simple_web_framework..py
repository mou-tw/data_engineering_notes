import socket
from datetime import datetime

sk = socket.socket()
sk.bind(('127.0.0.1',9487))
sk.listen()

dt_now = datetime.strftime(datetime.now(), '%Y%m%d')

def func_t1():
    with open('t1.html','r') as f:
        ret = f.read()
        ret = ret.replace('@Q@Q@Q@Q', dt_now)
        return bytes(ret, encoding='utf-8')

def func_not_found():
    ret = 'Page Not Found'
    return bytes(ret, encoding='utf-8')

mapping_dict = {
    '/test' : func_t1
}


while 1:
    conn, _ = sk.accept()
    request_data = conn.recv(8096)
    request_data = str(request_data, encoding='utf-8')
    
    url = request_data.split('\r\n')[0]
    url = url.split()[1]
    print(url)

    #http protocol
    conn.send(b'http/1.1 200 OK\r\ncontent-type:text/html; charset=utf-8\r\n\r\n')


    if url in mapping_dict.keys():
        conn.send(mapping_dict[url]())
    else:
        conn.send(func_not_found())

    #close all connection
    conn.close()
    sk.close()