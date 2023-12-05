arr = list(map(int, input().split()))
n = len(arr)
sum1, sum2 = 0, 0

for i in range(n):
    if i % 2 == 1:
        sum2 += arr[i]
    else:
        sum1 += arr[i]

if sum1 > sum2:
    print(sum1 - sum2)
else:
    print(sum2 - sum1)