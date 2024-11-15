team1 = 'Мастера кода'
team2 = ('Волшебники данных')



def number(team1_num = 0, team2_num = 0): # Использование %
    print('В команде  "Мастер кода" участников  %s! \nВ команде "Волшебники данных" учаников %s! ' % (team1_num, team2_num))
    print('Итого сегодня участников: %s и %s!' % (team1_num, team2_num))

score1 = 0
score2 = 0

def time(team1_time = 0,team2_time = 0):
    time1 = team1_time
    time2 = team2_time
    print('Команда "{}"  решила задач:{}!\nКоманда "{}" решила задач: {}!'.format(team2,score2,team1,score1))
    print('"{}" решили задачу за {} сек.\n"{}" решили задачу за {} сек.'.format(team2,time2,team1,time1))

def challenge_result(tasks_total, time_avg):
    print(f'Сегодня было решено {tasks_total}, в среднем за {time_avg} секунд на задачу!')
    if score1 > score2 :
        print(f'Победа команды: "{team1}"!')
    elif score1 < score2:
        print(f'Победа команды: "{team2}"!')
    else:
        print('Ничью')

number(team1_num = 5, team2_num = 6)
score1 = 40
score2 = 42
time(team1_time=1552.512,team2_time=2153.3451 )
challenge_result(tasks_total=82, time_avg=45.2)

