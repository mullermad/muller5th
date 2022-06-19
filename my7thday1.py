
import  random

print("WELLCOME TO HANGMAN GAME PROJECTS\n")
word_list =["muller","elias","gizachew","kilosiga"]

choosen_word=random.choice(word_list)

print(choosen_word)
display=[]
for n in range(len(choosen_word)):
    display += "_"
    live=6
end = False
while not end:
    guess=input("guiss a letter\n").lower()

    for n in range(len(choosen_word)):
        letter=choosen_word[n]
        if guess == letter:
            display[n] = letter
    if guess not in choosen_word:
        live -=1
        if live==0:
            end=True
            print("GAMEOVER :YOU LOSE")


    if '_' not in display:
           end=True
           print("YOU WIN THE GAME MULLER")

    print(display)












