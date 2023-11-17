k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
if a%2 == 0:
    for i in range (a+1,b+1,2):
        print(i, end = " ")
else:
    for i in range (a,b+1,2):
        print(i, end = " ")