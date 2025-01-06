import os

from tabulate import tabulate

title_color = ['Цвета']
data = [['Черный'], ['Белый'], ['Серый'], ['Синий'], ['Красный'], ['Зеленый'], ['Желтый'], ['Розовый'],
        ['Фиолетовый'], ['Оранжевый']]
table_title = ['Номер', 'Производитель', 'Марка', 'Цвет', 'Тип двигателя', 'Тип коробки передач', 'активность фар',
               'активность двигателя', 'Статус дверей']
title_dvig = ['Двигатели']
lst_dvigat = [
    ["Бензиновый"],
    ["Дизельный"],
    ["Электрический"],
    ["Гибридный"],
    ["Газовый"],
]
title_box_peredach = ['Коробки передач']
lst_box_peredach = [
    ["Механическая"],
    ["Автоматическая"],
    ["Роботизированная"],
    ["Вариатор"],
    ["Tiptronic"]
]


def add_car(file):
    """Добавляет машину в файл."""
    while True:
        listik = terminal_vavod_car()
        print("Список машин:")
        print(tabulate(listik, headers=table_title, tablefmt="github"))
        number = input("Введите номер машины(число) отличное от других номеров в списке: ")
        if proverka_in_numbers_car(listik, number):
            print('Номер успешно введен')
            break
        else:
            print("Некорректный номер машины.")
    while True:
        print('')
        with open("base_manufacturer.txt", "r", encoding="utf-8") as f:
            proizv = ['Производители']
            lin = f.readlines()
            lines = ''.join(lin).split(',')
            lines_new = [[x.strip()] for x in lines]
            print(tabulate(lines_new, headers=proizv, tablefmt="github"))
        manufacturer = input("Введите производителя машины: ").capitalize()
        if proverka_base_manufacture(manufacturer) == False:
            print(
                'К сожалению такого производителя нет в нашем списке.Вы можете попробовать ввести производителя заново напечатав "новое", либо расширить наш список допустимых производителей напечатав "Добавить": ')
            a = input('Введите подходящее слово(Новое\Добавить): ')
            if a.lower() == "добавить":
                lines_new.append([a.capitalize()])
                add_base_manufacture(manufacturer)
                add_base_brand_proizv(manufacturer)
                print("Новый производитель успешно добавлен:")
                continue
            if a.lower() == "новое":
                continue
            else:
                print("Вы некорректно указали команду!")
        else:
            break
    while True:

        print('')
        with open("base_brand_manufacture.txt", "r", encoding="utf-8") as f:
            lines = [line.strip().split(',') for line in f]
            lst_brands = None
            for key, value in enumerate(lines):
                for model in value:
                    if model == manufacturer:
                        lst_brands = lines[key][1:]
            lst_brands_output = [[x.strip()] for x in lst_brands]
            title_brands = [f'Марки производителя {manufacturer}']
            print(tabulate(lst_brands_output, headers=title_brands, tablefmt="github"))
        brand = input("Введите марку машины: ")
        lst = proverka_base_brand(brand, manufacturer)
        if lst[0] == False:
            print(
                'К сожалению такой марки машины нет в нашем списке. Вы можете попробовать ввести марку заново напечатав "новое", либо расширить наш список допустимых марок напечатав "Добавить": ')
            a = input('Введите подходящее слово(Новое\Добавить): ')
            if a.lower() == "добавить":
                add_base_brand(lst[1], brand)
                for key, value in enumerate(lines):
                    if key == lst[1]:
                        lines[key].append(brand)
                print("Новая марка успешно добавлена:")
                continue
            if a.lower() == "новое":
                continue
            else:
                print("Вы некорректно указали команду!")
        else:
            break
    while True:
        print('')
        print(tabulate(data, headers=title_color, tablefmt="github"))
        print('')
        print('добавить в список свой цвет - 1\nввести цвет - 2\nудалить цвет - 3')
        a = input('Введите число:')
        if str(a) == '1':
            print('')
            color = input("Введите новый цвет: ")
            duplicate = False
            for x in data:
                if color.capitalize() in x:
                    duplicate = True
                    break
            if not duplicate:  # Если цвета нет в списке, добавляем его
                data.append([color.capitalize()])
                print(tabulate(data, headers=title_color, tablefmt="github"))
                continue
            else:
                print("Этот цвет уже есть в списке.")
                continue

        if str(a) == '2':
            print('')
            color = input("Введите цвет машины: ")
            found = False
            for x in data:
                if color.capitalize() in x:
                    found = True
                    break  # Выходим из цикла, если цвет найден
            if found:
                print(f"Цвет {color} выбран успешно")
                break
            else:
                print('Такого цвета нет в списке!')
            continue  # Продолжаем цикл после проверки цвета

        if str(a) == '3':
            print('')
            color = input("Введите цвет, который хотите удалить: ")
            found = False
            for i, x in enumerate(data):
                if color.capitalize() in x:
                    found = True
                    data.pop(i)  # Удаляем цвет из списка
                    print(tabulate(data, headers=title_color, tablefmt="github"))
                    break  # Выходим из цикла, если цвет удален
            if not found:
                print("Такого цвета нет в списке!")
            continue

        else:
            print('Вы ввели не число!')
            continue  # Продолжаем цикл после вывода сообщения об ошибке

    while True:
        print('')
        print(tabulate(lst_dvigat, headers=title_dvig, tablefmt="github"))
        print('')
        print('добавить в список свой двигатель - 1\nввести двигатель - 2\nудалить двигатель - 3')
        a = input('Введите число:')

        if str(a) == '1':
            dvigat = input("Введите новый тип двигателя: ")
            duplicate = False
            for x in lst_dvigat:
                if dvigat.capitalize() in x:
                    duplicate = True
                    break
            if not duplicate:  # Если цвета нет в списке, добавляем его
                lst_dvigat.append([dvigat.capitalize()])
                print(tabulate(lst_dvigat, headers=title_dvig, tablefmt="github"))
                continue
            else:
                print("Этот двигатель уже есть в списке.")
                continue

        if str(a) == '2':
            print('')
            dvigat = input("Введите двигатель машины: ")
            found = False
            for x in lst_dvigat:
                if dvigat.capitalize() in x:
                    found = True
                    break
            if found:
                print('')
                print(f"Двигатель {dvigat} выбран успешно!")
                break
            else:
                print('Такого двигателя нет в списке!')
            continue

        if str(a) == '3':
            print('')
            dvigat = input("Введите двигатель, который хотите удалить: ")
            found = False
            for i, x in enumerate(lst_dvigat):
                if dvigat.capitalize() in x:
                    found = True
                    lst_dvigat.pop(i)  # Удаляем цвет из списка
                    print(tabulate(lst_dvigat, headers=title_dvig, tablefmt="github"))
                    break
            if not found:
                print('')
                print("Такого двигателя нет в списке!")
            continue

        else:
            print('')
            print('Вы ввели не число!')
            continue
    while True:
        print('')
        print(tabulate(lst_box_peredach, headers=title_box_peredach, tablefmt="github"))
        print('')
        print(
            'добавить в список свой тип коробки передач - 1\nввести коробку передач - 2\nудалить коробку передач - 3')
        a = input('Введите число: ')

        if str(a) == '1':
            print('')
            box_per = input("Введите новый тип коробки передач: ")
            duplicate = False
            for x in lst_dvigat:
                if box_per.capitalize() in x:
                    duplicate = True
                    break
            if not duplicate:  # Если цвета нет в списке, добавляем его
                lst_box_peredach.append([box_per.capitalize()])
                print(tabulate(lst_box_peredach, headers=title_box_peredach, tablefmt="github"))
                continue
            else:
                print('')
                print("Этот тип коробки передач уже есть в списке.")
                continue

        if str(a) == '2':
            print('')
            box_per = input("Введите тип коробки передач: ")
            found = False
            for x in lst_box_peredach:
                if box_per.capitalize() in x:
                    found = True
                    break
            if found:
                print('')
                print(f"Коробка передач {box_per} выбрана успешно")
                break
            else:
                print('')
                print('Такой коробки передач нет в списке!')
            continue

        if str(a) == '3':
            print('')
            box_per = input("Введите  тип коробки передач, которую хотите удалить: ")
            found = False
            for i, x in enumerate(lst_box_peredach):
                if box_per.capitalize() in x:
                    found = True
                    lst_box_peredach.pop(i)  # Удаляем цвет из списка
                    print(tabulate(lst_box_peredach, headers=title_box_peredach, tablefmt="github"))
                    break
            if not found:
                print('')
                print("Такого типа коробки передач нет в списке!")
            continue

        else:
            print('')
            print('Вы ввели не число!')
            continue
    while True:
        print('')
        action_far = input("Введите 'ДА', если фары активны и 'НЕТ' в противоположенном случае: ")
        if action_far.lower() == "да":
            break
        if action_far.lower() == "нет":
            break
        else:
            print('Вы указали некорректный тип!')
    while True:
        print('')
        action_dvigat = input("Введите 'ДА', если двигатель включен и 'НЕТ' в противоположенном случае: ")
        if action_dvigat.lower() == "да":
            break
        if action_dvigat.lower() == "нет":
            break
        else:
            print('Вы указали некорректный тип!')

    while True:
        print('')
        action_doors = input("Введите 'ДА', если двери открыты и 'НЕТ', если закрыты: ")
        if action_doors.lower() == "да":
            break
        if action_doors.lower() == "нет":
            break
        else:
            print('Вы указали некорректный тип!')

    with open(file, "a", encoding="utf-8") as f:
        f.write(
            f"{number.lower()},{manufacturer.lower()},{brand.lower()},{color.lower()},{dvigat.lower()},{box_per.lower()},{action_far.lower()},{action_dvigat.lower()}, {action_doors.lower()}\n")
    print("Машина успешно добавлена!")

