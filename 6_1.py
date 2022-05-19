a = int(input('inp  '))
i = ''
while a > 0:
    i = str(a % 2) + i
    a = a//2
    print(a)
print(i)
while len(i) < 8:
    i = i + '0'# посмотреть кула надо добавлять нули - вперёд или назад, если вперёд - поменять слагаемые местами
print(i)
