"""__________lambda функция______________"""

first = 'Мама мыла раму'
second = 'Рамёна мало было'

print(list(map(lambda x, y: x == y, first, second )))

"""___________Замыкание_____________"""

def get_advanced_writer(file_name):
    def write_averything(*data_set):
        with open(file_name, 'a') as file:
            for i in data_set:
                file.write(f'{i}\n')
    return write_averything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в','списке'])

"""_____________ Метод __call__ _________"""
from random import choice

class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да','Нет','Наверное')
print(first_ball())
print(first_ball())
print(first_ball())