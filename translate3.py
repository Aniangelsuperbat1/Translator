import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.resize(1000, 1000)

        layout = qtw.QGridLayout()
        self.setLayout(layout)

        Translate_lan = qtw.QLineEdit()
        Translated_lan = qtw.QLineEdit()
        Label_Lan = qtw.QComboBox()
        Label_Translated = qtw.QComboBox()

        Button = qtw.QPushButton("translate")
        Button.clicked.connect(self.close)

        layout.addWidget(Label_Lan, 0, 1)
        layout.addWidget(Label_Translated, 0, 3)
        layout.addWidget(Button, 1, 2)
        layout.addWidget(Translate_lan, 1, 1)
        layout.addWidget(Translated_lan, 1, 3)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
