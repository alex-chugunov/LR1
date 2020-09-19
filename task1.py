import math as mt

expr19 = 124 / ((45 * 3 + 7) - 2 / 5)
print(expr19)

a = float(input("Введите a: \n"))
b = float(input("Введите b: \n"))
c = float(input("Введите c: \n"))
d = float(input("Введите d: \n"))
e = float(input("Введите e: \n"))
m = float(input("Введите m: \n"))
n = float(input("Введите n: \n"))
p = float(input("Введите p: \n"))

try:
    ch1 = mt.pow(2, n) * (mt.sin(a) + mt.cos(b * c / mt.pow(d, m)))
    ch2 = mt.sin(a) + mt.cos(b * c / mt.pow(d, m))
    znm = mt.log10(mt.pow(a + b * c / mt.pow(d, m), 1 / 3)) - e / mt.pow(2, p)
    expr9 = ch1 * ch2 / znm
    print(expr9)
except:
    print("Ошибка!")
