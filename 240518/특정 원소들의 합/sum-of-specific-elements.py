arr =[]
for k in range(4):
    row = list(map(int, input().split()))
    arr.append(row)
    
sum_arr = 0

for i in range(4):
    for j in range(i+1):
        sum_arr += arr[i][j]

print(sum_arr)