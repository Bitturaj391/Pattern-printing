def pattern(n):
    temp = n
    x = 1
    while (n>0):
        print(" "*(n-1) + "*"*x)
        n = n-1
        x = x+2
n = int(input("Enter the number of rows "))
pattern(n)