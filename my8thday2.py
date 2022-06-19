print("prime number checker")

number = int(input("enter the number"))
is_prime = True
for i in range(2,number):
    if number %  i==0:
        is_prime=False



if is_prime==True:
    print("it is prime")
else:
    print("it is not prime")

