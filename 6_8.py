slovar = {'Ru': ('Mos','Spb', 'Kaz'), 'By': ('Min', 'Gro', 'Bre'), 'Lit': ('Vil', 'Kau', 'Pal')}
def naidi_gorod(text):
    i = input('Введи город ')
    a = slovar.keys()
    for b in a:
        n = slovar[b]
        for z in n:
            if z == i:
                print(b)
naidi_gorod(slovar)
