k = input()
l = k.split()

b = int(l[0])
a = int(l[1])

even = 0

if b % 2 == 0:
    even = b
    while even >= a:
        print(even, end = " ")
        even -= 2
else:
    even = b - 1
    while even >= a:
        print(even, end = " ")
        even -= 2