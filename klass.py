stroka = input()
spisok = []
for unik in stroka:
    symbol = stroka.count(unik)
    if symbol == 1:
        spisok.append(unik)
print(spisok)
