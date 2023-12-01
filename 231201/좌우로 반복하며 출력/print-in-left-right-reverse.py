n = int(input())
for i in range(1,n+1):
    if i % 2 ==1:
        for k in range(1,n+1):
            print(k,end = "")
    else:
        for j in range(n):
            print(n-j,end = "")
    print( )