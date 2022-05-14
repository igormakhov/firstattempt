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

text = input().lower().replace(' ','')
glasnye = ("a", "e", "u", "i", "o")
obshee = len(text)
glas = 0
neglasnye = 0
for i in range(0, obshee):
    if text[i].isalpha():# проверить чтобы убирало не буквы!!!!!!!!!!!!!!!!!!!
        if text[i] in glasnye:
            glas = glas + 1
        else:
            neglasnye = neglasnye + 1
print('Гласных', glas)
print('Негласных', neglasnye)


