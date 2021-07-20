for row in range(6):
    for col in range(11):
        if (row==3 and (col>1 and col<9)) or (row+col==5 or col-row==5):
            print("*",end='')
        else:
            print(end=" ")
    print()