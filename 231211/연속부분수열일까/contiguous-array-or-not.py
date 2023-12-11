k = list(map(int, input().split()))
n1 = k[0]
n2 = k[1]
help_select = 0
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

if arr_B[0] not in arr_A:
    print("No")
else:
    k = arr_A.index(arr_B[0])
    for i in range(n2):
        if arr_B[i] == arr_A[i+k]:
            help_select += 1
    
    if help_select == n2:
        print("Yes")
    else:
        print("No")