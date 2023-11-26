n = int(input())
cnt = 0
while True:
    
    if n % 2 == 0:
        if n == 1:
            break
        else:
            n /= 2
            cnt += 1
    else:
        if n == 1:
            break
        else:
            n = 3*n +1
            cnt += 1
print(cnt)