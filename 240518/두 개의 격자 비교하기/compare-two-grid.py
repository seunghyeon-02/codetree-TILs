arr_n_m = list(map(int, input().split()))
n = arr_n_m[0]
m = arr_n_m[1]

arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

arr_2 = []
for i in range(n):
    row = list(map(int, input().split()))
    arr_2.append(row)


result_arr = []
for k in range(n):
    result_row =[]
    for j in range(m):
        if arr[k][j] != arr_2[k][j]:
            result_row.append(1)
        else:
            result_row.append(0)
    result_arr.append(result_row)

for j in range(n):
    for k in range(m):
        print(result_arr[j][k], end = " ")
    print( )