n = int(input())

arr = list(map(float, input().split( )))
sum1 = sum(arr)
avr = sum1 / n 
print(f"{avr:.1f}")
if avr >= 4.0:
    print("Perfect")
elif avr >= 3.0:
    print("Good")
else:
    print("Poor")