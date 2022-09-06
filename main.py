from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk

class WindowsReminder():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Title")

    def quit_window(self, icon, item):
        icon.stop()
        self.window.destroy()

    def show_window(self, icon, item):
        icon.stop()
        self.window.after(0, self.window.deiconify)

    def withdraw_window(self):
        self.window.withdraw()
        image = Image.open("icon.ico")
        menu = (item('Show', self.show_window), item('Quit', self.quit_window))
        icon = pystray.Icon("name", image, "title", menu)
        icon.run()

    def startWindows(self):
        self.window.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.window.mainloop()

zet = WindowsReminder()
zet.startWindows()