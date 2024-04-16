def copy_row():
    with open(f'db/data_1.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    print(f"Вывод данных из 1-ого файла:\n"
              f"{''.join(data)}")
    print()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пустой!")
    else:
        number_row = int(input(f"Введите номер строки "
                                f"от 1 до {count_rows}: "))
        while number_row < 1 or number_row > count_rows:
            number_row = int(input(f"Ошибка!"
                                    f"Введите номер строки "
                                    f"от 1 до {count_rows}: "))
        with open('db/data_1.txt') as source, open('db/data_2.txt', 'w') as destination:
            destination.write(data[number_row - 1])
        print("Строка успешно скопирована!")