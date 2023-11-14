k = input()
l = k.split()

o = input()
p = o.split()

A_age = int(l[0])
A_gender = l[1]

B_age = int(p[0])
B_gender = p[1]

if (A_age >= 19 and A_gender == "M") or (B_age >= 19 and B_gender == "M"):
    print(1)
else:
    print(0)