actions = ['Номер', 'Производитель', 'Марка', 'Цвет', 'Тип двигателя', 'Тип КП', 'Состояние фар', 'Состояние двигателя', 'Состояние дверей', 
           'Выход в главное меню']

def delete_car(file):
    while True:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                print("Список машин:")
                lines = [str(x[:-1]).split(',') for x in lines]
                print(tabulate(lines, headers=table_title, tablefmt="github"))
            else:
                print("Список машин пуст.")
        print('Укажите по какому критерию вы хотите удалять машину|или группу машин: ')

        print(
            'Удаление по номеру-1\nУдаление по производителю-2\nУдаление по марке-3\nУдаление по цвету-4\nУдаление по типу двигателя-5\nУдаление по типу коробки передач-6\nУдаление по вкл\выкл фар-7\nУдаление по вкл\выкл двигателю-8\nУдаление по статусу дверей - 9\nВыход в главное меню-10')

        del_znach = (input('Введите подходящее число: '))
        if del_znach == '1':
            while True:
                del_numbers = input('Введите номер удаляемой машины:')
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if del_numbers == value_1[0]:
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        'Если хотите удалить эту машину напишите "удалить", если хотите вернуться к выбору компонентов машины пропишите "отмена"')
                    v = input('напишите подходящее слово(удалить | отмена): ').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if line[0] != del_numbers:
                                    f.write(",".join(line) + "\n")
                        print("Машина удалена.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "отмена":
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению машин с таким номером нет в нашем списке.')
                    print('Вы можете попробовать ввести новое значение прописав команду"Повторить".')
                    print('Для выхода к выбору значений по удаления авто пропишите"Отмена".')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду( Повторить | Отмена ): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is False:
                            break
                        else:
                            print('Неверный ввод')
                    break
        if del_znach == '2':
            i = 0
            while True:
                del_manufacturer = input('Введите производителя удаляемой машины: ')
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if del_manufacturer == value_1[1]:
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        'Если хотите удалить эти/у машину напишите "удалить", если хотите удалить выборочную машину напишите "выбор",если хотите вернуться к выбору компонентов машины пропишите "отмена"')
                    v = input('напишите подходящее слово(удалить | выбор | отмена):').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if line[1] != del_manufacturer:
                                    f.write(",".join(line) + "\n")
                        print("Удаление прошло успешно.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "выбор":
                        while True:
                            a = input('Введите номер удаляемой машины: ')
                            if proverka_in_numbers_car_delete(del_numbers_lst, a) == True:
                                with open(file, "w", encoding="utf-8") as f:
                                    for line in lines:
                                        if line[0] != a or line[1] != del_manufacturer:
                                            f.write(",".join(line) + "\n")
                                print("Машина удалена.")
                                break
                            else:
                                print('Некорректный ввод номера машины, попробуйте снова')
                        break  # Выход из цикла удаления по номеру
                    elif v == 'отмена':
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению машин с таким производителем нет в нашем списке.')
                    print('Вы можете попробовать ввести новое значение прописав команду"Повторить".')
                    print('Для выхода к выбору значений по удаления авто пропишите"Отмена".')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду( Повторить | Отмена ): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is None:
                            print('Неверный ввод')
                        else:
                            i += 1
                            break
                    if i != 0:
                        i -= 1
                        break

        if del_znach == '3':
            i = 0
            while True:
                del_manufacturer = input('Введите марку удаляемой машины: ').lower()
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if del_manufacturer == value_1[2]:
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        'Если хотите удалить эти/у машину напишите "удалить", если хотите удалить выборочную машину напишите "выбор",если хотите вернуться к выбору компонентов машины пропишите "отмена"')
                    v = input('напишите подходящее слово(удалить | выбор | отмена):').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if line[2] != del_manufacturer:
                                    f.write(",".join(line) + "\n")
                        print("Удаление прошло успешно.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "выбор":
                        while True:
                            a = input('Введите номер удаляемой машины: ')
                            if proverka_in_numbers_car_delete(del_numbers_lst, a) == True:
                                with open(file, "w", encoding="utf-8") as f:
                                    for line in lines:
                                        if line[0] != a or line[2] != del_manufacturer:
                                            f.write(",".join(line) + "\n")
                                print("Машина удалена.")
                                break
                            else:
                                print('Некорректный ввод номера машины, попробуйте снова')
                        break  # Выход из цикла удаления по номеру
                    elif v == 'отмена':
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению машин с такой маркой нет в нашем списке.')
                    print('Вы можете попробовать ввести новое значение прописав команду"Повторить".')
                    print('Для выхода к выбору значений по удаления авто пропишите"Отмена".')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду( Повторить | Отмена ): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is None:
                            print('Неверный ввод')
                        else:
                            i += 1
                            break
                    if i != 0:
                        i -= 1
                        break

        if del_znach == '4':
            i = 0
            while True:
                del_manufacturer = input('Введите цвет удаляемой машины: ').lower()
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if del_manufacturer == value_1[3]:
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        'Если хотите удалить эти/у машину напишите "удалить", если хотите удалить выборочную машину напишите "выбор",если хотите вернуться к выбору компонентов машины пропишите "отмена"')
                    v = input('напишите подходящее слово(удалить | выбор | отмена):').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if line[3] != del_manufacturer:
                                    f.write(",".join(line) + "\n")
                        print("Удаление прошло успешно.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "выбор":
                        while True:
                            a = input('Введите номер удаляемой машины: ')
                            if proverka_in_numbers_car_delete(del_numbers_lst, a) == True:
                                with open(file, "w", encoding="utf-8") as f:
                                    for line in lines:
                                        if line[0] != a or line[3] != del_manufacturer:
                                            f.write(",".join(line) + "\n")
                                print("Машина удалена.")
                                break
                            else:
                                print('Некорректный ввод номера машины, попробуйте снова')
                        break  # Выход из цикла удаления по номеру
                    elif v == 'отмена':
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению машин с таким цветом нет в нашем списке.')
                    print('Вы можете попробовать ввести новое значение прописав команду"Повторить".')
                    print('Для выхода к выбору значений по удаления авто пропишите"Отмена".')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду( Повторить | Отмена ): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is None:
                            print('Неверный ввод')
                        else:
                            i += 1
                            break
                    if i != 0:
                        i -= 1
                        break
        if del_znach == '5':
            i = 0
            while True:
                del_manufacturer = input('Введите тип двигателя удаляемой машины: ').lower()
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if del_manufacturer == value_1[4]:
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        'Если хотите удалить эти/у машину напишите "удалить", если хотите удалить выборочную машину напишите "выбор",если хотите вернуться к выбору компонентов машины пропишите "отмена"')
                    v = input('напишите подходящее слово(удалить | выбор | отмена): ').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if line[4] != del_manufacturer:
                                    f.write(",".join(line) + "\n")
                        print("Удаление прошло успешно.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "выбор":
                        while True:
                            a = input('Введите номер удаляемой машины: ')
                            if proverka_in_numbers_car_delete(del_numbers_lst, a) == True:
                                with open(file, "w", encoding="utf-8") as f:
                                    for line in lines:
                                        if line[0] != a or line[4] != del_manufacturer:
                                            f.write(",".join(line) + "\n")
                                print("Машина удалена.")
                                break
                            else:
                                print('Некорректный ввод номера машины, попробуйте снова')
                        break  # Выход из цикла удаления по номеру
                    elif v == 'отмена':
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению машин с таким типом двигателя нет в нашем списке.')
                    print('Вы можете попробовать ввести новое значение прописав команду"Повторить".')
                    print('Для выхода к выбору значений по удаления авто пропишите"Отмена".')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду( Повторить | Отмена ): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is None:
                            print('Неверный ввод')
                        else:
                            i += 1
                            break
                    if i != 0:
                        i -= 1
                        break
        if del_znach == '6':
            i = 0
            while True:
                del_manufacturer = input('Введите тип коробки передач удаляемой машины: ').lower()
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if del_manufacturer == value_1[5]:
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        'Если хотите удалить эти/у машину напишите "удалить", если хотите удалить выборочную машину напишите "выбор",если хотите вернуться к выбору компонентов машины пропишите "отмена"')
                    v = input('напишите подходящее слово(удалить | выбор | отмена): ').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if line[5] != del_manufacturer:
                                    f.write(",".join(line) + "\n")
                        print("Удаление прошло успешно.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "выбор":
                        while True:
                            a = input('Введите номер удаляемой машины: ')
                            if proverka_in_numbers_car_delete(del_numbers_lst, a) == True:
                                with open(file, "w", encoding="utf-8") as f:
                                    for line in lines:
                                        if line[0] != a or line[5] != del_manufacturer:
                                            f.write(",".join(line) + "\n")
                                print("Машина удалена.")
                                break
                            else:
                                print('Некорректный ввод номера машины, попробуйте снова')
                        break  # Выход из цикла удаления по номеру
                    elif v == 'отмена':
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению машин с таким типом коробки передач нет в нашем списке.')
                    print('Вы можете попробовать ввести новое значение прописав команду"Повторить".')
                    print('Для выхода к выбору значений по удаления авто пропишите"Отмена".')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду( Повторить | Отмена ): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is None:
                            print('Неверный ввод')
                        else:
                            i += 1
                            break
                    if i != 0:
                        i -= 1
                        break
        if del_znach == '7':
            i = 0
            while True:
                del_manufacturer = input('Введите активность фар (да|нет) удаляемой машины: ').lower()
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if del_manufacturer == value_1[6]:
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        'Если хотите удалить эти/у машину напишите "удалить", если хотите удалить выборочную машину напишите "выбор",если хотите вернуться к выбору компонентов машины пропишите "отмена"')
                    v = input('напишите подходящее слово(удалить | выбор | отмена): ').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if line[6] != del_manufacturer:
                                    f.write(",".join(line) + "\n")
                        print("Удаление прошло успешно.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "выбор":
                        while True:
                            a = input('Введите номер удаляемой машины: ')
                            if proverka_in_numbers_car_delete(del_numbers_lst, a) == True:
                                with open(file, "w", encoding="utf-8") as f:
                                    for line in lines:
                                        if line[0] != a or line[6] != del_manufacturer:
                                            f.write(",".join(line) + "\n")
                                print("Машина удалена.")
                                break
                            else:
                                print('Некорректный ввод номера машины, попробуйте снова')
                        break  # Выход из цикла удаления по номеру
                    elif v == 'отмена':
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению таких машин нет в нашем списке.')
                    print('Вы можете попробовать ввести новое значение прописав команду"Повторить".')
                    print('Для выхода к выбору значений по удаления авто пропишите"Отмена".')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду( Повторить | Отмена ): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is None:
                            print('Неверный ввод')
                        else:
                            i += 1
                            break
                    if i != 0:
                        i -= 1
                        break
        if del_znach == '8':
            i = 0
            while True:
                del_manufacturer = input('Введите активность двигателя(да|нет) удаляемой машины: ').lower()
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if del_manufacturer == value_1[7]:
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        'Если хотите удалить эти/у машину напишите "удалить", если хотите удалить выборочную машину '
                        'напишите "выбор",если хотите вернуться к выбору компонентов машины пропишите "отмена"')
                    v = input('напишите подходящее слово(удалить | выбор | отмена): ').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if line[7] != del_manufacturer:
                                    f.write(",".join(line) + "\n")
                        print("Удаление прошло успешно.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "выбор":
                        while True:
                            a = input('Введите номер удаляемой машины: ')
                            if proverka_in_numbers_car_delete(del_numbers_lst, a) == True:
                                with open(file, "w", encoding="utf-8") as f:
                                    for line in lines:
                                        if line[0] != a or line[7] != del_manufacturer:
                                            f.write(",".join(line) + "\n")
                                print("Машина удалена.")
                                break
                            else:
                                print('Некорректный ввод номера машины, попробуйте снова')
                        break  # Выход из цикла удаления по номеру
                    elif v == 'отмена':
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению таких машин нет в нашем списке.')
                    print('Вы можете попробовать ввести новое значение прописав команду"Повторить".')
                    print('Для выхода к выбору значений по удаления авто пропишите"Отмена".')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду( Повторить | Отмена ): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is None:
                            print('Неверный ввод')
                        else:
                            i += 1
                            break
                    if i != 0:
                        i -= 1
                        break

        if del_znach == '9':
            i = 0
            while True:
                del_manufacturer = input('Укажите, открыты ли двери (да|нет) удаляемой машины: ').lower()
                del_numbers_lst = []
                for key_1, value_1 in enumerate(lines):
                    if len(value_1) > 8 and del_manufacturer == value_1[8].strip():
                        del_numbers_lst.append(value_1)
                if del_numbers_lst != []:
                    print(tabulate(del_numbers_lst, headers=table_title, tablefmt="github"))
                    print(
                        "Если хотите удалить эти/эту машину, введите 'удалить', если хотите удалить выборочную машину, "
                        "напишите 'выбор', или введите 'отмена' для выхода.")
                    v = input('напишите подходящее слово(удалить | выбор | отмена): ').lower()
                    if v == 'удалить':
                        with open(file, "w", encoding="utf-8") as f:
                            for line in lines:
                                if len(line) <= 8 or line[8].strip() != del_manufacturer:
                                    f.write(",".join(line) + "\n")
                        print("Удаление прошло успешно.")
                        break  # Выход из цикла удаления по номеру
                    elif v == "выбор":
                        while True:
                            a = input('Введите номер удаляемой машины: ')
                            if proverka_in_numbers_car_delete(del_numbers_lst, a) == True:
                                with open(file, "w", encoding="utf-8") as f:
                                    for line in lines:
                                        if len(line) <= 8 or (line[0] != a or line[8].strip() != del_manufacturer):
                                            f.write(",".join(line) + "\n")
                                print("Машина удалена.")
                                break
                            else:
                                print('Некорректный ввод номера машины, попробуйте снова')
                        break  # Выход из цикла удаления по номеру
                    elif v == 'отмена':
                        break  # Выход из цикла удаления по номеру
                    else:
                        print('Неверный ввод')
                else:
                    print('К сожалению таких машин нет в нашем списке.')
                    print('Попробуйте ввести новое значение, прописав команду "Повторить".')
                    print('Также вы можете выйти из удаления машины, прописав "Отмена"')
                    while True:
                        commands_in_exit = str(input('Введите подходящую команду(Повторить | Отмена): '))
                        func_rezult = proverka_сommands(commands_in_exit)
                        if func_rezult is True:
                            break
                        elif func_rezult is None:
                            print('Неверный ввод')
                        else:
                            i += 1
                            break
                    if i != 0:
                        i -= 1
                        break

        if del_znach == '10':
            break


def proverka_сommands(znach):
    if znach.capitalize() == 'Повторить':
        return True
    if znach.capitalize() == 'Отмена':
        return False
    else:
        return None


def edit_car_by_number(file_path, car_number):
    lines = []
    car_found = False

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            parts_print = [parts]
            if parts[0] == car_number:
                car_found = True

                while True:
                    print(tabulate(parts_print, headers=table_title, tablefmt="github"))
                    print("\nВыберите поле для редактирования:")
                    print("1. Марка")
                    print("2. Цвет")
                    print("3. Тип двигателя")
                    print("4. Тип коробки передач")
                    print("5. Активность фар")
                    print("6. Активность двигателя")
                    print("7. Статус дверей")
                    print("8. Завершить редактирование")

                    choice = input("Введите номер поля: ")
                    if choice == '1':
                        marka = redactir_model(parts[1])
                        if True in marka:
                            parts[2] = marka[1].lower() if marka[1].lower() else parts[2]
                    elif choice == '2':
                        color = redactir_color().lower()
                        parts[3] = color if color else parts[3]
                    elif choice == '3':
                        dvigat = redactir_dvigat().lower()
                        parts[4] = dvigat if dvigat else parts[4]
                    elif choice == '4':
                        box_peredach = redactir_box_peredach().lower()
                        parts[5] = box_peredach if box_peredach else parts[5]
                    elif choice == '5':
                        new_headlights_status = input("Введите новый статус фар (оставьте пустым, чтобы не менять): ").lower()
                        parts[6] = new_headlights_status if new_headlights_status else parts[6]
                    elif choice == '6':
                        new_engine_status = input("Введите новый статус двигателя (оставьте пустым, чтобы не менять): ").lower()
                        parts[7] = new_engine_status if new_engine_status else parts[7]
                    elif choice == '7':
                        new_doors_status = input("Введите новый статус дверей (оставьте пустым, чтобы не менять): ").lower()
                        parts[8] = new_doors_status if new_doors_status else parts[8]
                    elif choice == '8':
                        break
                    else:
                        print("Неверный выбор. Попробуйте снова.")

                lines.append(",".join(parts) + "\n")  # Добавляем обновленную строку
            else:
                lines.append(line)  # Добавляем исходную строку

    if car_found:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print("Данные о машине обновлены.")
        return True
    else:
        print("Машина с таким номером не найдена.")
        return False

def redactir_box_peredach():
    while True:
        print('')
        print(tabulate(lst_box_peredach, headers=title_box_peredach, tablefmt="github"))
        print('')
        print(
            'добавить в список свой тип коробки передач - 1\nввести коробку передач - 2\nудалить коробку передач - 3')
        a = input('Введите число: ')

        if str(a) == '1':
            print('')
            box_per = input("Введите новый тип коробки передач: ")
            duplicate = False
            for x in lst_dvigat:
                if box_per.capitalize() in x:
                    duplicate = True
                    break
            if not duplicate:  # Если цвета нет в списке, добавляем его
                lst_box_peredach.append([box_per.capitalize()])
                print(tabulate(lst_box_peredach, headers=title_box_peredach, tablefmt="github"))
                continue
            else:
                print('')
                print("Этот тип коробки передач уже есть в списке.")
                continue

        if str(a) == '2':
            print('')
            box_per = input("Введите тип коробки передач: ")
            found = False
            for x in lst_box_peredach:
                if box_per.capitalize() in x:
                    found = True
                    break
            if found:
                print('')
                print(f"Коробка передач {box_per} выбрана успешно")
                return box_per
            else:
                print('')
                print('Такой коробки передач нет в списке!')
            continue

        if str(a) == '3':
            print('')
            box_per = input("Введите  тип коробки передач, которую хотите удалить: ")
            found = False
            for i, x in enumerate(lst_box_peredach):
                if box_per.capitalize() in x:
                    found = True
                    lst_box_peredach.pop(i)  # Удаляем цвет из списка
                    print(tabulate(lst_box_peredach, headers=title_box_peredach, tablefmt="github"))
                    break
            if not found:
                print('')
                print("Такого типа коробки передач нет в списке!")
            continue

        else:
            print('')
            print('Вы ввели не число!')
            continue

def redactir_dvigat():
    while True:
        print('')
        print(tabulate(lst_dvigat, headers=title_dvig, tablefmt="github"))
        print('')
        print('добавить в список свой двигатель - 1\nввести двигатель - 2\nудалить двигатель - 3')
        a = input('Введите число:')

        if str(a) == '1':
            dvigat = input("Введите новый тип двигателя: ")
            duplicate = False
            for x in lst_dvigat:
                if dvigat.capitalize() in x:
                    duplicate = True
                    break
            if not duplicate:  # Если цвета нет в списке, добавляем его
                lst_dvigat.append([dvigat.capitalize()])
                print(tabulate(lst_dvigat, headers=title_dvig, tablefmt="github"))
                continue
            else:
                print("Этот двигатель уже есть в списке.")
                continue

        if str(a) == '2':
            print('')
            dvigat = input("Введите двигатель машины: ")
            found = False
            for x in lst_dvigat:
                if dvigat.capitalize() in x:
                    found = True
                    break
            if found:
                print('')
                print(f"Двигатель {dvigat} выбран успешно!")
                return dvigat
            else:
                print('Такого двигателя нет в списке!')
            continue

        if str(a) == '3':
            print('')
            dvigat = input("Введите двигатель, который хотите удалить: ")
            found = False
            for i, x in enumerate(lst_dvigat):
                if dvigat.capitalize() in x:
                    found = True
                    lst_dvigat.pop(i)  # Удаляем цвет из списка
                    print(tabulate(lst_dvigat, headers=title_dvig, tablefmt="github"))
                    break
            if not found:
                print('')
                print("Такого двигателя нет в списке!")
            continue

        else:
            print('')
            print('Вы ввели не число!')
            continue
def redactir_color():
    while True:
        print('')
        print(tabulate(data, headers=title_color, tablefmt="github"))
        print('')
        print('добавить в список свой цвет - 1\nввести цвет - 2\nудалить цвет - 3')
        a = input('Введите число:')
        if str(a) == '1':
            print('')
            color = input("Введите новый цвет: ")
            duplicate = False
            for x in data:
                if color.capitalize() in x:
                    duplicate = True
                    break
            if not duplicate:  # Если цвета нет в списке, добавляем его
                data.append([color.capitalize()])
                print(tabulate(data, headers=title_color, tablefmt="github"))
                continue
            else:
                print("Этот цвет уже есть в списке.")
                continue

        if str(a) == '2':
            print('')
            color = input("Введите цвет машины: ")
            found = False
            for x in data:
                if color.capitalize() in x:
                    found = True
                    break  # Выходим из цикла, если цвет найден
            if found:
                print(f"Цвет {color} выбран успешно")
                return color
            else:
                print('Такого цвета нет в списке!')
            continue  # Продолжаем цикл после проверки цвета

        if str(a) == '3':
            print('')
            color = input("Введите цвет, который хотите удалить: ")
            found = False
            for i, x in enumerate(data):
                if color.capitalize() in x:
                    found = True
                    data.pop(i)  # Удаляем цвет из списка
                    print(tabulate(data, headers=title_color, tablefmt="github"))
                    break  # Выходим из цикла, если цвет удален
            if not found:
                print("Такого цвета нет в списке!")
            continue

        else:
            print('Вы ввели не число!')
            continue  # Продолжаем цикл после вывода сообщения об ошибке


def redactir_model(manufacturer):
    while True:
        print('')
        with open("base_brand_manufacture.txt", "r", encoding="utf-8") as f:
            lines = [line.strip().split(',') for line in f]
            lst_brands = None
            for key, value in enumerate(lines):
                for model in value:
                    if model == manufacturer.capitalize():
                        lst_brands = lines[key][1:]
            lst_brands_output = [[x.strip()] for x in lst_brands]
            title_brands = [f'Марки производителя {manufacturer}']
            print(tabulate(lst_brands_output, headers=title_brands, tablefmt="github"))
        brand = input("Введите марку машины: ")
        lst = proverka_base_brand(brand, manufacturer)
        if lst[0] == False:
            print(
                'К сожалению такой марки машины нет в нашем списке. Вы можете попробовать ввести марку заново напечатав "новое", либо расширить наш список допустимых марок напечатав "Добавить": ')
            a = input('Введите подходящее слово(Новое\Добавить): ')
            if a.lower() == "добавить":
                add_base_brand(lst[1], brand)
                for key, value in enumerate(lines):
                    if key == lst[1]:
                        lines[key].append(brand)
                print("Новая марка успешно добавлена:")
                continue
            if a.lower() == "новое":
                continue
            else:
                print("Вы некорректно указали команду!")
        else:
            return [True, brand]
def print_car_list(file):
    """Выводит список машин из файла."""
    with open(file, "r", encoding="utf-8") as f:
        lin = f.readlines()
        if lin:
            print("Список машин:")
            lines = [str(x[:-1]).split(',') for x in lin]
            print(tabulate(lines, headers=table_title, tablefmt="github"))
        else:
            print("Список машин пуст.")


def print_poisc_car(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        if lines:
            print("Список машин:")
            lines = [str(x[:-1]).split(',') for x in lines]
        else:
            print("Список машин пуст.")
            return  # Выход из функции, если список пуст

    while True:
        _lst = []
        print(tabulate(lines, headers=table_title, tablefmt="github"))
        print("\nВыберите поле для поиска:")
        print('1. Производитель')
        print("2. Марка")
        print("3. Цвет")
        print("4. Тип двигателя")
        print("5. Тип коробки передач")
        print("6. Активность фар")
        print("7. Активность двигателя")
        print("8. Статус дверей")
        print("9. Выйти в главное меню")

        str_count = input('Введите значение по поиску авто: ')
        if str_count.isdigit():
            if str_count == '1':  # Поиск по производителю
                while True:
                    del_manufacturer = input('Введите производителя машины: ').lower()
                    del_numbers_lst = []
                    for key_1, value_1 in enumerate(lines):
                        if del_manufacturer == value_1[1]:
                            del_numbers_lst.append(value_1)
                    for line in lines:
                        if line[1] == del_manufacturer:
                            _lst.append(line)
                    if not _lst:
                        a = ('Введите другого произвоителя чтобы выйти напишите отмена').lower()
                        if a == 'отмена':
                            break
                        else:
                            _lst.clear()
                            continue
                    else:
                        print(tabulate(_lst, headers=table_title, tablefmt="github"))
                        break
            elif str_count == '2':  # Поиск по производителю
                while True:
                    del_manufacturer = input('Введите марку машины: ').lower()
                    del_numbers_lst = []
                    for key_1, value_1 in enumerate(lines):
                        if del_manufacturer == value_1[2]:
                            del_numbers_lst.append(value_1)
                    for line in lines:
                        if line[2] == del_manufacturer:
                            _lst.append(line)
                    if not _lst:
                        a = ('Введите другую марку либо чтобы выйти напишите отмена').lower()
                        if a == 'отмена':
                            break
                        else:
                            _lst.clear()
                            continue
                    else:
                        print(tabulate(_lst, headers=table_title, tablefmt="github"))
                        break
            elif str_count == '3':
                while True:
                    del_manufacturer = input('Введите цвет машины: ').lower()
                    del_numbers_lst = []
                    for key_1, value_1 in enumerate(lines):
                        if del_manufacturer == value_1[3]:
                            del_numbers_lst.append(value_1)
                    for line in lines:
                        if line[3] == del_manufacturer:
                            _lst.append(line)
                    if not _lst:
                        a = ('Введите другой цвет либо чтобы выйти напишите отмена').lower()
                        if a == 'отмена':
                            break
                        else:
                            _lst.clear()
                            continue
                    else:
                        print(tabulate(_lst, headers=table_title, tablefmt="github"))
                        break
            elif str_count == '4':  # Поиск по типу двигателя
                while True:
                    del_manufacturer = input('Введите тип двигателя машины: ').lower()
                    del_numbers_lst = []
                    for key_1, value_1 in enumerate(lines):
                        if del_manufacturer == value_1[4]:
                            del_numbers_lst.append(value_1)
                    for line in lines:
                        if line[4] == del_manufacturer:
                            _lst.append(line)
                    if not _lst:
                        a = ('Введите другой тип двигателя либо чтобы выйти напишите отмена').lower()
                        if a == 'отмена':
                            break
                        else:
                            _lst.clear()
                            continue
                    else:
                        print(tabulate(_lst, headers=table_title, tablefmt="github"))
                        break
            elif str_count == '5':  # Поиск по типу коробки передач
                while True:
                    del_manufacturer = input('Введите тип коробки передач машины: ').lower()
                    del_numbers_lst = []
                    for key_1, value_1 in enumerate(lines):
                        if del_manufacturer == value_1[5]:
                            del_numbers_lst.append(value_1)
                    for line in lines:
                        if line[5] == del_manufacturer:
                            _lst.append(line)
                    if not _lst:
                        a = ('Введите другой тип коробки передач либо чтобы выйти напишите отмена').lower()
                        if a == 'отмена':
                            break
                        else:
                            _lst.clear()
                            continue
                    else:
                        print(tabulate(_lst, headers=table_title, tablefmt="github"))
                        break
            elif str_count == '6':  # Поиск по активности фар
                while True:
                    del_manufacturer = input('Введите активность фар(да/нет): ').lower()
                    del_numbers_lst = []
                    for key_1, value_1 in enumerate(lines):
                        if del_manufacturer == value_1[6]:
                            del_numbers_lst.append(value_1)
                    for line in lines:
                        if line[6] == del_manufacturer:
                            _lst.append(line)
                    if not _lst:
                        a = ('Введите другую активность фар либо для выхода напишите отмена: ').lower()
                        if a == 'отмена':
                            break
                        else:
                            _lst.clear()
                            continue
                    else:
                        print(tabulate(_lst, headers=table_title, tablefmt="github"))
                        break
            elif str_count == '7':  # Поиск по активности двигателя
                while True:
                    del_manufacturer = input('Введите активность двигателя(да/нет): ').lower()
                    del_numbers_lst = []
                    for key_1, value_1 in enumerate(lines):
                        if del_manufacturer == value_1[7]:
                            del_numbers_lst.append(value_1)
                    for line in lines:
                        if line[7] == del_manufacturer:
                            _lst.append(line)
                    if not _lst:
                        a = ('Введите другую активность двигателя либо для выхода напишите отмена: ').lower()
                        if a == 'отмена':
                            break
                        else:
                            _lst.clear()
                            continue
                    else:
                        print(tabulate(_lst, headers=table_title, tablefmt="github"))
                        break
            elif str_count == '8':  # Поиск по активности дверей
                while True:
                    del_manufacturer = input('Введите статус дверей, открыты ли они? (да/нет): ').lower().strip()
                    _lst = []  # Очищаем список перед каждым новым поиском
                    for line in lines:
                        if len(line) > 8 and line[8].strip().lower() == del_manufacturer:
                            _lst.append(line)
                    if not _lst:
                        print('Таких машин не найдено.')
                        a = input('Введите другое состояние дверей либо напишите "отмена" для выхода: ').lower()
                        if a == 'отмена':
                            break
                    else:
                        print(tabulate(_lst, headers=table_title, tablefmt="github"))
                        break
            elif str_count == '9':  # Выход в главное меню
                print("Выход в главное меню")
                return  # Выход из функции print_poisc_car
            else:
                print('Некорректный ввод. Пожалуйста, введите число от 1 до 9')
            break
        else:
            print('Некорректный ввод. Пожалуйста, введите число.')
    pass

def main():
    """Основная функция."""
    file = "cars_parking.txt"
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            pass  # Создаем файл, если его нет

    while True:
        print("\nМеню:")
        print("1. Добавить машину")
        print("2. Удалить машину")
        print("3. Редактировать машину")
        print("4. Вывести список машин")
        print('5. Найти машину/машины')
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_car(file)
        elif choice == "2":
            delete_car(file)
        elif choice == "3":
            pyk = terminal_vavod_car()
            while True:
                print_car_list(file)
                a = input('Напишите номер  машины: ')
                if proverka_in_numbers_car(pyk, a) == False:
                    edit_car_by_number(file, a)
                    break
                elif proverka_in_numbers_car(pyk, a) == True:
                    print("Машин с таким номером нет")
                else:
                    print("Список пуст")
                    break

        elif choice == "4":
            print_car_list(file)

        elif choice == "5":
            print_poisc_car(file)
        elif choice == "6":
            print('До скорых встреч!')
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")



def proverka_base_manufacture(manufacture):
    with open("base_manufacturer.txt", "r", encoding="utf-8") as f:
        lin = f.readlines()
        lines = ''.join(lin).split(',')
        lines_new = [x.strip() for x in lines]
        return manufacture.lower() in [line.lower() for line in lines_new]


def add_base_manufacture(manufacture):
    with open("base_manufacturer.txt", "a", encoding="utf-8") as f:
        f.write(f", {manufacture.capitalize()}")


def add_base_brand_proizv(manufacture):
    with open("base_brand_manufacture.txt", "a", encoding="utf-8") as f:
        f.write(manufacture + "\n")



def proverka_base_brand(brand, manufacture):
    with open("base_brand_manufacture.txt", "r", encoding="utf-8") as f:
        lines = [line.strip().split(',') for line in f]

        for key, value in enumerate(lines):
            if manufacture.lower() in [val.lower().strip() for val in value]:
                stroka_izm = key
                if brand.lower() in [val.lower().strip() for val in value]:
                    return [True, stroka_izm]  # Изменено: Возвращаем key (номер строки)

    return [False, stroka_izm]  # Изменено: Возвращаем key (номер строки)


def add_base_brand(numbers, brand):
    with open("base_brand_manufacture.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines[numbers] = lines[numbers].rstrip(
            "\n") + ", " + brand + "\n"  # Добавьте  brand в строку с индексом numbers

    with open("base_brand_manufacture.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)


def terminal_vavod_car():
    with open("cars_parking.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        if lines:
            lines = [str(x[:-1]).split(',') for x in lines]
            return lines


def proverka_in_numbers_car(lst, number):
    if lst == None:
        return True
    if number.isdigit():
        for value in lst:
            if value[0] == number:
                return False

        return True
    else:
        return False


def proverka_in_numbers_car_delete(lst, number):
    if number.isdigit():
        for value in lst:
            if value[0] == number:
                return True
        return False
    return False


if __name__ == "__main__":
    main()
