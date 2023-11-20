cnt_even = 0
cnt_odd =0

for i in range(1,11):
    a = int(input())
    if a % 2 != 0:
        cnt_odd += 1
    else:
        cnt_even += 1



print(cnt_odd)