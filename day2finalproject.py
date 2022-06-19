print("WELLCOME TO TIP CALCULATOR")
total_bill = float(input("what was the total bill:$"))
percentage_tip = int(input("what percentage of tip you would like to give ?:10  12 or 15?"))
number_of_people = int(input("how many people split the bill ?"))
pay_amoount_with_tip = total_bill + percentage_tip/100* total_bill
pay_individually = round(pay_amoount_with_tip/number_of_people, 2)
print(f"Each person should pay :$ {pay_individually}")