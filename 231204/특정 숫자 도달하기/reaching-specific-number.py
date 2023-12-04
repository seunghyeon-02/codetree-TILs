n = input()
k = n.split()
p = 0
sum_1 = 0
avr_1 = 0
for i in range(10):
    if int(k[i]) >= 250:
        n = k[0:i]
        break
    else:
        p+=1

for j in range(p):
    sum_1 += int(n[j])

print(sum_1, end = " ")

avr_1 = sum_1 /p

print(avr_1)