n = int(input())

for i in range(1,n+1):
    for k in range(1,n+1):
        print(f"{i} * {k} = {i*k}", end = "")
        if k != n:
            print(",", end = " ")
    print( )