k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
c = int(l[2])
first = 0
second = 0

if a == min(a, b, c):
    first += 1
elif a == b and b == c:
    second += 1
print(first, second)