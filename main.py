import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, \
    QLineEdit, QFileDialog, QGroupBox, QRadioButton, QTextEdit, \
    QStatusBar, QLabel, QVBoxLayout, QPushButton, QComboBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QLibraryInfo
from PolardShtrasen import find_Poly , str_Poly


class help(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("help")
        self.resize(600, 500)
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.textEdit.setText("Программа предназначена для разложения числа на простые множители\n ")


class about(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("about")
        self.resize(400, 200)
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 400, 200))
        self.textEdit.setText("Студент Таранов Алексей\n"
                              "группа М8О-113М-19")


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("Polard-Shtrasen")
        self.resize(450, 300)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.name_layout = QLabel(self)
        self.name_layout.setText("введите число:")
        self.name_layout.setGeometry(20,0,200,100)

        self.textbox_input = QLineEdit(self)
        self.textbox_input.move(20, 70)
        self.textbox_input.resize(280, 40)

        self.textbox_output = QLineEdit(self)
        self.textbox_output.move(20, 200)
        self.textbox_output.resize(280, 40)

        self.button = QPushButton('найти', self)
        self.button.move(20, 130)

        self.helpBox = QComboBox(self)
        self.helpBox.addItems(["help", "about"])
        self.helpBox.activated.connect(self.selectionchangehelp)
        self.helpBox.setGeometry(QtCore.QRect(350, 0, 100, 25))
        self.helpBox.setObjectName("helpBox")

        # pIntValidator = QIntValidator(self)
        # pIntValidator.setRange(1, 10000000000)
        # self.textbox_input.setValidator(pIntValidator)

        self.button.clicked.connect(self.on_click)
        # self.initUI()

        self.show()

    def on_click(self):
        shost = self.textbox_input.text()
        # print(find_Poly(int(shost)))
        # print('Clicked!')
        print(shost)
        if shost[0]=='-':
            shost=shost[1:]
            if shost.isdigit():
                if (int(shost) == 0):
                    self.textbox_output.setText("0")
                elif (int(shost)==1):
                    self.textbox_output.setText("-1")
                else:
                    self.textbox_output.setText("-"+str_Poly(find_Poly(int(shost))))
            else:
                self.showMessageBox("ошибка", "введите число")
        else:
            if shost.isdigit():
                if (int(shost)==0):
                    self.textbox_output.setText("0")
                elif (int(shost)==1):
                    self.textbox_output.setText("1")
                else:
                    self.textbox_output.setText(str_Poly(find_Poly(int(shost))))
            else:
                self.showMessageBox("ошибка", "введите число")


    def selectionchangehelp(self, i):
        if i == 0:
            self.h = help()
            self.h.show()
        if i == 1:
            self.a = about()
            self.a.show()


    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        # msgBox.setIcon(QtWidgets.QMessageBox.warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
