arr = list(map(int, input().split()))

k = 0
n = len(arr)

for i in range(n):
    if arr[i] == 0:
        k = i
        break

print(sum(arr[k-3:k]))