n = int(input())

for i in range (1, n+1):
    k = n / i
    if k <= 1:
        break
    n = k
print(i)