n = int(input())

for i in range(n):
    for k in range(n-i):
        print("*", end = " ")
    print( )
for i in range(2,n+1):
    for p in range(i):
        print("*", end = " ")
    print( )