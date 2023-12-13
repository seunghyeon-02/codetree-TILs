k = list(map(int, input().split()))
len_A = k[0]
len_B = k[1]
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
#arr_B[0]가 없으면 연속부분수열이 안됨
if arr_B[0] not in arr_A:
    print("No")
else:
    locate_first = arr_A.index(arr_B[0])
    locate_count = arr_A.count(arr_B[0])
    #arr_A 에 있는 arr_B의 첫번째 원소의 갯수만큼 반복한다.
    for h in range(locate_count):
        #만약 리스트 슬라이스으로 len_A가 len_B보다 작아지면멈추고 No 출력.
        if (len(arr_A[locate_first:]) < len_B) or (arr_B[0] not in arr_A):
            print("No")
            break    
        # 이 help select는 얼마나 일치하는지 알려주는 역할을 함.
        help_select = 0
        for i in range(len_B):
            if arr_B[i] == arr_A[locate_first + i]:
                help_select += 1
        if help_select == len_B:
            print("Yes")
            break
        else:
            #일치하지 않았으므로 arr_A에 다음번째항부터 새로운 배열 대입
            if len(arr_A[locate_first+1:]) == 0:
                print("No")
                break
            elif locate_count == h + 1:
                print("No")
                break
            else:
                arr_A = arr_A[locate_first+1:]
                locate_first = arr_A.index(arr_B[0])