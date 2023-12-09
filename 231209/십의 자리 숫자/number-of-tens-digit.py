arr = list(map(int, input().split()))
count_arr = [0] * 9

n = len(arr)
for i in range(n):
    if arr[i] == 0:
        arr = arr[:i]
        break

n1 = len(arr)
for k in range(n1):
    if arr[k] >= 10:
        cnt = arr[k] // 10
        count_arr[cnt-1] += 1

for j in range(1,10):
    print(f"{j} - {count_arr[j-1]}")