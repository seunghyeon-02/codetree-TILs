n = int(input())

for i in range(n):
    for k in range(n):
        print(f"({n-i},{n-k})", end =" ")
    print( )