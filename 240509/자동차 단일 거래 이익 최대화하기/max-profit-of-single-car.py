n = int(input())

arr = list(map(int, input().split()))

profit = 0

for i in range(n):
    for j in range(i+1,n):
        comp_1 = arr[j] - arr[i]
        if comp_1 >= 0 and comp_1 >= profit:
            profit = comp_1

print(profit)