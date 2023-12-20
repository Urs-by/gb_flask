import asyncio
import random
import time

summa = 0
random_list = [random.randint(1, 100) for _ in range(1, 10000)]


#test_list = [1, 2, 3, 4, 5, 6, 7,8,9 ]

async def increment(start, stop):
    global summa
    for i in random_list[start:stop]:
        summa += i
        await asyncio.sleep(0)
    print(f"Значение счетчика: {summa:_}")


count_threads = 5

part_size = len(random_list) // count_threads
rest = len(random_list) % count_threads


async def main():
    start = 0
    tasks = []
    task = asyncio.ensure_future(increment(start, len(random_list)))
    tasks.append(task)

    # for i in range(count_threads):
    #     if i < rest:
    #         stop = start + part_size + 1
    #     else:
    #         stop = start + part_size
    #     task = asyncio.ensure_future(increment(start, stop))
    #     tasks.append(task)
    #     start = stop
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())

    print(f"Значение счетчика в финале: {summa:_}")
    print(f"Время выполнения: {time.time() - start_time}")
