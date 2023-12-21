import multiprocessing
import time

from ran_list import random_list, split_list

count_process = 5

result_list = split_list(random_list, count_process)

summa = multiprocessing.Value('i', 0)


def increment(sm, part_list: list):
    for i in part_list:
        with sm.get_lock():
            sm.value += i
    print(f"Значение счетчика: {sm.value:_}")


if __name__ == '__main__':
    start_time = time.time()
    processes = []
    for i in range(count_process):
        p = multiprocessing.Process(target=increment, args=(summa, result_list[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Итоговон значение счетчика: {summa.value:_}")
    print(f"Время выполнения: {time.time() - start_time}")
