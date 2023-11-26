k = 0
l = 0
while True:
    n = int(input())
    if n // 10 == 2:
        k += n
        l += 1
    else:
        break
print(f"{k/l:.2f}")