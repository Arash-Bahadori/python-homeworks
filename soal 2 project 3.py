year = eval(input("enter the year:"))
if year % 4 == 0 and year % 100 == 0 :
    print("normal year")
elif year % 4 == 0 :
    print("leap year")
else :
    print("normal year")