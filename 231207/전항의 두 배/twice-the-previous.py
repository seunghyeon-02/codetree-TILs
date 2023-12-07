arr = list(map(int, input().split()))

i = 0
n = 0
while True:
    if n == 10:
        break
    else:
        new_num = 2 * arr[i] +arr[i+1]
        i += 1
        arr.append(new_num)
        n = len(arr)

for k in range(n):
    print(arr[k], end = " ")