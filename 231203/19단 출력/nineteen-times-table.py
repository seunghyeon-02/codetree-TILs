for i in range(19):
    for k in range(19):
        if k % 2 == 1:
            print(f"{i+1} * {k+1} = {(i+1) * (k+1)}")
        else:
            if k == 18:
                print(f"{i+1} * {k+1} = {(i+1) * (k+1)}", end = " ")
            else:
                print(f"{i+1} * {k+1} = {(i+1) * (k+1)}", end = " ")
                print("/",end =" ")
    print( )