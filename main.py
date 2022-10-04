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
        self.serverCheckErrors = str('not connect')
        self.colors='blue'
        self.schedConnectTimer=15
        self.schedColorTimer=15

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

    # status = 'не подключен', color = secrets.token_hex(3)

    def print_some_times(self, title='Raz', message='soobshenie'):
        schedule.every(10).seconds.do(self.connect).tag('friend')
        schedule.every(10).seconds.do(self.colorConnect).tag('friend')
        schedule.every(60).seconds.do(self.recheckconnect)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def notifications_and_serversocket(self, nachalo='ошибка', text='нет текста'):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.nth = Thread(target=self.print_some_times, args=('nachalo', 'text'))
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
        self.color = QAction("Color")
        self.color.triggered.connect(lambda: self.colorConnect())
        self.menu.addAction(self.color)
        self.newWindows = QAction("Windows")
        self.newWindows.triggered.connect(lambda: self.news(text='tut', descriptions='netut', link='uru'))
        # self.newWindows.triggered.connect(lambda: self.newWindo())
        self.menu.addAction(self.newWindows)
        self.reminder = QAction("Reminder")
        self.reminder.triggered.connect(lambda: self.notifications_and_serversocket())
        self.menu.addAction(self.reminder)
        self.socketStart = QAction("socketStart")
        self.socketStart.triggered.connect(lambda: self.connect())
        self.menu.addAction(self.socketStart)
        self.quit = QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)
        self.tray.setContextMenu(self.menu)

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
    def connect(self, addres='localhost', port=19000):
        super().connectClientSocket(addres=addres, port=port)
        try:
            if self.serverCheckStatus == 0:
                return schedule.CancelJob
        except:
            print('tut oshibka')

    @catch_exceptions(cancel_on_failure=True)
    def recheckconnect(self):
        try:
            if self.serverCheckStatus == 0:
                schedule.every(self.schedConnectTimer).seconds.do(self.connect).tag('friend')
                schedule.every(self.schedColorTimer).seconds.do(self.colorConnect).tag('friend')
            if self.serverCheckStatus == 1:
                pass
        except:
            print('Ошибка в планировщике')
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    window.show()
    app.exec()