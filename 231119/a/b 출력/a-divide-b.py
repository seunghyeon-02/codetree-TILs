k = input()
l = k.split()

a = int(l[0])
b = int(l[1])

d = a // b
print(f"{d}.", end ="")

for i in range(20):
    c = 10 * (a % b)
    d = c // b
    print(f"{d}", end = "")
    a = c % b