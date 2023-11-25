n = int(input())

for  i in range (1, n):
    k = n / i
    if k <= 1:
        break
    n = k
print(i)