p = input()
l = p.split()

a = int(l[0])
b = int(l[1])

for k in range(1,10):
    for i in range(b,a-1,-2):
        print(f"{i} * {k} = {i*k}", end = " ")
        if i != a:
            print("/", end =" ")
    print( )