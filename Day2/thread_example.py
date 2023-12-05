import threading

# thread 기본
# def sample_function_1():
#     for i in range(5):
#         print(i)

# def sample_function_2():
#     for i in range(5):
#         print(i)

# thread1 = threading.Thread(target = sample_function_1)
# thread2 = threading.Thread(target = sample_function_2)

# thread1.start()
# thread2.start()

# 매개변수를 입력으로 받는 thread

def print_number(start, end):
    for i in range(start, end + 1):
        print(i)

thread1 = threading.Thread(target = print_number, args = (1, 5))
thread2 = threading.Thread(target = print_number, args = (6, 10))

thread1.start()
thread2.start()

# 두 개의 쓰레드를 만들고 하나의 
# 함수는 hello를 5번 출력하는 기능,
# 다른 함수는 hi를 5번 출력하는 기능을
# 동시에 실행시키세요.

def sample_function_1():
    for i in range(5):
        print("hello")

def sample_function_2():
    for i in range(5):
        print("hi")

thread1 = threading.Thread(target = sample_function_1)
thread2 = threading.Thread(target = sample_function_2)

thread1.start()
thread2.start()