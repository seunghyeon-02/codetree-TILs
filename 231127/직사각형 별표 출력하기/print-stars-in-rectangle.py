k = input()
l = k.split()

n = int(l[0])
m = int(l[1])

for i in range(n):
    for p in range(m-1):
        print("*", end = " ")
    print("*")