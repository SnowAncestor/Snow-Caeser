import os
import logo
import Caesar_Enc
import Caeser_Dec

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def caesar(st):
    if st == "encode":
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        after_enc = Caesar_Enc.Enc(text, shift)
        print(f"Here is the Encoded Result: {after_enc}\n")
    elif st == "decode":
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        after_dec = Caeser_Dec.Dec(text, shift)
        print(f"Here is the Decoded Result: {after_dec}\n")
    else:
        return "wrong input!"

status = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
Possibility = caesar(status)

if Possibility == "wrong input!":
    print("You have two choices! But unfortunately you have lost them.")
else:
    while True:
        input("Press Enter to continue...")  

        clear_console()
        print(logo.logo)

        At_Final = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
        if At_Final == "no":
            break
        elif At_Final == "yes":
            status = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
            Possibility = caesar(status)
            if Possibility == "wrong input!":
                print("You have two choices! But unfortunately you have lost them.")
                break
        else:
            print("You have two choices! But unfortunately you have lost them!")
            break
