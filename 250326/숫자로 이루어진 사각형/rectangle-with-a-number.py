n = int(input())

def print_num(n):
    start_num = 1
    for i in range(n):
        for j in range(n):
            if start_num == 10:
                start_num = 1
            print(start_num, end =" ")
            start_num += 1
        print( )

print_num(n)
# Please write your code here.