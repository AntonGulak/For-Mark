import threading, time


def kernel(s):
    global norma
    while True:
        value = -4
        norma += value
        print(f'\n{s} изменил значение реактора на {value}, реактора: {norma}')
        time.sleep(1)


def reactor(s):
    global norma
    while True:
        value = 5
        norma += value
        print(f'\n{s} изменила значение реактора на {value}, реактора: {norma}')
        time.sleep(1)


def human(s):
    global norma
    while True:
        try:
            value = int(input())
        except:
            value = norma
        else:
            norma = b
        print(f'{s} заменил значение реактора на {abs(value)}, реактора: {norma}')


if __name__ == "__main__":
    norma = 1000
    thread1 = threading.Thread(target=kernel, args=('Стержень',)).start()
    thread2 = threading.Thread(target=reactor, args=('Реакция',)).start()
    thread3 = threading.Thread(target=human, args=('Оператор',)).start()