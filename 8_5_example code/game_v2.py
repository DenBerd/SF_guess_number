"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def number_predict(number: int = 1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predicted_number = 50 # исходное предполагаемое число
    spacing = 25 # исходный шаг

    while predicted_number != number:
        count += 1
        
        if number > predicted_number:
            predicted_number = predicted_number + spacing
            if spacing > 1:
                spacing = spacing//2
        else:
            predicted_number = predicted_number - spacing
            if spacing > 1:
                spacing = spacing//2
        
        
    return count


def score_game(number_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        number_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(number_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(number_predict)
