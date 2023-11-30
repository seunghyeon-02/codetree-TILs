k = input()
l = k.split()

a = int(l[0])
b = int(l[1])

for i in range(1, a+1):
    for k in range(1, b+1):
        print(i*k, end =" ")
    print( )