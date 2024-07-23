#leap year
n=int(input())
if(n%4==0 and n%100!=0 or n%400==0):
    print("leap year")
else:
    print("not a leap year")


#
year=int(input())
if(2000<=year and year<=2025):
    print("the given year is out of range")
else:    
    if(year % 4 == 0 and year % 100 != 0) or (year%400 == 0):
        print("it is a leap year")
    else:
        print("it is not a leap year")