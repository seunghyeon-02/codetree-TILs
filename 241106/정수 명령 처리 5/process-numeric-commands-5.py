n = int (input())
list_1 = []

for i in range(n):
    arr = input()
    arr = arr.split()
    
    fun_name = str(arr[0])
    if len(arr) == 2:
        num = int(arr[1])

    if arr[0]  == "push_back":
        list_1.append(num)
    
    elif arr[0] == "pop_back":
        list_1.pop()

    elif arr[0] == "size":
        print(len(list_1))
   
    else:
        print(list_1[num-1])