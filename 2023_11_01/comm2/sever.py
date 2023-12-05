import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8') # 1024 byte(한글로는 500자정도)를 받아오겠다
        
        #받아온 데이터가 없으면 연결을 종료
        if not data:
            break
        print(f'클라이언트가 보낸 메세지 : {data}')

    client_socket.close()

# 서버 ip 주소와 포트 번호 정하기
sever_ip = '127.0.0.1'
sever_port = 12345


# 서버 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버 주소 바인딩
server_socket.bind((sever_ip, sever_port))

# 연결 대기
server_socket.listen(5) # 클라이언트를 최소 5명까지 받을 수 있다.


# 클라이언트 연결 수락
client_socket, client_address = server_socket.accept()
print(f'{client_address}에서 연결이 수락되었습니다. ')

client_handle = threading.Thread(target = handle_client, args = (client_socket,))
client_handle.start()

while True:
    response = input('클라이언트에게 보낼 메세지 : ')

    #받아온 데이터가 없으면 연결을 종료
    if response.lower() == 'exit':
        break

    client_socket.send(response.encode('utf-8'))
    
server_socket.close()