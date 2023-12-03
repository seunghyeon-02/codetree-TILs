n = int(input())

for i in range(n):
    k = input()
    l = k.split()

    a = int(l[0])
    b = int(l[1])
    cnt = 0
    for j in range(a, b+1):
        if j % 2 == 0:
            cnt += j
    print(cnt)