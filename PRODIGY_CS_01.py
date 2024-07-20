def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) + shift_amount
            if char.islower():
                if new_char > ord('z'):
                    new_char -= 26
                encrypted_text += chr(new_char)
            elif char.isupper():
                if new_char > ord('Z'):
                    new_char -= 26
                encrypted_text += chr(new_char)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = ord(char) - shift_amount
            if char.islower():
                if new_char < ord('a'):
                    new_char += 26
                decrypted_text += chr(new_char)
            elif char.isupper():
                if new_char < ord('A'):
                    new_char += 26
                decrypted_text += chr(new_char)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption and Decryption")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'E':
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")
    elif choice == 'D':
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
