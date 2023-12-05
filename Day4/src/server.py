import socket, threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 20000

server_socket.bind((server_ip, server_port))
server_socket.listen()

clients = {}
order_num = 0
# key : 주문 번호, value : 주문 개수
order_dict = {}

# 키오스크와 관련된 일을 하는 함수
def kiosk_task(order_num, client_socket, order_dict):
    while True:
        message = client_socket.recv(1024).decode('utf-8')

        # 키오스크의 주문 목록 전처리
        message = eval(message)

        # 주문 개수를 세기 위한 코드
        order_dict[order_num] = len(message)
        order_num += 1
        clients['view'].send(f"주문번호 {order_num}번 대기중 입니다.".encode('utf-8'))
        client_socket.send(f"주문번호 {order_num}번 접수 되었습니다.".encode('utf-8'))
        
        

        for item in message:
            order_info, ea = item

            # 해당 머신에게 작업 요청
            s = clients[order_info[0]]
            print(str((order_info, ea, order_num)))
            s.send(str((order_info, ea, order_num)).encode('utf-8'))

        

def coffee_task(client_socket, order_num, order_dict):
    while True:
        message = client_socket.recv(1024).decode('utf-8')        
        if message:
            print(f'{message}번 커피 나왔습니다.')
            if order_dict[order_num] > 1:
                order_dict[order_num] -= 1
            else:
                # 전광판에 완료 신호를 보낸다.
                clients['view'].send(f'주문번호 {message}번 완료되었습니다.'.encode('utf-8'))

def bread_task(client_socket, order_num, order_dict):
    while True:
        message = client_socket.recv(1024).decode('utf-8')        
        if message:
            print(f'{message}번 빵 나왔습니다.')
            if order_dict[order_num] > 1:
                order_dict[order_num] -= 1
            else:
                # 전광판에 완료 신호를 보낸다.
                clients['view'].send(f'주문번호 {message}번 완료되었습니다.'.encode('utf-8'))

def beverage_task(client_socket, order_num, order_dict):
    while True:
        message = client_socket.recv(1024).decode('utf-8')        
        if message:
            print(f'{message}번 음료 나왔습니다.')
            if order_dict[order_num] > 1:
                order_dict[order_num] -= 1
            else:
                # 전광판에 완료 신호를 보낸다.
                clients['view'].send(f'주문번호 {message}번 완료되었습니다.'.encode('utf-8'))

def handler(client_socket, order_num, name, order_dict):    
    if name == 'kiosk':
        kiosk_task(order_num, client_socket, order_dict)
    elif name == 'coffee':
        coffee_task(client_socket, order_num, order_dict)
    elif name == 'bread':
        bread_task(client_socket, order_num, order_dict)
    elif name == 'beverage':
        beverage_task(client_socket, order_num, order_dict)
    

while True:
    print('대기중...')
    client_socket, client_address = server_socket.accept()
    print(f'{client_address} 클라이언트 접속')

    client_socket.send("NAME".encode('utf-8'))
    name = client_socket.recv(1024).decode('utf-8')

    clients[name] = client_socket
    print(f'{client_address} 클라이언트 연결 완료')

    threading.Thread(target=handler, args=(client_socket, order_num, name, order_dict,)).start()