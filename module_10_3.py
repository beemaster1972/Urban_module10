from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            debit = randint(50, 500)
            self.balance += debit
            print(f'Пополнение: {debit}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            kredit = randint(50, 500)
            print(f'Запрос на {kredit}')
            if kredit <= self.balance:
                self.balance -= kredit
                f"Снятие: {kredit}. Баланс: {self.balance}"
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


if __name__ == '__main__':
    bk = Bank()
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(f'Итоговый баланс {bk.balance}')