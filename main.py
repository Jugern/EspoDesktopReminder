from notifications import Notifications as ntf
import threading, os, sched, time, schedule, functools
import connectServer
import sys, random, secrets
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from dialog import Ui_Dialog
from WindowsReminder import Ui_Form
from threading import Thread
from connectServer import ClientSocket
# from dotenv import load_dotenv
from pystray import MenuItem as item
from PIL import Image

class NewWindowsReminder(QWidget, Ui_Form):
    def __init__(self, *args, text='text', descriptions='descriptions', link='link', **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.text = text
        self.descriptions = descriptions
        self.link = link
        self.title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">{self.text}</span></p></body></html>")
        self.description.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">{self.descriptions}</span></p></body></html>")
        self.linkButton.setText(f"{self.link}")


# class WindowsReminder(ntf):


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog, ClientSocket, ntf):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.serverCheckStatus = 0
        self.startCheck = 0
        self.serverCheckErrors = str('отключенно')
        self.colors='red'
        self.dataToConnect = {'login':0, 'loginAPI':0, 'addres':0, 'port':0}
        self.startButton.clicked.connect(lambda: self.start())
        self.resetButton.clicked.connect(lambda: self.stop())
        self.resetButton.setEnabled(False)

    def start(self):
        self.addres = self.lineAddress.text()
        self.port = self.linePort.text()
        self.login = self.lineLogin.text()
        self.loginAPI = self.lineLoginAPI.text()
        try:
            self.port = int(self.port)
        except ValueError:
            self.colorDef(text='неправильные данные', color='red')
            return
        if self.validations():
            print('ne proshlo')
            return
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
        schedule.every(60).seconds.do(self.recheckconnect)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def notifications_and_serversocket(self, nachalo='ошибка', text='нет текста'):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.nth = Thread(target=self.print_some_times)
            self.nth.start()
        finally:
            lock.release()

    def closeEvent(self, event):#create tray
        self.icon = QIcon("icon.ico")
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)
        self.menu = QMenu()
        self.example = QAction("Show")
        self.example.triggered.connect(self.show)
        self.menu.addAction(self.example)
        self.quit = QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)
        self.tray.setContextMenu(self.menu)

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

    def news(self, text='tet', descriptions='zes', link='lis'):
        self.w2 = NewWindowsReminder(text=text, descriptions=descriptions, link=link)
        self.w2.show()

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
        pass

    def stop(self):
        self.startButton.setEnabled(True)
        self.resetButton.setEnabled(False)
        self.colorDef(text='отключенно', color='red')
        schedule.clear()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    window.show()
    app.exec()