n = int(input())

arr = list(map(int, input().split()))
count_arr = [0] * 9

for i in range(1,10):
    cnt = 0
    for elem in arr:
        if elem == i:
            count_arr[elem-1] += 1
    print(count_arr[i-1])