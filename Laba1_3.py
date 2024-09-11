a = [int(i) for i in input().split()]

s = 0

for i in a:
    if i > 0:
        s += i
print("Сумма положительных элементов списка: ", s)

n1 = -1
n2 = -1
s = 0

for i in range(len(a)):
    if a[i] == 0 and n1 == -1:
        n1 = i
    elif a[i] == 0 and n2 == -1:
        n2 = i
    if n1 != -1 and n2 == -1:
        s += a[i]
if (n1 == -1 or n2 == -1):
    print("Меньше двух нулей")
else:
    print("Сумма между первыми двумя нулями: ", s)
