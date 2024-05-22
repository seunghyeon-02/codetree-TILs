arr = list(map(int, input().split()))

n = arr[0]
m = arr[1]

pri_arr = []
num = 1

for i in range(n):
    
    row = []    
    for j in range(m):
        row.append(num)
        num += 1
    pri_arr.append(row)


for k in range(n):
    for h in range(m):
        print(pri_arr[k][h], end = " ")
    print()