import socket, threading
import time
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.view import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.view_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.view_client.connect(("127.0.0.1", 20000))  # 서버 IP 주소와 포트 번호를 지정

        self.name = 'view'

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def receive(self):
        wait_string = ''
        complete_string = ''

        while True:

            message = self.view_client.recv(1024).decode('utf-8')
            if message == 'NAME':
                self.view_client.send(self.name.encode('utf-8'))
            else:
                # message 안에 완료, 대기
                if '대기' in message:
                    # 대기 번호 쪽으로 텍스트 보여주기
                    # 번
                    order_num = message[5]
                    wait_string += order_num + ' '
                    self.ui.lineEdit.setText(wait_string)
                    
                else:
                    # 완료 번호 쪽으로 텍스트 보여주기  
                    # 번
                    order_num = message[5]
                    
                    wait_string = wait_string.replace(order_num + ' ', '')
                    self.ui.lineEdit.setText(wait_string)

                    complete_string += order_num + ' '
                    self.ui.lineEdit_2.setText(complete_string)
                 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())