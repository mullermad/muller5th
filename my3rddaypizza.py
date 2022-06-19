print("WELLCOME TO PIZZA ORDERING SOFTWARE PROGRAM")

size =input("what size of pizza u wanna to order? large,mid,small ?\n")
peporeni = input("do u want peporeni? l,m,s ?\n")
cheese = input("do u want extera cheese? y or n \n")
if size == "large":
   size_bill=int(25)
elif size == "mid":
    size_bill =int(20)

elif size == "small":
    size_bill =int(15)

if peporeni=="l":
    peporeni_bill = int(3)
else:
    peporeni_bill=int(2)

if cheese == "y":
    cheese_bill=int(1)

total_bill = size_bill + peporeni_bill + cheese_bill
print(f"the total bill for the pizza u take is about: ${ total_bill}")

