from PyQt6 import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(839, 417)
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(30, 20, 781, 41))
        self.title.setObjectName("title")
        self.description = QtWidgets.QLabel(Form)
        self.description.setGeometry(QtCore.QRect(20, 70, 801, 251))
        self.description.setObjectName("description")
        self.linkButton = QtWidgets.QCommandLinkButton(Form)
        self.linkButton.setEnabled(True)
        self.linkButton.setGeometry(QtCore.QRect(30, 350, 781, 48))
        self.linkButton.setObjectName("linkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Текст ТИТЛЕ</span></p></body></html>"))
        self.description.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Дескриптион</span></p></body></html>"))
        self.linkButton.setText(_translate("Form", "ССылка на событие"))
