arr = list(map(int, input().split()))

comp_1 = 0
comp_2 = max(arr)
for i in range(len(arr)):
    if arr[i] <= 500 and arr[i] >= comp_1:
        comp_1 = arr[i]
    elif arr[i] >= 500 and arr[i] <= comp_2:
        comp_2 = arr[i]

print(f"{comp_1} {comp_2}")