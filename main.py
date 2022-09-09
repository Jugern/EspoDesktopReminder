import pystray
import tkinter as tk
import notifications
import threading
from threading import Thread
from pystray import MenuItem as item
from PIL import Image

class WindowsReminder():

    def __init__(self):
        self.notifications = notifications.Notifications()
        self.window = tk.Tk()
        self.window.title("Title")
        self.frameAccount = tk.Frame(master=self.window)
        self.lbl_Account = tk.Label(master=self.frameAccount, text='Данные для подключения', width=35, height=3)
        self.lbl_Login = tk.Label(master=self.frameAccount, text='Логин', width=35, height=2)
        self.lbl_Password = tk.Label(master=self.frameAccount, text='Пароль', width=35, height=2)
        self.entryLogin = tk.Entry(master=self.frameAccount)
        self.entryPassword = tk.Entry(master=self.frameAccount)
        self.buttonEnter = tk.Button(master=self.frameAccount, text='подключение', width=15, height=2)
        self.frameStatus = tk.Frame(master=self.window)
        self.lbl_Status = tk.Label(master=self.frameStatus, text='Статус соединения :', width=25, height=2)
        self.lbl_StatusData = tk.Label(master=self.frameStatus, text='отключено', width=10, height=2)
        self.frameAccount.pack(fill=tk.BOTH, expand=True)
        self.frameStatus.pack(fill=tk.BOTH, expand=True)
        self.lbl_Account.pack()
        self.entryLogin.pack()
        self.lbl_Login.pack()
        self.entryPassword.pack()
        self.lbl_Password.pack()
        self.buttonEnter.pack()
        self.lbl_Status.grid(row=6, column=0, sticky=tk.E)
        self.lbl_StatusData.grid(row=6, column=1)

    def createNewNotifications(self, text='ZAD'):
        self.windowNoti = tk.Tk()
        self.windowNoti.title("Title")
        self.frame = tk.Frame(master=self.windowNoti)
        self.labelExample = tk.Label(master=self.frame, text=f'{text}', width=100, height=30)
        self.frame.pack()
        self.labelExample.pack()
        self.windowNoti.mainloop()
        self.windowNoti.quit()

    def quit_window(self, icon, item):
        icon.stop()
        self.window.destroy()

    def show_window(self, icon, item):
        icon.stop()
        self.window.after(0, self.window.deiconify)

    def noti(self, item):
        lock = threading.Lock()
        lock.acquire()
        try:
            self.thm = Thread(target=self.notifications.otp, args=('tut', 'netut',))
            self.thm.start()
        finally:
            self.createNewNotifications()
            lock.release()
            self.windowNoti.quit()

    def withdraw_window(self):
        self.window.withdraw()
        image = Image.open("icon.ico")
        menu = (item('Show', self.show_window), item('noti', self.noti), item('Quit', self.quit_window))
        icon = pystray.Icon("name", image, "title", menu)
        icon.run()

    def startWindows(self):
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.mainloop()

zet = WindowsReminder()
zet.startWindows()
