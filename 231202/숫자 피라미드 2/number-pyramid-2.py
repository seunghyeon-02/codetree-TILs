n = int(input())
cnt = 1
for i in range(1, n+1):
    for k in range(i):
        print(cnt, end = " ")
        cnt += 1
    print( )