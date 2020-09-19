import math
try:
    print("Введите коэффициенты уравнения:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(a, "x^2+", b, "x", "+", c)
    dis = b ** 2 - 4 * a * c
    print("Дискриминант = " + str(dis))

    if dis == 0:
        x = -b / (2 * a)
        print("x = " + str(x))
    elif dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
    else:
        print("Комплексные корни")
except:
    print("Ошибка!")
