while True:
    n = int(input())
    if n > 25:
        print("Lower")
        continue
    elif n < 25:
        print("Higher")
        continue
    else:
        print("Good")
        break