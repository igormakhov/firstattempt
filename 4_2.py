spisok_1 = []
text = input('Введи много слов ')
spisok_1.extend(text)
print({("a", spisok_1.count("a")), ("b", spisok_1.count("b")), ("c", spisok_1.count("c"))})#первый вариант, неправильный явно

dlina_spiska = len(spisok_1)
slovar = {}
for n in range(0,dlina_spiska):
    item = spisok_1[n]
    slovar[item] = spisok_1.count(item)
print(slovar)

text = input('вводи')
counter = {symbol: text.count(symbol) for symbol in text}
print(counter)
