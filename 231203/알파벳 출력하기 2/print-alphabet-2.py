n = int(input())
h = 65

for i in range(n):
    for k in range(i):
        print(" ", end =" ")
    for j in range(n-i):
        if h == 91:
            h = 65
        print(chr(h), end = " ")
        h += 1
    print( )