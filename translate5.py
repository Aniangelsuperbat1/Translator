import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        closeapp = QAction(
            QIcon(r"C:\Users\ZhenP\OneDrive\Desktop\Translator\file.png"), "&Quit", self)
        closeapp.setShortcut("Ctrl+Q")
        closeapp.triggered.connect(qApp.quit)

        self.statusBar()

        MainMenu = self.menuBar()
        fileMenu = MainMenu.addMenu("&File")
        fileMenu.addAction(closeapp)
        # submenus
        # filemenu.addAction(QIcon(r"C:\Users\ZhenP\OneDrive\Desktop\Translator\file.png"),("submenu-1").setShortcut("Ctrl+f")
        # filemenu.addAction("submenu-2")

        # if you want to add more menu elements
        # fileMenu = MainMenu.addMenu("&view")

        self.home()

    def home(self):
        self.setGeometry(0, 0, 900, 500)
        self.setWindowTitle("translate")

        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)

        # self.button()
        # self.labels()

        self.show()

    # def button(self):
    #     button_one = QPushButton("translate", self)
    #     button_one.move(600, 200)
    #     button_one.clicked.connect(self.quit_app)

    # def labels(self):
    #     lbl_1 = QLineEdit("language", self)
    #     lbl_1.move(500, 200)
    #     lbl_1.setGeometry(100, 100, 100, 100)

    # def quit_app(self):
    #     sys.exit()


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.create_layout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def create_layout(self):
        self.groupBox = QGroupBox("pick your card")
        gridlayout = QGridLayout()

        button_one = QPushButton("translate", self)
        button_one.setGeometry(20, 20, 20, 20)
        button_two = QPushButton("translate", self)

        gridlayout.addWidget(button_one, 0, 0)
        gridlayout.addWidget(button_two, 0, 1)

        self.groupBox.setLayout(gridlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
