import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict = np.random.randint(1, 101)
    step = 50

    while number != predict:
        count += 1

        if predict < number:
            predict += step
        else:
            predict -= step

        if step > 1:
            step //= 2
    # Ваш код заканчивается здесь

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=10000)  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    return int(np.mean(count_ls))


print('Run benchmarking for game_core_v3: ', end='')
print(f"Ваш алгоритм угадывает число в среднем за: {score_game(game_core_v3)} попытки")
