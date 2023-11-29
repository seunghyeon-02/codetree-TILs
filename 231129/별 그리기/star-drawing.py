n = int(input())

for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end = "")
    for j in range(2*i-1):
        print("*", end = "")
    print( )
for p in range(1, n):
    for h in range(p):
        print(" ", end = "")
    for l in range(2*(n-p)-1):
        print("*", end = "")
    print( )