n = int(input())

arr = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(1+i+n*j)
    arr.append(row)

for m in range(n):
    for l in range(n):
        print(arr[m][l], end = " ")
    print( )