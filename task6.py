st = input("Введите число: ")
n = int(st[-2:])
if n % 10 == 0 or n % 10 in range(5,10) or n // 10 == 1:
     print(st + " программистов")
elif n % 10 == 1:
     print(st + " программист")
else:
     print(st + " программиста")