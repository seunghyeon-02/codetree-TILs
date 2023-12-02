l = input()
m = l.split()

a = int(m[0])
b = int(m[1])

for i in range(2, 9, 2):
    for k in range(b, a-1, -1):
        print(f"{k} * {i} = {i*k}", end = " ")
        if k != a:
            print("/", end = " ")
    print( )