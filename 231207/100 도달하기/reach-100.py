n = int(input())
arr = [1, n]

new_num = 0
new_arr =[]
i = 0
while True:
    if new_num >= 100:
        break
    else:
        new_num = arr[i]+arr[i+1]
        i += 1
        arr.append(new_num)

k = len(arr)
for j in range(k):
    print(arr[j], end =" ")