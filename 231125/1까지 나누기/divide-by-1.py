n = int(input())

for  i in range (1, n):
    k = n / i
    n = k
    if k <= 1:
        break
print(i)