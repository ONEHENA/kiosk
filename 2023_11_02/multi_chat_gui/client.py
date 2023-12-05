import socket
import threading

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.ui.pushButton.clicked.connect(self.on_button_clicked)


        # 서버 ip 주소와 포트 번호 정하기
        server_ip = '127.0.0.1'
        server_port = 12345

        # 서버 소켓 생성
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 서버에 연결 신청
        self.client_socket.connect((server_ip, server_port))

        self.nickname = input('별명을 입력해 주세요. : ')

        threading.Thread(target=self.receive).start()

    def on_button_clicked(self):
        input_text = self.ui.lineEdit.text()
        self.client_socket.send('f{self.nickname} : {input_text}'.encode('utf-8'))
        self.ui.lineEdit.setText('')
    
    def receive(self):
        while True:
            message = self.client_socket.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                self.client_socket.send(self.nickname.encode('utf-8'))
            else:
                self.ui.textBrowser.append(message)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())