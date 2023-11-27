n = int(input())

for p in range(n-1,0,-1):
    for k in range(p):
        print("*", end = " ")
    print("*")
print("*")