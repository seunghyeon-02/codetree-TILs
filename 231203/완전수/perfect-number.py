k = input()
l = k.split()

a = int(l[0])
b = int(l[1])

cnt = 0

for i in range(a,b+1):
    h = i
    for j in range(1,i):
        if i % j == 0:
            h -= j
    if h == 0:
        cnt += 1

print(cnt)