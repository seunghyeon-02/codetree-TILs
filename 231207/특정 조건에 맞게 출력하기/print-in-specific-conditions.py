arr = list(map(int, input().split()))

n = len(arr)

new_arr = []

for i in range(n):
    new_num = 0
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        new_num = arr[i] // 2
        new_arr.append(new_num)
    else:
        new_num = arr[i] + 3
        new_arr.append(new_num)
        
k = len(new_arr)

for j in range(k):
    print(new_arr[j], end = " ")