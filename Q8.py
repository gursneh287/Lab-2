n=int(input())
for i in range(n):
    year=int(input())
    if year%4==0 and (year%100!=0 or year%400==0):
        print(year," It is a leap year")
    else:
        print(year,"Not a leap year")