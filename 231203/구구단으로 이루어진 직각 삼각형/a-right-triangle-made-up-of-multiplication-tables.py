n = int(input())

for i in range(n):
    for k in range(1,1+n-i):
        if k == n-i:
            print(f"{i+1} * {k} = {(i+1)*k}",end =" ")
        else:
            print(f"{i+1} * {k} = {(i+1)*k}", end =" ")
            print("/", end =" ")
    print( )