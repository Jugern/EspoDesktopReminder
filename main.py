from notifications import Notifications as ntf
import threading, os, sched, time, schedule
import connectServer
import sys, random, secrets
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from dialog import Ui_Dialog
from threading import Thread
# from dotenv import load_dotenv
from pystray import MenuItem as item
from PIL import Image

class WindowsReminder(ntf):

    def print_some_times(self):
        schedule.every(10).seconds.do(self.otp, title='Raz', message='soobshenie')
        while True:
            schedule.run_pending()
            time.sleep(1)

    def noti(self, nachalo='ошибка', text='нет текста'):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.nth = Thread(target=self.print_some_times)
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
        self.reminder = QAction("Reminder")
        self.reminder.triggered.connect(lambda: self.noti())
        self.menu.addAction(self.reminder)
        self.quit = QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)
        self.tray.setContextMenu(self.menu)

    def colorConnect(self, status='не подключен', color='yellow'):
        self.label_2.clear()
        self.label_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:{color};\">{status}</span></p></body></html>")

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    # window.notifWindows()
    window.show()
    app.exec()