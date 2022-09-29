import win10toast

class Notifications():

    def otp(self, title='title', message='sets'):
        win10toast.ToastNotifier().show_toast(title, message)

