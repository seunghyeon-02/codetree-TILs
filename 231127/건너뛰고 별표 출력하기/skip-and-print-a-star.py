n = int(input())

for i in range(1, n+1):
    for p in range(i):
        print("*", end = "")
    print(" ")
    print(" ")
for i in range(1,n):
    for k in range(n-i):
        print("*", end = "")
    print(" ")
    print(" ")