from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPainter, QBrush, QPen
from PyQt6.QtCore import Qt

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(250, 267)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 101, 31))
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser.setUndoRedoEnabled(False)
        self.textBrowser.setOpenExternalLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 181, 22))
        self.lineEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 90, 101, 31))
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 130, 181, 22))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 230, 121, 21))
        self.label.setObjectName("label")
        self.startConnect = QtWidgets.QPushButton(Dialog)
        self.startConnect.setGeometry(QtCore.QRect(40, 160, 81, 41))
        self.startConnect.setObjectName("startConnect")
        self.resetConnect = QtWidgets.QPushButton(Dialog)
        self.resetConnect.setGeometry(QtCore.QRect(140, 160, 81, 41))
        self.resetConnect.setObjectName("resetConnect")
        self.textBrowser_2.raise_()
        self.textBrowser.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.startConnect.raise_()
        self.resetConnect.raise_()
        self.retranslateUi(Dialog)
        self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
        \u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\
        \u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Login</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LOGIN API</p></body></html>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">соединение:</span></p></body></html>"))
        self.startConnect.setText(_translate("Dialog", "Start"))
        self.resetConnect.setText(_translate("Dialog", "Reset"))

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        # painter.setPen(QPen(Qt.green,  5, Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        painter.drawEllipse( )
        painter.drawEllipse(130, 235, 10, 10)
        painter.end()
