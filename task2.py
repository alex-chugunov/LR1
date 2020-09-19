bil = input("Введите номер билета: \n")
try:
    if len(bil) % 2 == 0:
        half = len(bil) // 2
        a = bil[:half]
        b = bil[half:]
        sum_a = (sum(map(int, a)))
        sum_b = (sum(map(int, b)))
        if abs(sum_a - sum_b) == 0:
            print("Счастливый")
        elif abs(sum_a - sum_b) == 1:
            print("Встречный")
        else:
            print("Обычный")
    else:
        print("Ошибка! Номер билета нечётный!")
except:
    print("Ошибка!")
