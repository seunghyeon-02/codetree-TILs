n = int(input())
cnt_leapyear = 0
cnt_year = 0
for i in range(1, n+1):
    if i % 100 == 0 and i % 400 != 0:
        cnt_year += 1
    elif i % 4 == 0:
        cnt_leapyear +=1
        cnt_year += 1
print(cnt_leapyear)