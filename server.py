#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

PORT = int(sys.argv[1])  # Puerto en el que escuchamos


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    dicc = {}
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        print(self.client_address)
        for line in self.rfile:
            if line.decode('utf-8')[:8]== 'REGISTER':
                print("El cliente nos manda ", line.decode('utf-8'))
                self.dicc['USER'] = line.decode('utf-8')[13:-10]
                self.dicc['IP'] = self.client_address[0]
        print(self.dicc)


if __name__ == "__main__":
    # Listens at localhost ('') port which I want
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")