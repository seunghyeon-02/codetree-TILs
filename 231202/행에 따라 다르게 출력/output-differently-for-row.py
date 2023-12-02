n = int(input())
cnt = 1
for i in range(1,n+1):
    if i % 2 == 1:
        for j in range(1,n+1):
            print(cnt, end =" ")
            cnt += 1
        cnt += 1
        print( )
    if i % 2 == 0:
        for k in range(1,n+1):
            print(cnt,end = " ")
            cnt += 2
        cnt -= 1
        print( )