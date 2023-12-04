n = input()
k = n.split()
p = 0
sum_1 = 0
avr_1 = 0
for i in range(10):
    if int(k[i]) >= 250:
        k = k[0:i]
        break
    else:
        p+=1
for j in range(p):
    sum_1 += int(k[j])

avr_1 = sum_1 /p

print(f"{sum_1} {avr_1:.1f}")