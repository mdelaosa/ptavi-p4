#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de SIP en UDP simple
"""

import socketserver
import sys
import json
import time

class SIPRegistrerHandler(socketserver.DatagramRequestHandler):
    """
        SIP server class
    """

    def handle(self):

        while 1:
            #Leyendo lo que envia el cliente.
            line = self.rfile.read()
            line_client = line.decode('utf-8').split()
            if not line:
                break  # Termina el bucle infinito
            else:
                print("RECEIVED \r\n")

            if line_client[0] == 'REGISTER':
                # Guardamos dirección e IP en nuestro diccionario.
                servidor = line_client[1].split(':')
                user = servidor[1]
                dicc['IP'] = self.client_address[0]
                dicc['SERVER'] = user
                self.wfile.write(b"SIP/2.0 200 OK" + b'\r\n')
                print(dicc)
                if line_client[3] == '0':
                    print("DELETING DIC")
                    del dicc['IP'], dicc['SERVER']
                    self.wfile.write(b"SIP/2.0 200 OK" + b'\r\n\r\n')


if __name__ == "__main__":

    dicc = {}
    try:
        PORT = int(sys.argv[1])
    except IndexError:
        sys.exit("Debe introducir: server.py port_number")
    """Creamos UDP en el puerto que indicamos utilizando la clase."""
    serv = socketserver.UDPServer(('', PORT), SIPRegistrerHandler)
    print("Iniciando servidor... \r\n")
    try:
        """Creamos el servidor"""
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
