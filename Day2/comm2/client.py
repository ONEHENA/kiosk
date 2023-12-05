import socket
import threading

def receive_data(client_socket):
    while True:
        # 서버에서 응답 받기
        data = client_socket.recv(1024).decode('utf-8')
        # 받아온 데이터가 없으면 연결을 종료
        if not data:
            break
        print(f'서버에서 온 메세지 : {data}')

# 주소, 포트
client_ip = '127.0.0.1'
client_port = 12345

# 클라이언트 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결
client_socket.connect((client_ip, client_port))

recive_handle = threading.Thread(target= receive_data, args=(client_socket,))
recive_handle.start()

while True:
    message = input('서버에게 보낼 메시지 :')
    if message.lower() == 'exit':
        break
    # 메세지를 서버로 전송
    client_socket.send(message.encode('utf-8'))

client_socket.close()