# # Напишите программу на Python, которая будет находить
# # сумму элементов массива из 1000000 целых чисел.
# # � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# # � Массив должен быть заполнен случайными целыми числами
# # от 1 до 100.
# # � При решении задачи нужно использовать многопоточность,
# # многопроцессорность и асинхронность.
# # � В каждом решении нужно вывести время выполнения
# # вычислений.

import random
import threading
import time

summa = 0
random_list = [random.randint(1, 100) for _ in range(1, 1000_000)]
# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def increment(start, stop):
    global summa
    for i in random_list[start:stop]:
        summa += i
    print(f"Значение счетчика: {summa:_}")


threads = []
count_threads = 5

part_size = len(random_list) // count_threads
rest = len(random_list) % count_threads
start = 0
start_time = time.time()
for i in range(count_threads):

    if i < rest:
        stop = start + part_size + 1
    else:
        stop = start + part_size

    t = threading.Thread(target=increment, args=(start, stop))
    threads.append(t)
    t.start()
    start = stop

#
for t in threads:
    t.join()
print(f"Значение счетчика в финале: {summa:_}")
print(f"Время выполнения: {time.time() - start_time}")
