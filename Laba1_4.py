d = {'a':0,
       'b':0,
       'c':0,
       'd':0,
       'e':0,
       'f':0,
       'g':0,
       'h':0,
       'i':0,
       'j':0,
       'k':0,
       'l':0,
       'm':0,
       'n':0,
       'o':0,
       'p':0,
       'q':0,
       'r':0,
       's':0,
       't':0,
       'u':0,
       'v':0,
       'w':0,
       'x':0,
       'u':0,
       'z':0
    }
d1 = d.copy()

s = input()
s1 = input()

for i in s:
    d[i]+=1
for i in s1:
    d1[i]+=1

t = True

for i in d.keys():
    if d[i] != d1[i]:
        print("Данные слова не являеются анаграмами")
        t = False
        break
if (t):
    print("Данные слова являеются анаграмами")

    
    
