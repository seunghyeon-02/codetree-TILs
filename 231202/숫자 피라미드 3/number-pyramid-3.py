n = int(input())

for i in range(1, n+1):
    for k in range(i):
        print(i*(k+1), end = " ")
    print( )