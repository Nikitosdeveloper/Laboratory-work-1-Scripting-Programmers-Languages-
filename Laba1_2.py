s = input()

k = 0

for i in range(len(s)-1):
    if str(s[i]).islower() and str(s[i+1]).islower():
        k += 1
    elif str(s[i]).isupper() and str(s[i+1]).isupper():
        k += 1
print(k)
