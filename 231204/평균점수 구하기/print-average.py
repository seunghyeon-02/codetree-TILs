n = input()
list = n.split( )
sum1 = 0
avr1 = 0

for i in range(8):
    k = float(list[i])
    sum1 += k 

avr1 = sum1 / 8
print(f"{avr1:.1f}")