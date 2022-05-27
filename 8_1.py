text = ['я запишу здесь кучу слов, они мне нужны для программы.',
        'большую кучу слов, а не маленькую. Совсем большую кучу. Они пригодятся. И не только мне.',
        'я буду писать из этих слов матрицу из слов. Будет ОЧень много слов.'
]
mega_nov_spisok = []
for s in range (0, len(text)):
        stroka = str(text[s]).lower()
        spisok = list(stroka)
        for i in spisok:
                if i.isalpha() or i == ' ':
                        continue
                else:
                        spisok.remove(i)
        nov_spisok = f"{''.join(spisok)}"
        sam_nov_spisok = nov_spisok.split()
        for a in range(0, len(sam_nov_spisok)):
                if len(sam_nov_spisok[a]) > 2:
                        mega_nov_spisok.append(sam_nov_spisok[a])
slovar = {}
for u in range(0, len(mega_nov_spisok)):
        z = mega_nov_spisok[u]
        d = [mega_nov_spisok.count(z)]
        slovar[z] = d
print(slovar)

