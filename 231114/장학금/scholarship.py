k = input()
l = k.split()


mid_score = int(l[0])
last_score = int(l[1])

if mid_score >= 90:
    if last_score >=95:
        print(100000)
    elif last_score >=90:
        print(50000)
    else:
        print(0)
else:
    print(0)