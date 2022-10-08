import win10toast

class Notifications():

    def otp(self):
        win10toast.ToastNotifier().show_toast(self.sps[1], self.sps[2])

    def pereborJSON(self):
        for i in self.datacheck.values():
            self.returnLogin = i['login']
            self.returnLoginAPI = i['loginAPI']
            self.timeNotifications = i['time']
            self.textNotifications = i['text']
        self.serviceReminer = self.textNotifications['notifications']
        # pos.append(self.timeNotifications, self.serviceReminer, self.textReminder, self.urlReminder)
        self.textReminder = self.textNotifications['descriptions']
        self.urlReminder = self.textNotifications['url']
        if self.returnLogin == self.login and self.returnLoginAPI == self.loginAPI:
            return [self.timeNotifications, self.serviceReminer, self.textReminder, self.urlReminder]
        else:
            return False