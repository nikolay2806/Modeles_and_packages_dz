import os
import random
import shutil
import system


while True:
    menu = ['1. Создать папку',
            '2. Удалить (файл/папку)',
            '3. Копировать (файл/папку)',
            '4. Просмотр содержимого рабочей директории',
            '5. Посмотреть только папки',
            '6. Посмотреть только файлы',
            '7. Просмотр информации об операционной системе',
            '8. Создатель программы',
            '9. Играть в викторину',
            '10. Мой банковский счет',
            '11. Смена рабочей директории (*необязательный пункт',
            '12. Выход']
    for i in menu:
        print(i)
    choice = input('Выберете пункт меню: ')

    # 1. Создать папку
    if choice == '1':
        new_file = input('Введите имя папки: ')
        if not os.path.exists(new_file):
            os.mkdir(new_file)
            print(f'Создана папка "{new_file}"')

    # 2. Удалить (файл/папку)
    if choice == '2':
        remove_file = input('Введите имя папки для удаления: ')
        if  os.path.exists(remove_file):
            os.rmdir(remove_file)
            print(f'Удалена папка "{remove_file}"')
        else:
            print('Указанная папка не существует')

    # 3. Копировать (файл/папку)
    if choice == '3':
        print('Папки и файлы в текущей директории')
        path = os.listdir()
        print(path)
        file = input('Введите имя файла или папки для копирования: ')
        if os.path.isdir(file):
            shutil.copytree(file,f'{file}_копия')
            print(file)

        else:
            os.path.isfile(file)
            list_f = file.split('.')
            shutil.copy(file,f'{list_f[0]}_копия.{list_f[1]}')

    # 4. Просмотр содержимого рабочей директории
    if choice == '4':
        print('Папки и файлы в текущей директории')
        path = os.listdir()
        print(path)
    # 5. Посмотреть только папки
    if choice == '5':
        for file in os.listdir():
            d = os.path.join(file)
            if os.path.isdir(d):
                print(d)
    # 6. Посмотреть только файлы
    if choice == '6':
        for file in os.listdir():
            d = os.path.join(file)
            if os.path.isfile(d):
                print(d)
    # 7. Просмотр информации об операционной системе
    if choice == '7':
      system.main()

    # 8. Создатель программы
    if choice == '8':
        print('разработчик: Мартюшев Николай')
    # 9. Играть в викторину
    if choice == '9':
        def get_random_person():
            """
               Получить 1-го случайного человека
               :return:
               """
            FAMOUS_PEOPLE = {'Александр Сергеевич Пушнин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                             'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                             'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                             'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                             'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}
            name, date = random.choice(list(FAMOUS_PEOPLE.items()))
            return name, date
        def get_person_and_question():
            name, date = get_random_person()
            print(name)
            answer = input('Введите дату рождения знаменитости: ')
            if answer == date:
                print('Верно')
            else:
                print('Неверно')
        print('Добро пожаловать в игру "Викторина"')
        rounds = int(input('Сколько раз вы хотите играть? '))
        for i in range(rounds):
            get_person_and_question()
    # 10. Мой банковский счет
    if choice == '10':
        print('Мой банковский счет: 7777 7777 7777 7777')
    # 11. Смена рабочей директории (*необязательный пункт
    if choice == '11':
        pass
    # 12. Выход
    if choice == '12':
        break
    else:
        print('Не верный пункт меню')


