k = input()
l = k.split()

a = int(l[0])
b = int(l[1])

if a>b:
    print(a*b)
else:
    print(b//a)