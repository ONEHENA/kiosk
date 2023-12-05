import socket, threading

kiosk_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kiosk_client.connect(("127.0.0.1", 12345))  # 서버 IP 주소와 포트 번호를 지정

# 분류, 제품명, 가격, 제조시간(ms)
order_list = [
    ('coffee', 'americano', '5000', '3000'),
    ('coffee', 'late', '7000', '5000'),
    ('bread', 'cio', '2500', '7000'),
    ('bread', 'morning', '4000', '10000'),
    ('beverage', 'orange juice', '4500', '3000'),
    ('beverage', 'apple juice', '3000', '2000')
]

name = 'kiosk'

def receive():
    while True:
        message = kiosk_client.recv(1024).decode('utf-8')
        if message == 'NAME':
            kiosk_client.send(name.encode('utf-8'))
        else:
            print(message)
        
def write():
    while True:
        c_order = []
        select = 9999
        while True:
            select = int(input('주문 선택(다 고르셨으면 9를 누르세요)'))
            if select == 9:
                break
            ea = int(input('개수 선택'))
            c_order.append((order_list[select-1], ea))

        message = str(c_order)
        kiosk_client.send(message.encode('utf-8'))


# 멀티 클라이언트용 쓰레드
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# 메시지 보내기
write_thread = threading.Thread(target=write)
write_thread.start()