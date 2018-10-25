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
LINE = sys.argv[3:]  # Método y usuario

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    registersip = ' '.join(LINE)
    if registersip != "":
        if LINE[0] == 'register':
            registersip = 'REGISTER sip:' + LINE[1] + ' SIP/2.0\r\n'  # Método + Usuario
            print("Enviando:", registersip)
        my_socket.send(bytes(registersip, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)
        print('Recibido -- ', data.decode('utf-8'))
    else:
        print('No hay mensaje')

print("Socket terminado.")
