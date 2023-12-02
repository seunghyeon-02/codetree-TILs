n = int(input())
# i = 1234
for i in range(1, n+1):
    #i = 1 k= 1 // i = 2 k = 2 1 //
    for k in range(i, 0,-1):
        print(n+1-k, end = " ")
    print( )