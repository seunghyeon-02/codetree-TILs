k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
c = int(l[2])

if a>b>c or c>b>a:
    print(b)
elif a>c>b or b>c>a:
    print(c)
else:
    print(a)