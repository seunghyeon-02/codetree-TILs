n = int(input())
k = 0

for i in range(1, n+1):
    if i % 2 == 0 or (i % 3 == 0 and i % 9 != 0) or i % 10 == 5:
        continue
    print(i, end =" ")