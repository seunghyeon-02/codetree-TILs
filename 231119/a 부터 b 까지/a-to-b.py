k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
print(a, end =" ")
for i in range(a, 30):
    if a >= b:
        break
    elif a % 2 == 0:
        a += 3
        print(a, end =" ")
    else:
        a *= 2
        print(a,end =" ")