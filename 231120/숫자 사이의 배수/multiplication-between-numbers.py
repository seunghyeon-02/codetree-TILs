k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
sum_5_7 = 0
cnt = 0
for i in range (a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_5_7 += i
        cnt += 1

avr = float(sum_5_7 / cnt)

print(f"{sum_5_7} {avr:.1f}")