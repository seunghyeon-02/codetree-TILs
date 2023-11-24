k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
k = 1
for i in range(a, b+1):
    k *= i
print(k)