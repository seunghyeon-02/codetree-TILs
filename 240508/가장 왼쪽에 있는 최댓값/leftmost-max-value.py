n = int(input())
arr = list(map(int, input().split()))
a1 = arr[0]

for i in range(n):
    if len(arr) == 1:
        print(1, end =" ")
        break
    else:
        max_a = max(arr)
        location_a = arr.index(max_a)
        print(location_a+1, end = " ")
        arr = arr[:location_a]