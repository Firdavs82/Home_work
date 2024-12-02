import threading
import time
import random


class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            top_in_up = random.randint(50, 500)
            self.balance += top_in_up
            print(f'Пополнение: {top_in_up}. Баланс: {self.balance}.')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            take_off = random.randint(50,500)
            print(f'Запрос на {take_off}')
            if self.balance >= take_off:
                self.balance -= take_off
                print(f'Снятие: {take_off}. Баланс: {self.balance}')
            else:
                print(f'запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk, ))
th2 = threading.Thread(target=Bank.take, args=(bk, ))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')