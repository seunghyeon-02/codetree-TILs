arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    if i == 999 or i == -999:
        arr = arr[:cnt] 
        break
    else:
        cnt += 1

print(f"{max(arr)} {min(arr)}")