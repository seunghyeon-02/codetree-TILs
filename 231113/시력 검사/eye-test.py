r_sight = float(input())
l_sight = float(input())

if r_sight >=1.0 and l_sight >=1.0:
    print("High")
elif r_sight >=0.5 and l_sight >=0.5:
    print("Middle")
else:
    print("Low")