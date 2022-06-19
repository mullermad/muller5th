import random
rock='''
_____|__rock________|
_____|__________|
_____|__________|
'''

sissor='''
_____|____sissor______|
_____|___+________|
_____|___()_______|
'''
paper='''
_____|___\\\\\__paper_____|
_____|_____\\\\_____|
_____|_______\\\\\___|
'''


user_choice = int(input("What do you choose? type 0 for rock, 1 for paper or 2 for sissor\n"))

computer_choice = random.randint(0,2)

if computer_choice ==0 and user_choice ==2:
    print(f"the computer choose{rock} \nand you choose {sissor}\n")
    print("computer won you lose")
elif computer_choice ==2 and user_choice ==1:
    print(f"the computer choose{sissor} \nand you choose {paper}\n")
    print("computer won you lose")
elif computer_choice == 1 and user_choice == 0:
    print(f"the computer choose{paper} \nand you choose {rock}\n")
    print("computer won you lose")

elif computer_choice ==2 and user_choice ==0:
    print(f"the computer choose{sissor} \nand you choose {rock}\n")
    print("wowwwwwwwwwww    you  won computer lose")
elif computer_choice ==1 and user_choice ==2:
    print(f"the computer choose{paper} \nand you choose {sissor}\n")
    print("wowwwwwwwwwww    you  won computer lose")
elif computer_choice ==0 and user_choice ==1:
    print(f"the computer choose{rock} \nand you choose {paper}\n")
    print("wowwwwwwwwwww    you  won computer lose")



elif computer_choice==user_choice:
    print("you draw with computer")
else:
    print("you enter invalid number")













