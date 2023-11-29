n = int(input())

for i in range(n):
    for k in range(n-i-1):
        print(" ", end ="")
    for j in range(i+1):
        print("*", end =" ")
    print( )
for h in range(n-1):
    for p in range(h+1):
        print(" ", end = "")
    for l in range(n-h-1):
        print("*", end =" ")
    print( )