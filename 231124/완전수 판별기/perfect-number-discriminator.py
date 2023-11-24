n = int(input())

k = 0
for i in range(1,n):
    if n % i == 0:
        k += i

if k == n:
    print("P")
else:
    print("N")