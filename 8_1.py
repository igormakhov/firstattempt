text = ['я запишу здесь кучу слов, они мне нужны для программы.',
        'большую кучу слов, а не маленькую. Совсем большую кучу. Они пригодятся. И не только мне.',
        'я буду писать из этих слов матрицу из слов. Будет ОЧень много слов.'
]
stroka = str(text[1]).lower()
spisok = list(stroka)
for i in spisok:
        if i.isalpha() or i == ' ':
                continue
        else:
                spisok.remove(i)
print(stroka)
print(spisok)
nov_spisok = f"{''.join(spisok)}"
print(nov_spisok)
sam_nov_spisok = nov_spisok.split()
print(sam_nov_spisok)
mega_nov_spisok = []
dlina_nov = len(sam_nov_spisok)
for a in range(0, dlina_nov):
        if len(sam_nov_spisok[a]) > 2:
               mega_nov_spisok.append(sam_nov_spisok[a])
print(mega_nov_spisok)
mega_dlina = len(mega_nov_spisok)
slovar = {}
for u in range(0, mega_dlina):
        z = mega_nov_spisok[u]
        d = mega_nov_spisok.count(z)
        slovar[z] = d
print(slovar)

# slovar = {}
# dlina = len(text)
# for i in range(0, dlina):
#         slovar[text[i]] = i
# print(slovar)
