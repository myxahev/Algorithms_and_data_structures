# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a, b, c = [int(x) for x in input('Введите 3 числа через пробел: ').split()]

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)