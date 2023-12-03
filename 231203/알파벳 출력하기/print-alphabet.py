n = int(input())
j = 65
for i in range(n):
    for k in range(i+1):
        print(chr(j), end ="")
        j += 1
    print( )