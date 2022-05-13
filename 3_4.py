first = float(input("введи первое число "))
second = float(input("введи второе число "))
third = float(input("введи третье число "))
polozh = 0
otritsalovo = 0
nol = 0


if first == 0:
    nol = nol + 1
else:
    if first > 0:
        polozh = polozh + 1
    else:
        if first < 0:
            otritsalovo = otritsalovo + 1
if second == 0:
    nol = nol + 1
else:
    if second > 0:
        polozh = polozh + 1
    else:
        if second < 0:
            otritsalovo = otritsalovo + 1

if third == 0:
    nol = nol + 1
else:
    if third > 0:
        polozh = polozh + 1
    else:
        if third < 0:
            otritsalovo = otritsalovo + 1

print("Положительных", polozh)
print("Отрицательных", otritsalovo)
print("Нулей", nol)
