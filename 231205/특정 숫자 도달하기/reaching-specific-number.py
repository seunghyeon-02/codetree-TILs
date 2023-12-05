arr = list(map(int, input().split( )))
k = 0
for i in range(10):
    if arr[i] >=250:
        break
    else:
        k += 1
arr = arr[:k]
s = sum(arr)
print(sum(arr),end = " ")
print(f"{(s/k):.1f}")