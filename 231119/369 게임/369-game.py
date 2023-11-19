n = int(input())
i = 1
while i <= n:
    if i % 3 != 0:
        print(i, end =" ")
        i += 1
    else:
        print(0, end = " ")
        i += 1