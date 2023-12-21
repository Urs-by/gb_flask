import asyncio

import time
from ran_list import random_list, split_list

count_process = 5
result_list = split_list(random_list, count_process)

summa = 0


async def increment(part_list: list):
    global summa
    for i in part_list:
        summa += i
        await asyncio.sleep(0)
    print(f"Значение счетчика: {summa:_}")


async def main():
    for i in range(count_process):
        tasks = []
        task = asyncio.ensure_future(increment(result_list[i]))
        tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())

    print(f"Значение счетчика в финале: {summa:_}")
    print(f"Время выполнения: {time.time() - start_time}")
