k = input()
l = k.split()

a = int(l[0])
b = int(l[1])

if a<b:
    print(1, end = " ")
else:
    print(0, end = " ")

if a == b:
    print(1, end = " ")
else:
    print(0, end = " ")