# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input("Введите трехзначное число: "))
print('Сумма цифр =', a//100 + (a % 100) // 10 + a%10)
print('Произведение цифр =', (a//100) * ((a % 100) // 10) * (a%10))