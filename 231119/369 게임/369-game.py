n = int(input())
i = 1
k = "3"
l = "6"
m = "9"
while i <= n:
    if i % 3 != 0:
        i = str(i)
        if k in i:
            print(0, end = " ")
            i = int(i) + 1
        elif l in i:
            print(0, end = " ")
            i = int(i) + 1
        elif m in i:
            print(0, end = " ")
            i = int(i) + 1   
        else:
            i = int(i)
            print(i, end =" ")
            i += 1
    else:
        print(0, end = " ")
        i += 1