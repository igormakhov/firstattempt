def perevorot(spisok):
    dlina = len(spisok)
    for a in range(dlina):
        posled = spisok[dlina-1]
        spisok.insert(a, posled)
        del spisok[dlina]
    print(spisok)

perevorot([1, 2, 3, 4, 5, 6])
