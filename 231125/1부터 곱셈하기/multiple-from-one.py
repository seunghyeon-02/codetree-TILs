n = int(input())
k =1
for i in range(1, 10):
    k *= i
    if k >= n:
        break
print(i)