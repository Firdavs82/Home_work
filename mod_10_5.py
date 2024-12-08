import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line)



if __name__ == '__main__':
    files = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for name in files:
        read_info(name)
    end_time = datetime.now()
    print(end_time - start_time, '(линейный)')


    start_time2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    end_time2 = datetime.now()
    time_of_multiprocessing = end_time2 - start_time2
    print(f'Время работы мультипроцесса : {time_of_multiprocessing}')
