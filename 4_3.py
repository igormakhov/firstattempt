kol_vo = int(input('введите кол-во абонентов '))
slovar_raz = {}
slovar_dva = {}
for i in range(0, kol_vo):
    name = input("введите имя ")
    email = input("введите почту ")
    slovar_raz[name] = email
    slovar_dva[i] = slovar_raz.popitem()
print(slovar_dva)

