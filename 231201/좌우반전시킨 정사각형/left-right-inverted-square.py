n = int(input())

for i in range(1, n+1):
    for k in range(n, 0, -1):
        print(i*k,end =" ")
    print( )