arr = list(map(int, input().split( )))
k = 10
sum1 = 0
avr1 = 0
for i in range(10):
    if arr[i] == 0:
        arr = arr[:i]
        k = i 
        break

sum1 = sum(arr)
avr1 = sum1 / k

print(f"{sum1} {avr1:.1f}")