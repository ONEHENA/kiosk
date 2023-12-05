import socket, threading
import time

beverage_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
beverage_client.connect(("127.0.0.1", 20000))  # 서버 IP 주소와 포트 번호를 지정

name = 'beverage'

def make_coffee(order_info, ea, order_num):
    _, p_name, _, p_time = order_info

    for i in range(ea):
        time.sleep(int(p_time)//1000)
        print(f'{order_num}번 주문 {p_name} {i+1}개 완성')
    

def receive():
    while True:
        message = beverage_client.recv(1024).decode('utf-8')
        if message == 'NAME':
            beverage_client.send(name.encode('utf-8'))
        else:
            print(message)
            # 사용할 수 있는 상태로 전처리
            message = eval(message)
            order_info, ea, order_num = message

            # 주문을 처리하는 코드
            make_coffee(order_info, ea, order_num)

            # 음료가 다 완성되었으니 완성 메세지를 서버에 보내기
            beverage_client.send(str(order_num).encode('utf-8'))
        
# 멀티 클라이언트용 쓰레드
receive_thread = threading.Thread(target=receive)
receive_thread.start()
