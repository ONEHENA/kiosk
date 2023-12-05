import socket
import threading

# 서버 ip주소와 포트 번호 정하기
server_ip = '127.0.0.1'
server_port = 12345

# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 서버 주소 바인딩
server_socket.bind((server_ip, server_port))
# 연결 대기
server_socket.listen()

# 클라이언트 소켓 관리를 위한 리스트
clinets = []

# 클라이언트의 정보를 확인할 수 있는 리스트
nicknames = []

def broadcast(message):
    for client in clinets:
        client.send(message)

def handler(clinet):
    while True:
        message = clinet.recv(1024)
        broadcast(message)

while True:
    # 연결
    client_socket, client_address = server_socket.accept()
    print(f'{client_address} 클라이언트가 연결되었습니다.')

    # 확인
    client_socket.send('NICKNAME'.encode('utf-8'))
    nickname = client_socket.recv(1024).decode('utf-8')

    clinets.append(client_socket)
    nicknames.append(nickname)

    print(f'클라이언트의 별명은 {nickname} 입니다.')
    broadcast(f'{nickname} 클라이언트가 접속했습니다.'.encode('utf-8'))
    broadcast(f'채팅방에 총 {len(nicknames)}명이 있습니다.'.encode('utf-8'))

    client_socket.send('서버에 연결 되었습니다.'.encode('utf-8'))

    # 접속한 클라이언트를 관리할 수 있는 쓰레드
    threading.Thread(target= handler, args=(client_socket,)).start()

