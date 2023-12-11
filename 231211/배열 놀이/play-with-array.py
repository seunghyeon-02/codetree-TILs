k = list(map(int, input().split()))
n = k[0]
q = k[1]

arr_n = list(map(int, input().split()))

for i in range(q):
    
    arr_q = list(map(int, input().split()))
    a = arr_q[1]
    if len(arr_q) == 3:
        b = arr_q[2]
    
    if arr_q[0] == 1:
        print(arr_n[a-1])

    elif arr_q[0] == 2:
        if a not in arr_n:
            print(0)
        else:
            print(arr_n.index(a)+1)

    else:
        for i in range(a,b+1):
            print(arr_n[i-1], end =" ")
        print( )