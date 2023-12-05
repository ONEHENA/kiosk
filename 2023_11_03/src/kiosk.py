import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.kiosk import Ui_MainWindow
import socket, threading



class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.ame_spin_box.valueChanged.connect(self.update_total_price)
        self.ui.latte_spin_box.valueChanged.connect(self.update_total_price)
        self.ui.salt_spin_box.valueChanged.connect(self.update_total_price)
        self.ui.morning_spin_box.valueChanged.connect(self.update_total_price)
        self.ui.orange_spin_box.valueChanged.connect(self.update_total_price)
        self.ui.apple_spin_box.valueChanged.connect(self.update_total_price)

        self.ui.push_button.clicked.connect(self.on_button_clicked)

        # 통신 관련 코드
        self.kiosk_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.kiosk_client.connect(("127.0.0.1", 12345))  # 서버 IP 주소와 포트 번호를 지정

        # 분류, 제품명, 가격, 제조시간(ms)
        self.order_list = [
            ('coffee', 'americano', '5000', '3000'),    
            ('coffee', 'latte', '7000', '5000'),
            ('bread', 'salt', '2500', '7000'),
            ('bread', 'morning', '4000', '10000'),
            ('beverage', 'orange juice', '4500', '3000'),
            ('beverage', 'apple juice', '3000', '2000')
        ]

        self.name = 'kiosk'

        # 멀티 클라이언트용 쓰레드
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        # # 메시지 보내기
        # write_thread = threading.Thread(target=self.write)
        # write_thread.start()

    def receive(self):
        while True:
            message = self.kiosk_client.recv(1024).decode('utf-8')
            if message == 'NAME':
                self.kiosk_client.send(self.name.encode('utf-8'))
            else:
                self.ui.service_label.setText(message)
    # def write(self):
    #     # 주문 완료 버튼이 눌렸을 때 데이터를 가져올 수 있도록 변경
    #     while True:
    #         c_order = []
    #         select = 9999
    #         while True:
    #             select = int(input('주문 선택(다 고르셨으면 9를 누르세요)'))
    #             if select == 9:
    #                 break
    #             ea = int(input('개수 선택'))
    #             c_order.append((self.order_list[select-1], ea))

    #         message = str(c_order)
    #         self.kiosk_client.send(message.encode('utf-8'))

    def on_button_clicked(self):
        c_order = []

        # order list의 index
        # 몇 개 갯수
        num_ame = self.ui.ame_spin_box.value()
        if num_ame > 0:
            # 처리
            index = 1
            ea = num_ame
            c_order.append((self.order_list[index-1], ea))
            
        num_latte = self.ui.latte_spin_box.value()
        if num_latte > 0:
            # 처리
            index = 2
            ea = num_latte
            c_order.append((self.order_list[index-1], ea))

        num_salt = self.ui.salt_spin_box.value()
        if num_salt > 0:
            # 처리
            index = 3
            ea = num_salt
            c_order.append((self.order_list[index-1], ea))

        num_morning = self.ui.morning_spin_box.value()
        if num_morning > 0:
            # 처리
            index = 4
            ea = num_morning
            c_order.append((self.order_list[index-1], ea))

        num_orange = self.ui.orange_spin_box.value()
        if num_orange > 0:
            # 처리
            index = 5
            ea = num_orange
            c_order.append((self.order_list[index-1], ea))

        num_apple = self.ui.apple_spin_box.value()
        if num_apple > 0:
            # 처리
            index = 6
            ea = num_apple
            c_order.append((self.order_list[index-1], ea))
        

        # 버튼이 눌리고 마지막에 서버에 데이터를 보내주는 코드
        message = str(c_order)
        self.kiosk_client.send(message.encode('utf-8'))

    def update_total_price(self):
        total = 0

        ame_value = self.ui.ame_spin_box.value()
        ame_price = self.ui.ame_price.text()[:4]
        ame_reslut = ame_value * int(ame_price)
        total += ame_reslut

        latte_value = self.ui.latte_spin_box.value()
        latte_price = self.ui.latte_price.text()[:4]
        latte_reslut = latte_value * int(latte_price)
        total += latte_reslut

        salt_value = self.ui.salt_spin_box.value()
        salt_price = self.ui.salt_price.text()[:4]
        salt_reslut = salt_value * int(salt_price)
        total += salt_reslut

        morning_value = self.ui.morning_spin_box.value()
        morning_price = self.ui.morning_price.text()[:4]
        morning_reslut = morning_value * int(morning_price)
        total += morning_reslut

        orange_value = self.ui.orange_spin_box.value()
        orange_price = self.ui.orange_price.text()[:4]
        orange_reslut = orange_value * int(orange_price)
        total += orange_reslut

        apple_value = self.ui.apple_spin_box.value()
        apple_price = self.ui.apple_price.text()[:4]
        apple_reslut = apple_value * int(apple_price)
        total += apple_reslut

        self.ui.total_price.setText(f'{total} 원')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
#####
