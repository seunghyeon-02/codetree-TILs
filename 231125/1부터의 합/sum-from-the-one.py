n = int(input())

sum1 =0

for i in range(1, 101):
    sum1 += i
    if sum1 >= n:
        break
print(i)