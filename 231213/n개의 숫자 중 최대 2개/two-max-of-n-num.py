n = int(input())

arr = list(map(int, input().split()))
max_a = max(arr)
arr.remove(max_a)

print(max_a, end =" ")
print(max(arr))