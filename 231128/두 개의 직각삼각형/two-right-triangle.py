n = int(input())
#줄 설정 if n =4 i = 1234
for i in range(1, n+1):
    #*출력 p = 8 4 2 0
    for p in range(n-i+1):
        print("*",end = "")
    for k in range(2*(i-1)):
        print(" ",end = "")
    for j in range(n-i+1):
        print("*", end ="")
    print( )
    
#공백 출력 == 첫번짼 0개 둘째줄엔 2개 셋재줄엔 4개 그러면 2(n-1)근데 가운데에 6개