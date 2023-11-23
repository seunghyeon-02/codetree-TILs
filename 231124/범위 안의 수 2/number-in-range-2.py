i, k, b = 1, 0, 0

while i <= 10:
    a = int(input())
    if a >= 0 and a <= 200:
        b += a
        k += 1
    i += 1

print(f"{b} {b/k:.1f}")