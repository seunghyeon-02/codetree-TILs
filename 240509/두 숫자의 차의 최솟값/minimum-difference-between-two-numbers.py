n =int(input())

arr = list(map(int, input().split()))

min_num = max(arr)

for i in range(n):
    for j in range(i+1,n):
        comp_num = arr[i] - arr[j]
        if comp_num <= 0:
            comp_num = -comp_num

        if comp_num <= min_num:
            min_num = comp_num
print(min_num)