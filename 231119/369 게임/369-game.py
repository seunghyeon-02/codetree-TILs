n = int(input())
i = 1
while i <= n:
    if i % 3 != 0:
        if 30<= i <= 39:
            print(0)
        else:
            print(i, end =" ")
            i += 1
    else:
        print(0, end = " ")
        i += 1