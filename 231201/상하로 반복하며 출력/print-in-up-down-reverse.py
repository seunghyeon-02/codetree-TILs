n = int(input())

for i in range(1,n+1):
    if n % 2 == 0:
        for k in range(n//2):
            print(i, end = "")
            print(n-i+1, end ="")
    else:
        for j in range((n-1)//2):
            print(i, end="")
            print(n-i+1, end = "")
        print(i, end ="")
    print( )