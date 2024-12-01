import threading
import time


def write_words(words_count, file_name):
    file =  open(file_name, 'a', encoding='utf-8')
    for i in range(words_count):
        file.write(f'Какое-то слово № <номер слова по порядку> {i+1}\n ')
        time.sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
res_time_ = end_time - start_time

print(f'Время работы потоков {res_time_}')

start_time = time.time()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'exsample7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

end_time = time.time()
res_time2_ = end_time - start_time

print(f'Время работы потоков {res_time2_}')

print(f'Использование Потоков быстрее функций на {res_time2_-res_time_} секунд')