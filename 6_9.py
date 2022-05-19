slovar = {'Uasya': {'Imya': 'Vasya', 'Familiya': 'Petrov', 'E-mail': 'pes@kot.ru'},
          'Petya': {'Imya': 'Pyotr', 'Familiya': 'Ivanov', 'E-mail': ''},
          'Lena': {'Imya': 'Elena', 'Familiya': 'Vasina', 'E-mail': 'len@los.ru'},
          'Zhanna': {'Imya': 'Snezhanna', 'Familiya': 'Petina'},
          'Olezha': {'Imya': 'Oleg', 'Familiya': 'Uzki', 'E-mail': 'poleg@zab.ru'}}
a = slovar.keys()
for i in a:
    slovar_1 = slovar[i]
    c = slovar_1.get('E-mail')
    if c is None or len(c) == 0:
        print(i)




