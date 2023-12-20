import random

random_list = [random.randint(1, 100) for _ in range(1, 1000000)]


def split_list(input_list: list, n: int) -> list:
    """
    Разбивает список на части для параллельной обработки
    :param input_list:
    :param n:
    :return: список с разбитыми частями
    """
    # Рассчитываем размер каждой части
    part_size = len(input_list) // n
    # Получаем остаток, который будет распределен по частям
    remainder = len(input_list) % n
    for i in range(0, len(input_list)):
        result = []
        start = 0
        for i in range(n):
            # Увеличиваем размер части на 1, если есть остаток
            if i < remainder:
                end = start + part_size + 1
            else:
                end = start + part_size
            result.append(input_list[start:end])
            start = end

        return result

