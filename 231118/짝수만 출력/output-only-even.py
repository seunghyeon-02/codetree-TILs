k = input()
l = k.split()

a = int(l[0])
b = int(l[1])
 
i = 0
even = 0

if a % 2 == 0:
    even = a
    while even <= b:
        print (even, end = " ")
        even += 2

else:
    even = a + 1
    while even <= b:
        print(even, end = " ")
        even += 2