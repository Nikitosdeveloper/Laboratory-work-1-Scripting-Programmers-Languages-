from math import sqrt

def isSimple(a):
    for i in range(2,round(sqrt(a))+1):
        if a % i == 0:
            return False
    return True


a, b = [int(i) for i in input().split(' ')]

for i in range(a,b+1):
    if (isSimple(i)):
        print(i)
