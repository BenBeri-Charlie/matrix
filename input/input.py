#!/bin/python3

import sys
import json
import matrix

# Входные данные - номера вызываемых функций и (не обязательно) имя файла с входными данными
# Если файл не указан - данные для проверки читаются из input.json
# Примеры вызова:
# ./input.py 1 2 3
# ./input.py test.json 3 2 1
if __name__ == "__main__":
    # Путь по-умолчанию
    path = 'input.json'
    # Список для номеров вызываемых функций
    calls = []

    # Чтение параметров вызова
    for param in sys.argv[1:]:
        # Если это цифра - добавить в список вызываемых функций
        if param.isdigit():
            calls.append(param)
        # Иначе - это путь к файлу совходными данными
        else:
            path = param

    # Чтение JSON со входными данными
    with open(path) as f:
        data = json.load(f)

    # Словарь функций
    dictionary = {
        '1': matrix.add(data['first_matrix_dimensions'],
                        data['second_matrix_dimensions'],
                        data['first_matrix'],
                        data['second_matrix']),
        '2': matrix.sub(data['first_matrix_dimensions'],
                        data['second_matrix_dimensions'],
                        data['first_matrix'],
                        data['second_matrix']),
        '3': matrix.mult(data['first_matrix_dimensions'],
                         data['second_matrix_dimensions'],
                         data['first_matrix'],
                         data['second_matrix'])
    }

    # Вызов функции из словоря по списку входных данных
    for param in calls:
        print(dictionary[param])
