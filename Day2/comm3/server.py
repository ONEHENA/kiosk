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
        # 서버 ip주소와 포트 번호 정하기
        server_ip = '127.0.0.1'
        server_port = 12345
        # 서버 소켓 생성
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 서버 주소 바인딩
        self.server_socket.bind((server_ip, server_port))
        # 연결 대기
        self.server_socket.listen(5)

        threading.Thread(target=self.listener).start()


    def on_button_clicked(self):
        input_text = self.ui.lineEdit.text()
        self.client_socket.send(input_text.encode('utf-8'))
        self.ui.lineEdit.setText('')
        

    def listener(self):
        # 클라이언트 연결 수락
        self.client_socket, client_address = self.server_socket.accept()
        print(f'{client_address}에서 연결이 수락되었습니다. ')

        client_handle = threading.Thread(target= self.handle_client, 
                                         args=(self.client_socket,))
        client_handle.start()
    
    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            self.ui.textBrowser.append(data)                    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())