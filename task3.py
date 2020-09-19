import numpy as np
import random as rnd


def Func(ls):
    print("Максимальное число в массиве: " + str(max(ls)))
    print("Минимальное число в массиве: " + str(min(ls)))
    print("Сумма элементов в массиве: " + str(sum(ls)))


# main function
print("Задача №3")
try:
    raz = int(input("Введите размер массива: \n"))
    a = [] * raz  # создание массива вручную
    for i in range(raz):
        a.append(int(input("Введите число " + str(i + 1) + " из " + str(raz) + ":\n")))
    Func(a)
    b = rnd.sample(range(100), raz)  # второй массив с случайными числами с заранее заданным размером
    Func(b)
    c = np.arange(raz)  # создание массивов при помощи numpy
    print(c)
    d = np.zeros(raz)
    print(d)
    e = np.array(99)
    print(e)
except:
    print("Ошибка!")
