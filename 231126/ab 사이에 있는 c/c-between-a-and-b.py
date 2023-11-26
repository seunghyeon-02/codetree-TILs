k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
c = int(l[2])
cnt = 0
for i in range(a, b+1):
    for k in range(1,100):
        if i == c*k:
            cnt += 1
        else:
            continue
if cnt >= 1:
    print("YES")
else:
    print("NO")