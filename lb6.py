import random


def number_1():
    library = {
        "Франция": "Париж",
        "Америки": "Вашингтон",
        "Россия": "Москва",
        "Китай": "Пекин",
        "Великобритания": "Лондон",
        "Германия": "Берлин",
        "Япония": "Токио",
        "Индия": "Нью-Дели",
        "Бразилия": "Бразилиа",
        "Италия": "Рим",
    }

    print("\nКлюч-значение:\n")
    for x, y in library.items():
        print(f"{x}: {y}")

    entry_country = input("\nВведите страну: ")
    if entry_country in library:
        print(f"Страна: {entry_country} -> Столица: {library[entry_country]}")
    else:
        print(f"{entry_country} - нет в словаре")

    print("\nСортировка в алфавитном порядке по странам: ")
    sorted_library = sorted(library.keys())
    for x in sorted_library:
        print(f"{x}: {library[x]}")


def number_2():
    alphabet = {
        "А": 1,
        "В": 1,
        "Е": 1,
        "И": 1,
        "Н": 1,
        "О": 1,
        "Р": 1,
        "С": 1,
        "Т": 1,
        "Д": 2,
        "К": 2,
        "Л": 2,
        "М": 2,
        "П": 2,
        "У": 2,
        "Б": 3,
        "Г": 3,
        "Ё": 3,
        "Ь": 3,
        "Я": 3,
        "Й": 4,
        "Ы": 4,
        "Ж": 5,
        "З": 5,
        "Х": 5,
        "Ц": 5,
        "Ч": 5,
        "Ш": 8,
        "Э": 8,
        "Ю": 8,
        "Ф": 10,
        "Щ": 10,
        "Ъ": 10,
    }

    score = 0
    word = input("Введите слово: ")

    for i in word.upper():
        if i in alphabet:
            score += alphabet[i]

    print(f"Стоимость: {score}")


while True:
    number = int(input("Введите номер задания: "))

    if number == 1:
        number_1()
    elif number == 2:
        number_2()
    else:
        print("Такого задания нет")
