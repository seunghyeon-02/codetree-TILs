a = input()
b = input()
c = input()

a1 = a.split()
b1 = a.split()
c1 = c.split()

a_symp = a1[0]
a_temp = int(a1[1])

b_symp = b1[0]
b_temp = int(b1[1])

c_symp = c1[0]
c_temp = int(c1[1])

patient = 0

if a_symp == "Y" and a_temp >= 37:
    patient += 1
if b_symp == "Y" and b_temp >= 37:
    patient += 1
if c_symp == "Y" and c_temp >= 37:
    patient +=1

if patient >= 2:
    print("E")
else:
    print("N")