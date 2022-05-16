perv = float(input('введи первое число '))
znak = input('введи действие ')
vtor = float(input('введи второе число '))
znach = 0
if znak == '+':
    znach = perv + vtor
elif znak == '-':
    znach = perv - vtor
elif znak == '*':
    znach = perv * vtor
elif znak == '/':
    znach = perv / vtor
print(znach)
