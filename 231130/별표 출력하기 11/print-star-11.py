n = int(input())

for i in range(1,2*n+2):
    if i % 2 == 1:
        for k in range(2*n+1):
            print("*", end =" ")
        print( )
    if i % 2 == 0:
        for p in range(n+1):
            print("*", end =" ")
            print(" ", end =" ")
        print( )