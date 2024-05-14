arr = list(map(int, input().split()))
arr_2= list(map(int, input().split()))

sum_arr = sum(arr)
sum_arr_2 = sum(arr_2)

print(sum_arr/4, sum_arr_2/4)
for i in range(4):
    k = arr[i] + arr_2[i]
    print(k/2 , end = " ")
print( )
h = sum_arr+ sum_arr_2
print(h/8)