n = input()
k = n.split()

a = int(k[0])
b = int(k[1])
cnt_1 = 0

for i in range(a, b+1):
    cnt = 0
    for j in range(1,i+1):
        if i % j ==0:
            cnt += 1
    if cnt == 3:
        cnt_1 += 1

print(cnt_1)