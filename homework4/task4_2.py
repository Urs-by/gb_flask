import multiprocessing
import time
import random

random_list = [random.randint(1, 100) for _ in range(1, 1000000)]
# print(random_list)

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,10]

summa = multiprocessing.Value('i', 0)


def increment(sm, start, stop):
    for i in random_list[start:stop]:
        with sm.get_lock():
            sm.value += i
    print(f"Значение счетчика: {sm.value:_}")


count_process = 5
part_size = len(random_list) // count_process
rest = len(random_list) % count_process
start = 0

if __name__ == '__main__':
    start_time = time.time()
    processes = []
    for i in range(count_process):
        if i < rest:
            stop = start + part_size + 1
        else:
            stop = start + part_size
        p = multiprocessing.Process(target=increment, args=(summa, start, stop))
        processes.append(p)
        p.start()
        start = stop

    for p in processes:
        p.join()

    print(f"Итоговон значение счетчика: {summa.value:_}")
    print(f"Время выполнения: {time.time() - start_time}")
