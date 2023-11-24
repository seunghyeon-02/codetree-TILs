k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
k =0

for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        k += i
        
print(k)