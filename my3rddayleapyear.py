year = int(input("enter the year\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap")
    else:
        print("leap year")

else:
    print("not leap year")

