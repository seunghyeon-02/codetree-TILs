arr = []
arr_2 = []

n = 3
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

space = input()

for k in range(n):
    row_2 = list(map(int, input().split()))
    arr_2.append(row_2)

result_arr = []

for m in range(n):
    row_result = []
    for l in range(n):
        result = arr[m][l] * arr_2[m][l]
        row_result.append(result)
    result_arr.append(row_result)

for j in range(n):
    for h in  range(n):
        print(result_arr[j][h], end = " ")
    print( )