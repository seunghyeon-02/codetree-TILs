k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
sum_5 = 0

for i in range(a, b+1):
    if i % 5 == 0:
        sum_5 += i
print(sum_5)