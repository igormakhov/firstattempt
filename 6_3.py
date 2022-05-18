spisok = [1, 2, 3, 4, 5, 6]
n = int(input("введи смещение "))
dlina = len(spisok)
for a in range(n):
    posled = spisok[dlina-1]
    spisok.insert(0, posled)
    del spisok[dlina]

print(spisok)
