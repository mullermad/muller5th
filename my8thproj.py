alphabet=["a","b","c","d","e","e","f","g","h","i",
          "j","k","l","m","n","o","p","q","r","s","t","u",
          "v","w","x","y","z","a","b","c","d","e","e","f","g","h",
          "i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

result=True

while result:
    direction=input("type ' encode' to encript or type 'decode' to decript message\n")

    if direction == "encode" or direction=="decode":

        message=input("type the message\n").lower()

        shift=int(input("type the shift number\n"))
        shift=shift%26
        def ceasar(user_message,shift_amount,my_direction):
             end_text = " "
             if my_direction == "decode":
                 shift_amount *= -1

             for char in user_message:
                  if char in alphabet:

                     position=alphabet.index(char)
                     new_position=position+shift_amount
                     end_text+=alphabet[new_position]
                  else:

                     end_text+=char
             print(f"the meaasge you {my_direction}  is {end_text}")





        ceasar(user_message=message,shift_amount=shift,my_direction=direction)
    else:
        print("wrong input")
    again = input("do you want to do again? type 'yes' to paly or 'no' to exit\n")
    if again=='no':
        result=False
        print("GOODBYE")

