import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for i in plain_text:        
        if i in alphabet:
            ascii_char = ord(i) + shift_amount
            
            if ord(i) in range(65,91):
                while ascii_char > 90:
                    ascii_char -= 26
            elif ord(i) in range(97,123):
                while ascii_char > 122:
                    ascii_char -= 26

            cipher_text += chr(ascii_char)
        else:
            cipher_text += i
        
    print(f"Here's the ecncoded result: \"{cipher_text}\"\n")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for i in cipher_text:
        if i in alphabet:
            ascii_char = ord(i) - shift_amount
            
            if ord(i) in range(65,91):
                while ascii_char < 65:
                    ascii_char += 26
            elif ord(i) in range(97,123):
                while ascii_char < 97:
                    ascii_char += 26

            plain_text += chr(ascii_char)
        else:
            plain_text += i
        
    print(f"Here's the decoded result: \"{plain_text}\"\n")

choice = "yes"

while(choice == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("You've entered wrong choice\n")
    
    choice = input("Type 'yes' if you wanna go again. Otherwise type 'no'.\n")