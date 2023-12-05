n = int(input())
k = 1
for i in range(1,n+1):
    if i % 2 == 1:
        for j in range(n):
            print(k,end = " ")
            k += 1
        print( )
    else:
        for h in range(n):
            print(k,end =" ")
            k += 1
        print( )