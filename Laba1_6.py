a = [int(i) for i in input().split()]
a = tuple(a)

Min = a[0]

for i in range(1,len(a),2):
    if a[i] < Min:
        Min = a[i]

print(Min)