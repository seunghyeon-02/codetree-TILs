k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
t = 1
f = 1
cnt = 0

while t <= 1920:
    if 1920 % t == 0 and 2880 % t == 0:
        for i in range(a, b+1):
            if i == t:
                cnt += 1
        t += 1
    else:
        t += 1



if cnt >= 1:
    print(1)
else:
    print(0)