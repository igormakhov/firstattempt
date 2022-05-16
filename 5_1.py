kolvo = int(input('Сколько цыферок желаете увидеть? '))
kratn = int(input('И чему должны быть кратные? '))
granitsa = int(input('Начиная от какой? '))
i=0
a=granitsa+1
while a % kratn != 0:
    a+=1
else:
    kray = a + kolvo*kratn - 1
for n in range(granitsa+1,kray):
    if n % kratn == 0:
        print(n)
        i=i+1
        if i == kolvo:
            break
