n = int(input())
cnt = 1
cnt_0 = 0
for i in range(1,n+1):
    if i % 2 ==1:
        for k in range(n):
            print(cnt,end =" ")
            cnt += 1
        print( )
    else:
        for j in range(1,n+1):
            print(cnt-j+n, end =" ")
        cnt += n            
        print( )