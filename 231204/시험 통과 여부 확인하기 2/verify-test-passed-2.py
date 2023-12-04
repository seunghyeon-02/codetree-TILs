n = int(input())
cnt = 0
for i in range(n):
    sum1 = 0
    arr = list(map(int, input().split( )))
    sum1 = sum(arr)
    if sum1 / 4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)