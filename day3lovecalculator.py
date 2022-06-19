name1=input("what is ur name ?\n")
name2=input("what is thir name ?\n")
bothname=name1 + name2
bothname.lower()
t=bothname.count("t")
r=bothname.count("r")
u=bothname.count("u")
e=bothname.count("e")
true = t + r + u + e

l=bothname.count("l")
o=bothname.count("o")
v=bothname.count("v")
e=bothname.count("e")
love = l + o + v + e
total = int(str(true) + str(love))


if total < 10 or total>90:
    print(f"the total love score is ,{total} u go together like chokekkkkkkkkk")
elif total >40 and total<50:
    print(f"the total love score is ,{total} you alright together")
else:
    print(f"the total love score is ,{total}")
