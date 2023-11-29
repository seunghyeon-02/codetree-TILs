n = int(input())
# n = 4 i = 12345678
for i in range(1,2*n+1):
    # i = 1 3 5 7
    if i % 2 == 1:
        for k in range((i+1)//2):
            print("*", end = " ")
        print( )
    # i = 2 4 6 8
    else:
        for j in range(n+1-(i//2)):
            print("*", end =" ")
        print( )