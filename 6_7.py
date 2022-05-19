spisok = [1, 3, 10, 5, 20, 1, 4, 15]
def schyot_3(spis):
    dlina = len(spisok)
    for i in range(dlina-1):
        if i < dlina and i != 0:
            a = spisok[i] + spisok[i-1] + spisok[i+1]
        elif i == 0:
            a = spisok[i] + spisok[i+1] + spisok[dlina-1]
        elif i == dlina:
            a = spisok[i-1] + spisok[dlina-1] + spisok[0]
schyot_3(spisok)
