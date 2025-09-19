import string

def caesar_cipher(text, shift, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = -shift if decrypt else shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

def vigenere_cipher(text, key, decrypt=False):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            if decrypt:
                shift = -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def main():
    print("🔐 Welcome to the Encryption Tool!")
    print("1. Encrypt with Caesar")
    print("2. Decrypt with Caesar")
    print("3. Encrypt with Vigenère")
    print("4. Decrypt with Vigenère")
    choice = input("Choose an option (1-4): ")

    text = input("Enter your message: ")

    if choice == "1":
        shift = int(input("Enter shift value: "))
        print("🔒 Encrypted:", caesar_cipher(text, shift))
    elif choice == "2":
        shift = int(input("Enter shift value: "))
        print("🔓 Decrypted:", caesar_cipher(text, shift, decrypt=True))
    elif choice == "3":
        key = input("Enter keyword: ")
        print("🔒 Encrypted:", vigenere_cipher(text, key))
    elif choice == "4":
        key = input("Enter keyword: ")
        print("🔓 Decrypted:", vigenere_cipher(text, key, decrypt=True))
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
