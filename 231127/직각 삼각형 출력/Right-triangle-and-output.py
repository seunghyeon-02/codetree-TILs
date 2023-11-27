n = int(input())
"""줄에 관련된 코딩"""
for i in range(n):
    """135의 규칙으로 늘어나는 코딩"""
    for k in range(2*i+1):
        print("*", end ="")
    print( )