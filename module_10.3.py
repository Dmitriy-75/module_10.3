import threading
from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = int(0)
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            num_plus = randint(50,500)
            self.balance += num_plus
            print(f'Пополнение: {num_plus}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            num_minus = randint(50,500)
            print(f'Запрос на {num_minus}')
            if self.balance > num_minus:
                self.balance -= num_minus
                print(f'Снятие: {num_minus}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')











