k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
s = 1
for i in range(1, b+1):
    if i % a == 0:
        s *= i
    
print(s)