a =["L", "E", "B", "R", "O", "S"]

letter = str(input())

if letter not in a:
    print("None")
else:
    print(a.index(letter))