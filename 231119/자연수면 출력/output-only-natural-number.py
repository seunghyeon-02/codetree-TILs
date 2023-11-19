k = input()
l = k.split()

a = int(l[0])
b = int(l[1])

if a>0 and a % 1 == 0:
    for i in range(b):
        print(a, end = "")
else:
    print(0)