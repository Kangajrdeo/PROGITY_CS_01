# Caesar Cipher program for encryption and decryption

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep non-alphabet characters unchanged
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Keep non-alphabet characters unchanged
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption/Decryption")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    choice = input("Do you want to encrypt or decrypt the message? (e/d): ").lower()

    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
