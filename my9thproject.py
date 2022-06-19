
print("wellcome to the game")
bid_dictionary={}
contnue=True
while contnue:
    name=input("what is your name ?\n")
    price=int(input("what is your bid ? :$\n"))
    bid_dictionary[name]=price
    other=input("is there other type 'yes' to continue otherwise type 'no' to exit\n")
    if other=="no":
        contnue=False
        max=0
        winner=""

        for i in bid_dictionary:
            if bid_dictionary[i]>max:
                max=bid_dictionary[i]
                winner=i
        print(f"the wiinner is is{winner}")



