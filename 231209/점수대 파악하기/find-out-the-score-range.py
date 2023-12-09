arr = list(map(int, input().split()))
count_arr = [0] * 10

for i in range(100):
    if arr[i] == 0:
        arr = arr[i]
        break

n = len(arr)

for i in range(n):
    if arr[i] >= 10:
        k = arr[i] // 10
        count_arr[k-1] += 1

for j in range(1,10):
    print(f"{10*j} - {count_arr[j-1]}")