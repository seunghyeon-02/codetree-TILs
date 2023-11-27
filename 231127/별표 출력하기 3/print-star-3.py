n = int(input())

for i in range (n):
    for p in range(i):
        print(" ", end =" ")
    for k in range (2*(n-i)-1):
        print("*", end = " ")
    print( )