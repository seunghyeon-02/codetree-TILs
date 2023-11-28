n = int(input())
#n줄 출력 i = 0 1 2 3
for i in range(n):
    #공백 출력
    for p in range(2*i):
        print(" ", end = "")
    for k in range(2*(n-i)-1):
        print("*", end = " ")
    print( )
#3줄 출력(n-1)
for j in range(n-1):
    #공백 출력 i = 0 1 2
    for l in range(2*(n-j-2)):
        print(" ", end = "")
    #*출력
    for m in range(2*(j+2)-1):
        print("*", end = " ")
    print( )