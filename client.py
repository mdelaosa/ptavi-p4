#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = sys.argv[1]  # IP del Servidor
PORT = int(sys.argv[2])  # Puerto en el que ejecuta
METHOD = str.upper(sys.argv[3])  # Método
USER = sys.argv[4]  # Usuario

REGISTERSIP = METHOD + ' sip:' + USER + ' SIP/2.0\r\n'  # Método + Usuario

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", REGISTERSIP)
    my_socket.send(bytes(METHOD, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
