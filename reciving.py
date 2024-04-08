import socket
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


def getData():
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    string = ("received message: %s" % data)
    return string

#while True:
#    data, addr = getData()
#    print("received message: %s" % data)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi")
        self.TextBox = QLabel("pineapple")
        self.setCentralWidget(self.TextBox)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.UpdateTimer)
        self.timer.start()
    
    def UpdateTimer(self):
        self.TextBox.setText(getData())


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()