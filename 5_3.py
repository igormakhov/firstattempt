n = int(input('До чего надо? '))
if n % 2 == 0:
    finish = n
else:
    finish = n - 1
spisok = []
for a in range(2,finish,10):
    for i in range(a,a+10,2):
        spisok.append(i)
    print(spisok)
    spisok = []



