n = int(input())
k =0

for i in range(1,n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        k += 1

print(n-k)