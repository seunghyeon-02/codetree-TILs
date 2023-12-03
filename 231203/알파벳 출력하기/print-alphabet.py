n = int(input())
j = 65
for i in range(n):
    for k in range(i+1):
        if j == 91:
            j = 65
            print(chr(j), end ="")
            j += 1
        else:
            print(chr(j), end ="")
            j += 1
    print( )