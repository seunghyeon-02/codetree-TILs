arr = list(map(int, input().split()))

n = len(arr)
k = 0
l = 0
cnt = 0
for i in range(n):
    if i % 2 == 1:
        k += arr[i]
        
    
    if i % 3 == 2:
        l += arr[i]
        cnt += 1

print(f"{k} {(l)/cnt:.1f}")