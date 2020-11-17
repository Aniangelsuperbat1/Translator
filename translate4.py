import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QGridLayout
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "translator"
        left = 500
        top = 500
        width = 500
        height = 500

        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)

        self.button()
        # self.layout_()
        self.Lan_

        self.show()
        # Button = qtw.QPushButton("translate")

    def button(self):
        button_push = QPushButton("translate", self)

    def Lan_(self):
        Translate_lan = QLineEdit()
        Translated_lan = QLineEdit()
        Label_Lan = QLineEdit("Choose Language", self)
        Label_Translated = QLineEdit("Choose Language", self)
        layout = QGridLayout()
        layout.addWidget(Label_Lan, 0, 1)
        layout.addWidget(Label_Translated, 0, 3)
        layout.addWidget(button, 1, 2)
        layout.addWidget(Translate_lan, 1, 1)
        layout.addWidget(Translated_lan, 1, 3)

        self.setLayout(layout)
    # def layout_(self):
    #     layout = QGridLayout()
    #     layout.addWidget(Label_Lan, 0, 1)
    #     layout.addWidget(Label_Translated, 0, 3)
    #     layout.addWidget(button, 1, 2)
    #     layout.addWidget(Translate_lan, 1, 1)
    #     layout.addWidget(Translated_lan, 1, 3)

    #     self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
