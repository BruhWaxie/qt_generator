# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(259, 169)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 110, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(10, 40, 108, 13))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.password_label.setFont(font)
        self.password_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.password_label.setObjectName("password_label")
        self.numbers_check = QtWidgets.QCheckBox(self.centralwidget)
        self.numbers_check.setGeometry(QtCore.QRect(20, 60, 144, 17))
        self.numbers_check.setObjectName("numbers_check")
        self.symbols_check = QtWidgets.QCheckBox(self.centralwidget)
        self.symbols_check.setGeometry(QtCore.QRect(20, 90, 145, 17))
        self.symbols_check.setObjectName("symbols_check")
        self.generate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generate_btn.setGeometry(QtCore.QRect(160, 120, 91, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.generate_btn.setFont(font)
        self.generate_btn.setStyleSheet("background-color : purple;\n"
"color : white;\n"
"border : 1px solid purple;\n"
"border-radius: 8px;\n"
"")
        self.generate_btn.setObjectName("generate_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор паролів"))
        self.label.setText(_translate("MainWindow", "Генератор паролів"))
        self.password_label.setText(_translate("MainWindow", "Ваш пароль буде тут"))
        self.numbers_check.setText(_translate("MainWindow", "Використовувати числа"))
        self.symbols_check.setText(_translate("MainWindow", "Використовувати букви"))
        self.generate_btn.setText(_translate("MainWindow", "Згенерувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())