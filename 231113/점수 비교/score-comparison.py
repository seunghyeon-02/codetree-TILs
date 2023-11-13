k = input()
m = k.split()

math_Score_A = int(m[0])
eng_Score_A = int(m[1])

l = input()
n = l.split()
math_Score_B = int(n[0])
eng_Score_B = int(n[1])

if math_Score_A > math_Score_B and eng_Score_A > eng_Score_B:
    print(1)
else:
    print(0)