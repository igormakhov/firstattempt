first = float(input("введи первое число "))
second = float(input("введи второе число "))
third = float(input("введи третье число "))
srednee = float(int((first + second + third)/3*1000)/1000)
print("Среднее арифметическое =", srednee)
srednee_2 = str((first + second + third)/3*1000)
print(srednee_2[0:4])
srednee_3 = (round(float((first + second + third)/3), 3))
print(srednee_3)
