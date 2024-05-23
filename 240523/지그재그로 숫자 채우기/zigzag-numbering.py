arr_n_m = list(map(int, input().split()))
n = arr_n_m[0]
m = arr_n_m[1]
arr = []

for i in range(n):
    row = []
    row.append(i)
    arr.append(row)

for k in range(1,m):
    if k % 2 == 1:
        count = arr[n-1][k-1]
        for j in range(n):
            count += 1
            arr[n-j-1].append(count)

    else:
        count = arr[0][k-1]
        for j in range(n):
            count += 1
            arr[j].append(count)


for h in range(n):
    for s in range(m):
        print(arr[h][s], end = " ")
    print( )