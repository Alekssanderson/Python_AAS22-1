"""
В качестве проверки кода на соответствие прописанным стандартам PEP-8
я решил взять код из домашнего задания №2, ибо как-раз в этом коде
программа PyCharm обнаружила больше всего ошибок (37 шт).



1) PEP 257: Для строк документов следует использовать тройные строки в двойных кавычках.

Вывод: всегда использовал одинарные кавычки для таких блоков комментарий,
лучше/хуже не стало, читаемость не изменилась.


2) PEP 8: Линия продолжения E128 с заниженным отступом для визуального отступа.
Было:
    A = ["Дюна", "Зеленая миля", ...,
        "Крестный отец", ...

Стало:
    A = ["Дюна", "Зеленая миля", ...,
         "Крестный отец", ...

Вывод: стало немного лучше, читаемость улучшилась.


3) PEP 8: Слишком длинная строка E501 (472 > 120 символов).
Было:
    # A1 = [["Дюна", 2021], ["Зеленая миля", 1999], ["Форрест Гамп", 1994],... - 472 символа

PEP-8 предлагает так:
    # A1 = [["Дюна", 2021], ... - до 120 символов
    # 1991], ["Крестный отец", 1972], ... - до 120 символов
    # ["Дюна", 1984], ["Брат 2", 2000], ... - до 120 символов
    # ["Интерстеллар", 2014], ... - до 120 символов
    # 2010], ["Титаник", 1997]]
Но я лучше сделаю более читаемым через тройные строки в двойных кавычках

Вывод: стало гораздо лучше, читаемость отличная.


4) Имя функции должно быть в нижнем регистре.
Было:
    def print_True_or_False(
    value): ...

Стало:
    def print_true_or_false(
    value): ...

Вывод: лучше/хуже не стало, читаемость не изменилась.



Дополнительные правила PEP-8 и не только, на которые я также обратил внимание входе решения домашнего задания:
5) Создание классов.
Было:
    class A(): ...
Стало:
    class A(object):
или
    class А: ...


6) Отступ от классов, согласно PEP 8 (E302), должно быть 2 пустых строки как сверху, так и снизу.
7) Стиль имен классов должен быть CamelCase, то есть:
    CamelCaps
    CamelHumpedWord


8) PEP 8: W292 нет новой строки в конце файла.
Вывод: переходить на новую строку после написания строки кода, даже если код завершен в части написания.
"""







# список из 20 фильмов:
A = ["Дюна", "Зеленая миля", "Форрест Гамп", "Список Шиндлера", "Молчание ягнят",
     "Крестный отец", "Начало", "Джанго освобожденный", "Храброе сердце", "Дюна",
     "Брат 2", "Криминальное чтиво", "Изгой", "Назад в будущее", "Интерстеллар",
     "Темный рыцарь", "Джентльмены", "Матрица", "Остров проклятых", "Титаник"]

"""
A1 = [["Дюна", 2021], ["Зеленая миля", 1999], ["Форрест Гамп", 1994], ["Список Шиндлера", 1993], 
["Молчание ягнят", 1991], ["Крестный отец", 1972], ["Начало", 2010], ["Джанго освобожденный", 2013], 
["Храброе сердце", 1995], ["Дюна", 1984], ["Брат 2", 2000], ["Криминальное чтиво", 1994], ["Изгой", 2000], 
["Назад в будущее", 1985], ["Интерстеллар", 2014], ["Темный рыцарь", 2008], ["Джентльмены", 2020], 
["Матрица", 1999], ["Остров проклятых", 2010], ["Титаник", 1997]] 
"""

# словарь из тех же 20 фильмов с датой выпуска в прокат:
B = {"Дюна": 2021, "Зеленая миля": 1999, "Форрест Гамп": 1994, "Список Шиндлера": 1993, "Молчание ягнят": 1991,
     "Крестный отец": 1972, "Начало": 2010, "Джанго освобожденный": 2013, "Храброе сердце": 1995, "Дюна": 1984,
     "Брат 2": 2000, "Криминальное чтиво": 1994, "Изгой": 2000, "Назад в будущее": 1985, "Интерстеллар": 2014,
     "Темный рыцарь": 2008, "Джентльмены": 2020, "Матрица": 1999, "Остров проклятых": 2010, "Титаник": 1997}

# множество из тех же 20 фильмов, создаем из того же списка:
C = set(A)


# Выполняем поиск элемента по списку, словарю и множеству:
def print_true_or_false(
        value):  # функция, принимающая 1 bool-аргумент (True/False), возвращая итог поиска о запрашиваемом фильме
    if value:
        print("В данном списке/словаре/множестве есть запрашиваемый фильм.")
    else:
        print("В данном списке/словаре/множестве отсутствует запрашиваемый фильм.")


search_movie = input("Введите название фильма, который хотите найти:")  # просим пользователя ввести название фильма

# Поиск элемента по списку А:
print_true_or_false(search_movie in A)  # вызываем функцию

# Поиск элемента по словарю B:
print_true_or_false(search_movie in B)  # вызываем функцию

"""
В данном случае ключом является само название фильма, а значением - год выпуска фильма.
Мы также можем дополнительно определить год выпуска запрашиваемого фильма из словаря 
через метод setdefault (доступ к значению ключа):
"""

if search_movie in B:
    print(f'Дата выпуска фильма "{search_movie}" - {B.setdefault(search_movie)} год')  # форматирование через f''

# Поиск элемента по множеству С, аналогично списку:
print_true_or_false(search_movie in C)