import time
import threading

## 은행에서 두 개의 창구가 있고
## 1번 창구는 3초에 한명씩 처리
## 2번 창구는 2초에 한명씩 처리

## 손님 리스트 10명
bank_queue = list(range(1, 11))

def bank_1():
    while bank_queue:
        customer = bank_queue.pop(0)
        print(f'{customer}번 손님이 오셨습니다. ')
        time.sleep(3)

def bank_2():
    while bank_queue:
        customer = bank_queue.pop(0)
        print(f'{customer}번 손님이 오셨습니다. ')
        time.sleep(2)

def main():
    # 1, 2번 창구에 손님을 적절하게 넣어주기
    thread1 = threading.Thread(target = bank_1)
    thread2 = threading.Thread(target = bank_2)

    thread1.start()
    thread2.start()

main()