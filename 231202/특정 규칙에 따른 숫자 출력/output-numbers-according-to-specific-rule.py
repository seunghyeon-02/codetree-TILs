n = int(input())
cnt = 1
for i in range(n):
    if cnt == 10:
        cnt = 1
    for j in range(i):
        print(" ", end = " ")
    for k in range(n-i):
        print(cnt, end =" ")
        cnt += 1
    print( )