spisok = [1, 2, 3, 4, 5, 6]
dlina = len(spisok)
print(spisok[dlina-1])

for a in range(dlina):
    posled = spisok[dlina-1]
    spisok.insert(a, posled)
    del spisok[dlina]
print(spisok)
