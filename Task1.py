def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption & Decryption")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ('e', 'd'):
        print("Invalid choice. Please enter 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift. Please enter an integer.")
        return

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
