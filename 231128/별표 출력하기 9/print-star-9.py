n = int(input())
#3줄 설정완료 i =012
for i in range(1,n+1):
    #공백 프린트 4개 2개 0개 
    for k in range(2*(n-i)):
        print(" ", end ="")
    # *프린트 1개 3개 5개 2n-1
    for p in range(2*i -1):
        print("*", end =" ")
    print()