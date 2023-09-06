money = float(input("Enter the amount for RD : "))
rate = float(input("Enter the rate of interest per annum : "))
time = int(input("Enter duration in months : "))
year = time/12
if time>=6 and money>=500:          #amount>=500 is must
    interest = (money*(((1+(rate/100))**year))-money)  #Calc interest amount
elif time<6:                #time>6 is must
    print("Duration should be more than 6 months")
elif money<500:
    print("Minimum amount should be more than Rs.500")
else:
    print("Invalid Input")
print("interest amount is:", interest)