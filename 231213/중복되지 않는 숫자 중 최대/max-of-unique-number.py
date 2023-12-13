n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    m = max(arr)
    k = arr.count(m)
    if k >= 2:
        for i in range(k):
            arr.remove(m)
        if len(arr) == 0:
            print(-1)
            break
    else:
        print(max(arr))
        break