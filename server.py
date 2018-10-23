#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

PORT = int(sys.argv[1])  # Puerto en el que escuchamos


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"Hemos recibido tu peticion")
        IPc = self.client_address[0]  # IP del Cliente
        PORTc = self.client_address[1]  # Puerto del Cliente
        for line in self.rfile:
            print("El cliente nos manda ", line.decode('utf-8'), IPc, PORTc)


if __name__ == "__main__":
    # Listens at localhost ('') port which I want
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', PORT), EchoHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
