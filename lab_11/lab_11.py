import math
import random
import datetime

# Math, random, datetime, Canvas модульдерін қолданып әр модульден 5  функцияны қолданып бағдарлама жазу.
x = 5.67                                                  # Дробный номер
print("Верхний предел:", math.ceil(x))                    # выводим целую часть числа с округлением к большему
print("Нижний предел:", math.floor(x))                    # выводим целую часть числа с округлением к меньшему
print("Факториал числа: ", math.factorial(int(x)))        # вывод факториала
print("e в степени 5.67: ", math.exp(x))                  # вывлдим степень экспоненты
print('5.67 градиан в градусе: ', math.degrees(x))        # конвертирует радиан в градусы

num = [1, 2, 3, 4, 5, 6, 7]
print("Вывод случайного целого числа: ", random.randint(0, 9))
print("Вывод случайного целого числа: ", random.randrange(0, 10, 2))
print("Вывод случайного числа от 0 до 1: ", random.random())
sampling = random.choices(num, k=5)
print("Выборка с методом choices ", sampling)
random.shuffle(num)
print("Вывод перемешанного списка ", num)

today = datetime.datetime.now()
print("Current date time: ", today)
delta = datetime.timedelta(weeks=5, days=5)
date = today + delta
print("After 5 weeks and 2 days is: ", date.day, ':', date.month, ':', date.year)
delta = datetime.timedelta(days=100)
date = today - delta
print("100 days before was: ", date.day, ':', date.month, ':', date.year)
delta = datetime.timedelta(hours=2, minutes=30, seconds=55)
date = today + delta
print("After 2 hours and 30 minutes is: ", date.hour, ':', date.minute, ':', date.second)

