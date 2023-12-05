import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui import Ui_MainWindow

import socket
import threading

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_button_clicked)

        
        # socket 관련 코드
        client_ip = '127.0.0.1'
        client_port = 12345

        # 클라이언트 소켓 생성
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #서버에 연결
        self.client_socket.connect((client_ip, client_port))
    
    def on_button_clicked(self):
        input_text = self.ui.lineEdit.text()
        self.client_socket.send(input_text.encode('utf-8'))
        self.ui.lineEdit.setText('')

    def receive_data(self, client_socket):
        while True:
            # 서버에서 응답 받기
            data = client_socket.recv(1024).decode('utf-8')
            self.ui.textBrowser.append(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show() 
    sys.exit(app.exec_())