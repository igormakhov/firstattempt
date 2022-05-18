spisok = [1, 4, 2, 8, 100, 13, 26, 10]
spisok_nech = []
spisok_chetn = []
for n in spisok:
    if n % 2 == 0:
        spisok_chetn.append(n)
    else:
        spisok_nech.append(n)
a = sorted(spisok_chetn)
b = sorted(spisok_nech)
a.extend(b)
print(a)


