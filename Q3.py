x = int(input("enter a number x:"))
y = int(input("enter a number y:"))
if x>=0 and y>=0:
    if y % x == 0:
        print("y is divisible by x")
    else:
        print("y is not divisible by x")
else:
    print("invalid output")
    
