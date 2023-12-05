n = int(input())

for i in range(1,n+1):
    for k in range(1,n+1):
        if i + k == 4:
            print(f"({i}, {k})")
        else:
            print(f"({i}, {k})", end =" ")