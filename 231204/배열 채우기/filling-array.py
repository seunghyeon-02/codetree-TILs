n = input()
arr = list(map(int, n.split()))
cnt = 0

for i in range(len(arr)):
    k = arr[i]
    if k == 0:
        arr = arr[0:i]
        break
    else:
        cnt = i

for j in range(cnt,-1, -1):
    print(arr[j], end =" ")