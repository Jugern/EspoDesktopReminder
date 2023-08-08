import sys, threading, time, schedule, functools, os
from notifications import Notifications as ntf
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from dialog import Ui_Dialog
from WindowsReminder import Ui_Form
from threading import Thread
from connectServer import ClientSocket
# from dotenv import load_dotenv

class NewWindowsReminder(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">TEXT</span></p></body></html>")
        self.description.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">DESCRIPTIONS</span></p></body></html>")
        self.linkButton.setText(f"""<a href="LINK">LINK/</a>'""")

    def closeEvent(self, event):
        event.ignore()
        self.hide()

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog, ClientSocket, ntf):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.serverCheckStatus = 0
        self.startCheck = 0
        self.checkStatus = 0
        self.datacheck = {0:0}
        self.serverCheckErrors = str('отключенно')
        self.colors = 'red'
        self.textNotifications = {0:0}
        self.timeNotifications = str()
        self.lostReminder = []
        self.startApp()
        self.w3 = NewWindowsReminder()
        self.w3.show()
        self.w3.hide()
        self.dataToConnect = {'login':0, 'loginAPI':0, 'addres':0, 'port':0}
        self.startButton.clicked.connect(lambda: self.start())
        self.resetButton.clicked.connect(lambda: self.stop())
        self.resetButton.setEnabled(False)

    def start(self):
        self.addres = self.lineAddress.text()
        self.port = self.linePort.text()
        self.login = self.lineLogin.text()
        self.loginAPI = self.lineLoginAPI.text()
        if self.validations():
            print('ne proshlo')
            self.colorDef(text='Неверные данные', color='red')
            return False
        self.startCheck = 1
        self.colorDef(text='соединение', color='#003942')
        self.notifications_and_serversocket()
        self.startButton.setEnabled(False)
        self.resetButton.setEnabled(True)

    def catch_exceptions(cancel_on_failure=False):
        def catch_exceptions_decorator(job_func):
            @functools.wraps(job_func)
            def wrapper(*args, **kwargs):
                try:
                    return job_func(*args, **kwargs)
                except:
                    import traceback
                    print(traceback.format_exc())
                    if cancel_on_failure:
                        return schedule.CancelJob
            return wrapper
        return catch_exceptions_decorator

    def print_some_times(self):
        schedule.every(10).seconds.do(self.connect).tag('start')
        schedule.every(10).seconds.do(self.colorConnect).tag('start')
        schedule.every(1).seconds.do(self.perebor).tag('start')
        # schedule.every(10).seconds.do(self.zapuskNotifications).tag('start')
        # schedule.every(10).seconds.do(self.startApp).tag('start')
        schedule.every(60).seconds.do(self.recheckconnect)
        while True:
            if self.checkStatus == 0:
                schedule.run_pending()
                time.sleep(1)
            else:
                break

    def notifications_and_serversocket(self):
        lock = threading.Lock()
        lock.acquire()
        try:
            if self.checkStatus == 0:
                self.nth = Thread(target=self.print_some_times)
                self.nth.start()
            else:
                print('return lock threading')
                return
        except:
            self.colorDef(text='Ошибка главного потока', color='red')
        finally:
            print('zakrilsya')
            lock.release()

    def closeEvent(self, event):#create tray
        self.icon = QIcon("icon.ico")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)
        self.menu = QMenu()
        self.example = QAction("Show")
        self.example.triggered.connect(self.zapuskWindows)
        self.menu.addAction(self.example)
        self.quits = QAction("Quit")
        self.quits.triggered.connect(self.vse)
        self.menu.addAction(self.quits)
        self.tray.setContextMenu(self.menu)

    def zapuskWindows(self):
        self.tray.setVisible(False)
        self.show()

    def Close(self):
        self.checkStatus = 1
        schedule.clear()
        app.quit()

    def vse(self):
        self.tray.setVisible(False)
        self.close()

    def colorDef(self, text='ошибка', color='red'):
        self.label_2.setText(f"{text}")
        self.label_2.setStyleSheet("QLabel {color: "+f'{color}'+"}")

    @catch_exceptions(cancel_on_failure=True)
    def colorConnect(self):
        self.label_2.setText(f"{self.serverCheckErrors}")
        self.label_2.setStyleSheet("QLabel {color: "+f'{self.colors}'+"}")
        try:
            if self.serverCheckStatus == 0:
                return schedule.CancelJob
        except:
            print('tut oshibka')

    @catch_exceptions(cancel_on_failure=True)
    def connect(self):
        super().connectClientSocket()
        try:
            if self.serverCheckStatus == 0:
                return schedule.CancelJob
        except:
            print('tut oshibka')

    @catch_exceptions(cancel_on_failure=True)
    def recheckconnect(self):
        try:
            if self.serverCheckStatus == 0:
                schedule.clear('start')
                self.colorDef(text='соединение', color='#003942')
                schedule.every(10).seconds.do(self.connect).tag('start')
                schedule.every(10).seconds.do(self.colorConnect).tag('start')
        except:
            schedule.clear('start')
            self.colors = 'red'
            self.serverCheckErrors = 'Ошибка в планировщике'
            self.colorDef()

    def validations(self):
        if self.validationsIP4():
            self.colorDef(text='Ошибка ip адреса', color='red')
            return True
        try:
            self.port = int(self.port)
            if 65534 > self.port > 0:
                pass
            else:
                self.colorDef(text='неправильный порт', color='red')
                return True
        except ValueError:
            self.colorDef(text='неправильный порт', color='red')
            return True
        try:
            if 63 > len(self.login) > 0:
                pass
            else:
                return True
        except:
            return True
        try:
            if 125 > len(self.loginAPI) > 0:
                pass
            else:
                return True
        except:
            return True
        self.dataToConnect.update({'login': self.login, 'loginAPI': self.loginAPI, 'addres': self.addres, 'port': self.port})

    def stop(self):
        self.startButton.setEnabled(True)
        self.resetButton.setEnabled(False)
        self.colorDef(text='отключенно', color='red')
        schedule.clear()
        self.checkStatus = 0

    def perebor(self):
        if int((list(self.datacheck.keys())[0])) == 1:
            self.sps = self.pereborJSON()
            if self.sps == False:
                return
            # self.news()
            self.lostReminder.append(self.sps)
            self.datacheck.clear()
            self.datacheck[0] = 0
        if int((list(self.datacheck.keys())[0])) == 2:
            self.colorDef(text='неправильные данные', color='black')
            schedule.clear()
            self.checkStatus = 1
            return

    def startApp(self):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.nth = Thread(target=self.zapuskNotifications)
            self.nth.start()
        except:
            self.colorDef(text='ошибка в потоке', color='red')
        finally:
            lock.release()

    def zapuskNotifications(self):
        try:
            while True:
                while len(self.lostReminder) > 0:
                    if self.w3.isVisible():
                        time.sleep(5.0)
                        continue
                    else:
                        self.w3.title.setText(
                        f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">{self.lostReminder[0][1]}</span></p></body></html>")
                        self.w3.description.setText(
                        f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">{self.lostReminder[0][2]}</span></p></body></html>")
                        self.w3.linkButton.setText(
                        f"""<a href="{self.lostReminder[0][3]}">{self.lostReminder[0][3]}/</a>'""")
                        self.lostReminder.pop(0)
                        self.w3.show()
                        self.otp()
                time.sleep(5.0)
        except:
            self.colorDef(text='ошибка в данных JSON', color='red')

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())