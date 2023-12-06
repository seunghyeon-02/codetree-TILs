n = int(input())

arr = list(map(int, input().split()))
new_arr = []

for i in range(n):
    new_arr.append(arr[i]**2)
    print(new_arr[i], end =" ")