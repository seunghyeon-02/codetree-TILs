n = int(input())
cnt = 2
for i in range(n):
    for k in range(n):
        if cnt == 10:
            cnt = 2
        print(cnt, end =" ")
        cnt += 2
    print( )