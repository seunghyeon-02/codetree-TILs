k = input()
l = k.split()

a = int(l[1])
b = int(l[0])

if b % 2 == 0:
    for i in range (b-1, a-1, -2):
        print(i, end = " ")
elif b % 2 != 0:
    for i in range (b, a-1, -2):
        print(i, end = " ")