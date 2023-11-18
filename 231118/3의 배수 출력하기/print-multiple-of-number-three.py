n = int(input())

k = 0
d = 0

while d < n:
    k += 1
    d = 3 * k
    if d <= n:
        print(d, end = " ")