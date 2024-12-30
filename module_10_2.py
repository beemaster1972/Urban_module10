from threading import Thread, current_thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int, enemies: int = 100):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = enemies
        self.days_in_battle = 0

    def battle(self):
        while self.enemies:
            self.enemies -= self.power if self.enemies >= self.power else self.enemies
            self.days_in_battle += 1
            print(f'{self.name} сражается {self.days_in_battle}-й день..., осталось {self.enemies} воинов')
            sleep(1)

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.battle()
        print(f'{self.name} одержал победу спустя {self.days_in_battle} дней(дня)!')


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    second_knight.join()
    while first_knight.is_alive() or second_knight.is_alive():
        pass
    print('Все битвы закончились!')
