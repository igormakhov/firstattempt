stroka = input()
spisok = []
for unik in stroka:
    symbol = stroka.count(unik)
    if symbol == 1:
        spisok.append(unik)
print(spisok)

slovo = input("слово").lower().replace(' ', '')
if slovo == slovo[::-1]:
    print('Правда')
else:
    print("Херня")
print("Совсем правда" if slovo == slovo[::-1] else "Совсем неправда")
