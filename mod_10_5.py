import multiprocessing
from datetime import datetime
import codecs

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf_8_sig') as file:
        for line in file:
            all_data.append(line)



if __name__ == '__main__':
    filenames = [f'./file{number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for i in filenames:
        read_info(i)
    end_time = datetime.now()
    print(end_time - start_time, '(линейный)')


    start_time2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end_time2 = datetime.now()
    time_of_multiprocessing = end_time2 - start_time2
    print(f'Время работы мультипроцесса : {time_of_multiprocessing}')
