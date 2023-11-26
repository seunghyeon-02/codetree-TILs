while True:
    k = input()
    l = k.split()

    a = int(l[0])
    b = int(l[1])
    c = l[2]

    print(a*b)

    if c == "C":
        break