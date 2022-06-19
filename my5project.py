
import random
print("WELLCOME TO PYPASSWORD GENERATOR")
num=['1','2','3','4','5','6','7','8','9','0']
smbl=['@',')','*','/','-','+','#','%','&','!']
ltr=['a','b''g','n','v','t','h' , 'r','d','u']

numbers= int(input("how many numbers you want to use for your password\n"))
symbols = int(input("how many symbols you want to use for your password\n"))
letters = int(input("how many letters you want to use for your password\n"))

# password= ""
#
#
# for i in range(1,numbers +1):
#     password +=random.choice(num)
#
#
# for j in range(1,symbols +1):
#     password +=random.choice(smbl)
#
#
#
# for k in range(1,letters +1):
#     password +=random.choice(ltr)
# print(password)

password_list=[]
for i in range(1,numbers +1):
    password_list +=random.choice(num)
for j in range(1,symbols +1):
    password_list +=random.choice(smbl)

for i in range(1,letters +1):
    password_list +=random.choice(ltr)


random.shuffle(password_list)



password=""
for t in password_list:
    password +=t
print(f"your password is: {password}")
