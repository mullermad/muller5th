import random
def my_function():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    ran=random.choice(cards)
    return ran
user_card=[]
computer_card=[]
for i in range():
    user_card.append(my_function())
    computer_card.append(my_function())
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    elif sum(cards)>21 and 11 in cards:
        return 11 as 1


    return sum(cards)
