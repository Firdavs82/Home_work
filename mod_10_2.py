import threading
import time




class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies_num = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали')
        while self.enemies_num > 0:
            print(f'{self.name} сражается {self.days}, осталось {self.enemies_num} воинов')
            self.enemies_num -= self.power
            self.days += 1
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

first_knight =Knight('Sir Lanselot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

print(f'Все битвы закончились!')