k = input()
m = k.split()

l = input()
n = l.split()

A_math = int(m[0])
A_engl = int(m[1])

B_math = int(n[0])
B_engl = int(n[1])

if A_math > B_math:
    print("A")
elif A_math < B_math:
    print("B")
else:
    if A_engl > B_engl:
        print("A")
    elif A_engl < B_engl:
        print("B")