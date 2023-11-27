n = int(input())
"""줄에 관련된 코딩"""
for i in range(n):
    """*를 잘 출력되게 코딩"""
    for j in range(i+1):
        print("*", end = " ")
    print( )
for p in range(n):
    for k in range(n-p,1,-1):
        print("*", end = " ")
    print( )