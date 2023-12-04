arr = list(map(int, input().split( )))
k = 10
cnt = 0
cnt_num =0
for i in range(10):
    if arr[i] == 0:
        arr = arr[:i]
        k = i
        break
    else:
        arr = arr

for j in range(k):
    if arr[j] % 2 == 0:
        cnt += arr[j]
        cnt_num += 1
print(f"{cnt_num} {cnt}")