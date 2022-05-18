slovar = {'Ru': ('Mos','Spb', 'Kaz'), 'By': ('Min', 'Gro', 'Bre'), 'Lit': ('Vil', 'Kau', 'Pal')}
i = input('Введи город ')
a = slovar.keys()
for b in a:
    n = slovar[b]
    for z in n:
        if z == i:
            print(b)
