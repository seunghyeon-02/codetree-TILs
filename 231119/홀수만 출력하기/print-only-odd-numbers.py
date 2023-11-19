n = int(input())
i = 1

while i <= n:
    k = int(input())
    if k % 3 == 0 and k % 2 == 1:
        print(k)
        i += 1
    else:
        i += 1