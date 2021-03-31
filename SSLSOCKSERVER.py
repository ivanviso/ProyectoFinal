#!/usr/bin/python3

import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET, SHUT_RDWR
import ssl
import wgtools #https://github.com/conqp/wgtools
import wgconf
listen_addr = '127.0.0.1'
listen_port = 8082
server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.load_verify_locations(cafile=client_certs)

bindsocket = socket.socket()
bindsocket.bind((listen_addr, listen_port))
bindsocket.listen(0)


while True:
    print("Waiting for client")
    newsocket, fromaddr = bindsocket.accept()
    print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
    conn = context.wrap_socket(newsocket, server_side=True)
    print("SSL established. Peer: {}".format(conn.getpeercert()))
    inbuf = b''  # Buffer de data entrante
    outbuf = b''  # Buffer de data saliente
    bufExpect = b'AUTH' #Marcamos lo que espera el servidor para realizar el proceso de login 
    login=bool
    try:
        while True:
            data = conn.recv(4096)
            if data:
                # Client sent us data. Append to buffer
                inbuf = data
                print("Received:", inbuf)
                if bufExpect==b'AUTH' and inbuf==b'AUTH':
                    conn.send(b'OK AUTH')
                    bufExpect=b'USER'
                    print("auth")
                if bufExpect==b'USER' and b'USER' in inbuf:
                    usuario=str(inbuf).split(" ", 1)
                    conn.send(b'OK USER')
                    bufExpect=b'PASS'
                    print("user", usuario)
                if bufExpect==b'PASS' and b'PASS' in inbuf:
                    psw=str(inbuf).split(" ", 1)
                    conn.send(b'OK PASS')
                    bufExpect=b'AUTH'
                    print("pass",psw)
                    login=True
                
                if login==True: 
                    public_key, private_key = wgtools.keypair()
                    conn.sendall(bytes(wgconf.clientwgconf(public_key,private_key), 'ascii'))
                    print(public_key)
            

            else:
                bufExpect=b'AUTH'
                break
    finally:
        print("Closing connection")
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()

