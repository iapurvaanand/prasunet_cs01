##encryption
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) + shift_amount
            if char.islower():
                if new_char > ord('z'):
                    new_char -= 26
            elif char.isupper():
                if new_char > ord('Z'):
                    new_char -= 26
            encrypted_text += chr(new_char)
        else:
            encrypted_text += char
    return encrypted_text
##decryption
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) - shift_amount
            if char.islower():
                if new_char < ord('a'):
                    new_char += 26
            elif char.isupper():
                if new_char < ord('A'):
                    new_char += 26
            decrypted_text += chr(new_char)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption and Decryption")
    while True:
        choose = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choose == 'q':
            break
        if choose not in ['e', 'd']:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")
            continue

        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))

        if choose == 'e':
            encrypted_message = encrypt(text, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choose == 'd':
            decrypted_message = decrypt(text, shift)
            print(f"Decrypted message: {decrypted_message}")

if _name_ == "_main_":
    main()