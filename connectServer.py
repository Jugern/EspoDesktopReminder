import socket
import json
from contextlib import closing

class ClientSocket():
    def connectClientSocket(self, data={'0':'0'}):
    # def connectClientSocket(self, addres='localhost', port=19000, data={'0':'0'}):
        # self.addres = addres
        # self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (self.addres, self.port)
        self.serverCheckStatus = 1
        # print('Подключено к {} порт {}'.format(*self.server_address))
        try:
            self.sock.connect(self.server_address)
        except:
            self.serverCheckStatus = 0
            self.serverCheckErrors = 'невозможно подключиться'
            self.colors = 'red'
        try:
            mess = {"0": {"login": 'data', "ipaddress": "192.168.7.6", "comment": "АдминистраторСервер",
                             "command": "discovery"}}
            raw_data = json.dumps(self.dataToConnect).encode()
            self.sock.sendall(raw_data)
            amount_received = 0
            amount_expected = 12
            self.serverCheckErrors = 'подключено'
            self.colors = 'green'
            while amount_received < amount_expected:
                data = self.sock.recv(1024)
                amount_received += 12
                mess = json.loads(data)
                print(f'Получено: {mess}')
        except:
            if self.serverCheckStatus==1:
                self.colors = 'black'
                self.serverCheckErrors = 'Ошибка соединения'
                print('Ошибка соединения')
        finally:
            if self.serverCheckStatus==1:
                self.colors = 'green'
                self.serverCheckErrors = 'Подключено'
                self.sock.close()
            if self.serverCheckStatus==0:
                self.sock.close()

    def checkConnections(self):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((self.addres, self.port)) == 0:
                return "Port is open"
            else:
                return "Port is not open"

# zapusk = ClientSocket()
# zapusk.connections(addres='localhost', port=19000)