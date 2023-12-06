arr = list(map(int, input().split()))
new_arr = []
for i in range(10):
    new_arr.append((arr[i]+arr[i+1]) % 10)
    arr.append(new_arr[i])
    print(arr[i],end =" ")