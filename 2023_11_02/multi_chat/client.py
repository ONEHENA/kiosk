import socket
import threading

# 서버 ip 주소와 포트 번호 정하기
server_ip = '127.0.0.1'
server_port = 12345

# 서버 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버에 연결 신청
client_socket.connect((server_ip, server_port))

nickname = input('별명을 입력해 주세요. : ')

def receive():
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message == 'NICKNAME':
            client_socket.send(nickname.encode('utf-8'))
        else:
            print(message)
def write():
    while True:
        message = input('할 말 입력 : ')
        client_socket.send(f'{nickname} : {message}'.encode('utf-8'))

threading.Thread(target=receive).start()
threading.Thread(target=write).start()
