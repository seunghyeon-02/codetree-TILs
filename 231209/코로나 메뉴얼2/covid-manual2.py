count_arr =[0] *4

for i in range(3):
    temp = 0
    symp = 0

    arr = list(map(str, input().split( )))
    if arr[0] == "Y":
        symp += 1
    if int(arr[1]) >= 37:
        temp += 1

    if symp and temp == 1:
        count_arr[0] += 1
    elif symp == 0 and temp == 1:
        count_arr[1] += 1
    elif symp == 1 and temp == 0:
        count_arr[2] += 1
    else:
        count_arr[3] += 1

for i in range(4):
    print(count_arr[i], end =" ")

if count_arr[0] >= 2:
    print("E")