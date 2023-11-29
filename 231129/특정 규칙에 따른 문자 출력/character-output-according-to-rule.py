n = int(input())
# n줄 출력  n = 3 i = 0 1 2
for i in range(n):
    # 공백 출력 k = 2 1 0 
    for k in range(n- i-1):
        print(" ", end =" ")
    #@출력
    for j in range(i+1):
        print("@", end = " ")
    print()
    #h =0 1
for h in range(n-1):
    for p in range(n-h-1):
        print("@", end =" ")
    print( )