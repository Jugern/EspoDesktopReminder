import socket
# import sys
import json
from contextlib import closing

class ConnectionsBase():
    def __init__(self, addres, port):
        self.addres = addres
        self.port = port

class CheckConnection(ConnectionsBase):
    def check(self):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((self.addres, self.port)) == 0:
                return "Port is open"
            else:
                return "Port is not open"

class ClientSocket(ConnectionsBase):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.addres, self.port)
        print('Подключено к {} порт {}'.format(*self.server_address))
        self.sock.connect(self.server_address)

    def connections(self):
        try:
            mess = {"data": {"hostname": "192.168.7.6", "ipaddress": "192.168.7.6", "comment": "АдминистраторСервер",
                             "command": "discovery"}}
            raw_data = json.dumps(mess).encode()
            self.sock.sendall(raw_data)
            amount_received = 0
            amount_expected = 12
            while amount_received < amount_expected:
                data = self.sock.recv(1024)
                amount_received += 12
                mess = json.loads(data)
                print(f'Получено: {mess}')

        finally:
            print('Закрываем сокет')
            self.sock.close()

zapusk = ClientSocket()
zapusk.connections()