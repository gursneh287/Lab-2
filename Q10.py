n = int(input("enter time in second:"))
if n <= 86400700:
    x = n/3600
    a = int(x) #hours
    y = n - (a*3600)
    b = int(y/60) #mins
    c = y - (b*60) #secs
print(a,"hours", b, "mins",c, "seconds")
    


