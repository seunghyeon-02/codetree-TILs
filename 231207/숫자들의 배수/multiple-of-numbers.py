n = int(input())
cnt = 0
arr = []
for i in range(1,16):
    arr.append(n*i)
    if n *i % 5 == 0:
        cnt += 1
        if cnt == 2:
            break
for k in range(i):
    print(arr[k], end = " ")