import socket, threading

view_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
view_client.connect(("127.0.0.1", 12345))  # 서버 IP 주소와 포트 번호를 지정

name = 'view'

def receive():
    while True:
        message = view_client.recv(1024).decode('utf-8')
        if message == 'NAME':
            view_client.send(name.encode('utf-8'))
        else:
            print(f'{message}번 주문이 완료되었습니다. ')


# 멀티 클라이언트용 쓰레드
receive_thread = threading.Thread(target=receive)
receive_thread.start()