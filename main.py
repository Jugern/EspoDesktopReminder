from notifications import Notifications as ntf
import threading, os, sched, time, schedule
import connectServer
import sys, random, secrets
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from dialog import Ui_Dialog
from WindowsReminder import Ui_Form
from threading import Thread
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


class WindowsReminder(ntf):
    def print_some_times(self, title='Raz', message='soobshenie'):
        schedule.every(10).seconds.do(self.otp, title=title, message=message)
        # schedule.every(10).seconds.do(self.showRiminder, text='tutru', descriptions='retre')
        while True:
            schedule.run_pending()
            time.sleep(1)

    def notifications_and_serversocket(self, nachalo='ошибка', text='нет текста'):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.nth = Thread(target=self.print_some_times, args=('nachalo', 'text'))
            self.nth.start()
            # self.thm = Thread(target=ntf.otp, args=(self, nachalo, text))
            # self.thm.start()
        finally:
            lock.release()

# class ConnecToWindows():

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog, WindowsReminder):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


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
        self.quit = QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)
        self.tray.setContextMenu(self.menu)

    def colorConnect(self, status='не подключен', color=secrets.token_hex(3)):
        self.label_2.clear()
        self.label_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#{color};\">{status}</span></p></body></html>")

    def news(self, text='tet', descriptions='zes', link='lis'):
        self.w2 = NewWindowsReminder(text=text, descriptions=descriptions, link=link)
        self.w2.show()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    # window.notifWindows()
    window.show()
    app.exec()