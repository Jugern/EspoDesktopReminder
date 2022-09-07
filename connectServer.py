import socket
# import sys
import json

class SocketServer():
    def connections(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 19000)
        print('Подключено к {} порт {}'.format(*server_address))
        sock.connect(server_address)

        try:
            mess = {"data": {"hostname": "192.168.7.6", "ipaddress": "192.168.7.6", "comment": "АдминистраторСервер",
                             "command": "discovery"}}
            raw_data = json.dumps(mess).encode()
            sock.sendall(raw_data)
            amount_received = 0
            amount_expected = 12
            while amount_received < amount_expected:
                data = sock.recv(1024)
                amount_received += 12
                mess = json.loads(data)
                print(f'Получено: {mess}')

        finally:
            print('Закрываем сокет')
            sock.close()
zapusk = SocketServer()
zapusk.connections()