import random
names = input("please enter names with comma separated muller\n")
names_oflist = names.split(",")
print(names_oflist)
#
# length = len(names_oflist)
#
# pay_name = random.randint(0, length-1)
payname = random.choice(names_oflist)
print(f"the person who pay the bill is {payname}")