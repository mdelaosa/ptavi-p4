#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    SERVER, PORT, METHOD, USER, EXVAL = sys.argv[1:]
except ValueError:
    sys.exit('INSERT: SERVER, PORT, METHOD, USER AND EXVAL')
REGISTER = 'REGISTER sip:' + USER + ' SIP/2.0\nEXPIRES: ' + EXVAL + '\r\n\r\n'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, int(PORT)))
    my_socket.send(bytes(REGISTER, 'utf-8') + b'\r\n')
    try:
        data = my_socket.recv(1024).decode('utf-8')
        print('RECEIVED -- ', data)
    except ConnectionRefusedError:
        print('CONNECTION ERROR')

print("Socket terminado.")
