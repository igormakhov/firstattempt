spisok = [1, 4, 'kvmek', 'ree', 234, '312', [14, 15, 17], (656, 452354, 'eter'), 'trt', 31]
i = len(spisok)
for a in range(i):
    if not isinstance(spisok[a], str):
        del spisok[a]
        spisok.insert(a, '-')
while '-' in spisok:
    spisok.remove('-')
print(spisok)
