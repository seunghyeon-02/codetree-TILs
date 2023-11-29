n = int(input())
#n = 4 i = 12345678
for i in range(1,2*n+1):
    # i = 1357
    if i % 2 == 1:
        # k 4 3 2 1 
        for k in range(n+1-(i+1)//2):
            print("*", end = " ")
    # i = 2468
    else:
        for j in range(i//2):
            print("*", end =" ")
    print( )