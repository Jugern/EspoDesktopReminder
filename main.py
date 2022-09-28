import pystray
import tkinter as tk
from notifications import Notifications as ntf
import notifications
import threading, os, sched, time, schedule
import connectServer
import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from dialog import Ui_Dialog
from threading import Thread
# from dotenv import load_dotenv
from pystray import MenuItem as item
from PIL import Image

class WindowsReminder():

    def noti(self, nachalo='tut', text='netut'):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.thm = Thread(target=ntf.otp, args=(str(nachalo), str(text)))
            self.thm.start()
        finally:
            lock.release()

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
        self.reminder = QAction("Reminder")
        self.reminder.triggered.connect(self.noti)
        self.menu.addAction(self.reminder)
        self.quit = QAction("Quit")
        self.quit.triggered.connect(app.quit)
        self.menu.addAction(self.quit)
        self.tray.setContextMenu(self.menu)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    window.show()
    app.exec()