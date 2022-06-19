print("WELLCOME TO DAY 5 ")
stu_height = input("enter the list of student height\n").split()

for n in range(0,len(stu_height)):
    stu_height[n]=int(stu_height[n])


sum=0

for i in stu_height:
    sum +=i
print(sum)

number=0
for m in stu_height:
    number+=1
print(number)

ave=sum/number
print(f"the average ii {ave}")




