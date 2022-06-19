height = float(input("enter height"))
weight = int(input("enter weight"))
bmi = round(float(weight/height**2),2)
if bmi < 18.5:
    print(f" your body mass index is {bmi},under weight")
elif bmi < 25:
    print(f" your body mass index is {bmi},normal weight")
elif bmi <30:
    print(f" your body mass index is {bmi},over weight")
elif bmi < 35:
    print(f" your body mass index is {bmi},obse")
else:
    print(f" your body mass index is {bmi},clinically obse")