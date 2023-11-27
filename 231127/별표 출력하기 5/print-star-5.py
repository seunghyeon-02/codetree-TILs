n = int(input())

for i in range(n,0,-1):
    """2줄 설정 완료 i = 1 2"""
    for p in range(i):
        """블럭 분할 완료 i = 1 p = 0 1 2, i = 2  p = 0 1"""
        for k in range(i):
            """블럭안에서 p개만큼 출력"""
            print("*", end ="")
        print(" ", end = "")
        
    print()