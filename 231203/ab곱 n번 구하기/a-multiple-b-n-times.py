n = int(input())
cnt =1
for i in range(n):
    k = input()
    l = k.split()
    a = int(l[0])
    b = int(l[1])
    for j in range(a,b+1):
        cnt *= j
    print(cnt)
    cnt = 1