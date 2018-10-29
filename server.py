#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import time
import json


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        while 1:
            line = self.rfile.read()  # Leyendo lo que envia el cliente.
            line_client = line.decode('utf-8').split()
            if not line:
                break  # Termina el bucle
            else:
                print("Petición recibida \r\n")
            if line_client[0] == 'REGISTER':
                direccion = line_client[1].split(':')
                USER = direccion[1]
                IP = self.client_address[0]
                EXPIRES = int(line_client[4])
                time_actual = int(time.time())
                time_actual_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                                time.gmtime(time_actual))
                time_exp = int(EXPIRES + time_actual)
                time_exp_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                             time.gmtime(time_exp))
                self.lista = []
                dicc[USER] = {'IP: ': IP, 'EXPIRES: ': time_exp_str}
                self.lista.append(dicc)
                print('SIP/2.0 200 OK\r\n')
                self.wfile.write(b"SIP/2.0 200 OK\r\n")  # Escritura socket
                if line_client[4] == '0':
                    print('DELETING')
                    del dicc[USER]
                    print(self.lista)
                else:
                    print(self.lista)
        self.register2json()

    def register2json(self):
        with open('registered.json', 'w') as archivo_json:
            json.dump(self.lista, archivo_json, sort_keys=True,
                      indent=4, separators=(',', ':'))


if __name__ == "__main__":

    dicc = {}
    try:
        PORT = int(sys.argv[1])
    except IndexError:
        sys.exit("Debe introducir: server.py port_number")
    """Creamos UDP en el puerto que indicamos utilizando la clase."""
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Iniciando servidor... \r\n")
    try:
        """Creamos el servidor"""
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
