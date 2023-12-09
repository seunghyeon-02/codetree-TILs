arr = list(map(int, input().split()))
count_arr = [0] * 7

for i in range(1,7):
    if i in arr:
        count_arr[i] += arr.count(i)
    
    print(f"{i} - {count_arr[i]}")