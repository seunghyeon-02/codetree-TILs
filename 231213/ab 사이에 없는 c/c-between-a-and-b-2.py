arr = list(map(int, input().split()))
a, b, c = arr[0], arr[1], arr[2]
cnt =0
for i in range(a,b+1):
    for k in range(1,100):
        if c*k == i:
            cnt+=1
if cnt >= 1:
    print("NO")
else:
    print("YES")