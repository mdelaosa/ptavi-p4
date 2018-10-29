#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Class and main program for a server."""

import socketserver
import sys
import time
import json


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """Echo server class."""

    def json2register(self):
        try:
            with open('registered.json', 'r') as archivo_json:
                self.dicc = json.load(archivo_json)
        except:
            pass

    def register2json(self):
        """Create json file."""
        with open('registered.json', 'w') as archivo_json:
            json.dump(self.list, archivo_json, sort_keys=True,
                      indent=4, separators=(',', ':'))

    def handle(self):
        """Handle method of the server class."""
        while 1:
            line = self.rfile.read()  # Leyendo lo que envia el cliente.
            line_client = line.decode('utf-8').split()
            if not line:
                break  # Termina el bucle
            else:
                print("Petición recibida \r\n")
            if line_client[0] == 'REGISTER':
                direction = line_client[1].split(':')
                user = direction[1]
                ip = self.client_address[0]
                expires = int(line_client[4])
                time_actual = int(time.time())
                time_actual_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                                time.gmtime(time_actual))
                time_exp = int(expires + time_actual)
                time_exp_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                             time.gmtime(time_exp))
                self.list = []
                dicc[user] = {'IP': ip, 'EXPIRES': time_exp_str}
                self.list.append(dicc)

                print('SIP/2.0 200 OK\r\n')
                self.wfile.write(b"SIP/2.0 200 OK\r\n")  # Escritura socket
                if line_client[4] == '0':
                    print('DELETING')
                    del dicc[user]
                    print(self.list)
                else:
                    print(self.list)
                if time_actual_str >= time_exp_str:
                    del dicc[user]
        self.register2json()


    def removeclient(self):
        """Delete client once it has expired."""




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
