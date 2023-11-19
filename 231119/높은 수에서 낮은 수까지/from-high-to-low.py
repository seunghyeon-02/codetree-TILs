k = input()
l = k.split()

a = int(l[0])
b = int(l[1])

if a >= b:
    for i in range(a, b-1, -1):
        print(i, end = " ")
else:
    for i in range(b, a-1, -1):
        print(i, end =" ")