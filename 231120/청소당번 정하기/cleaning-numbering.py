n = int(input())
cnt = 0
cnt_rest = 0
cnt_floor =0
cnt_class =0

while cnt <= n:
    if cnt == 0:
        cnt += 1
    if cnt % 12 == 0:
        cnt_rest += 1
        cnt += 1
    elif cnt % 3 ==0:
        cnt_floor += 1
        cnt += 1
    elif cnt % 2 ==0:
        cnt_class += 1
        cnt += 1
    else:
        cnt+= 1

print(cnt_class, cnt_floor, cnt_rest)