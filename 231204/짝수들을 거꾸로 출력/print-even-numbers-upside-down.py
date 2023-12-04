n = int(input())
arr = list(map(int, input().split( )))
cnt = 0
arr2 = list()
for i in range(n):
    if arr[i] % 2 == 0:
        arr2.append(arr[i])
        cnt += 1

for j in range(cnt-1,-1,-1):
    print(arr2[j], end = " ")