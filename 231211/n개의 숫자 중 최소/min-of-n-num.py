n = int(input())
arr = list(map(int, input().split()))
print(f"{min(arr)} {arr.count(min(arr))}")