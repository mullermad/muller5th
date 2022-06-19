import math
test_h=int(input("enter height\n"))
test_w=int(input("enter height\n"))
coverage=5

def paintcalculate(height,weight,cover):
    area=height*weight
    can=math.ceil(area/cover)

    print(f"the can is {can}")

paintcalculate(test_h,test_w,coverage)