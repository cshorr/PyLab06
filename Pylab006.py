
def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print(' |   ',end='')
    for i in range(alpha_len):
        print(f"| {alphabet[i % alpha_len]} ", end=' ')
    print('|')
    print(f"{'|--- '*(alpha_len + 1)}|")

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                c = alphabet[(i +shift) % alpha_len]
                print(f"| {c} ", end=' ')
                print(f"| {c} ", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]} ", end=' ')
        print("|")

def letter_to_index(letter, alphabet:str):
    return alphabet.lower().index(letter.lower())


def index_to_letter(index, alphabet:str):
    if 0 <= index < len(alphabet):
        return alphabet[index]
    return ''


def vigenere_index(key_letter, plaintext_letter, alphabet):
    return(letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % len(alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text += ' '
        elif c.upper() in alphabet:
            cipher_text += index_to_letter(vigenere_index(key[counter % len(key)], c, alphabet), alphabet)
            counter += 1
    return cipher_text

message = 'ONE GIANT LEAP FOR MANKIND'
key = "SURFBOARD"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = 'ONE GIANT LEAP FOR MANKIND'
         #"SUR FBOAR DSUR FBO ARDSURF
# print (f'{c},{key[i % len(key)]}')
#vigenere_sq(alphabet)
#print(letter_to_index('h', alphabet))
#print(index_to_letter(7, alphabet))
#print (index_to_letter(
       #vigenere_index('O', 'S', alphabet),alphabet))
print(encrypt_vigenere(key, message, alphabet) )
# Demonstration of the original encryption
def demo_PartOne():
    key = "SURFBOARD"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = 'ONE GIANT LEAP FOR MANKIND'
    cipher_text = encrypt_vigenere(key, message, alphabet)
    print("Original message:", message)
    print(f"Encrypted message: {cipher_text}")
#================================================================
    #Part 3 and 4 with help from ChatGPT, I probably don't deserve extra credit but its kinda fun anyway!
#================================================================
def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = alphabet.index(key_letter.upper())
    cipher_index = alphabet.index(cipher_letter.upper())
    plain_index = (cipher_index - key_index) % len(alphabet)
    if cipher_letter.isupper():
        return alphabet[plain_index]
    else:
        return alphabet[plain_index].lower()

def decrypt_vigenere(key, cipher_text, alphabet):
    plain_text = ''
    counter = 0
    for c in cipher_text:
        if c == ' ':
            plain_text += ' '
        elif c.upper() in alphabet:
            plain_text += undo_vigenere_index(key[counter % len(key)], c, alphabet)
            counter += 1
    return plain_text

def encrypt_vigenere(key, plain_text, alphabet):
    cipher_text = ''
    counter = 0
    for c in plain_text:
        if c == ' ':
            cipher_text += ' '
        elif c.upper() in alphabet:
            cipher_text += vigenere_index(key[counter % len(key)], c, alphabet)
            counter += 1
    return cipher_text

def vigenere_index(key_letter, plain_letter, alphabet):
    key_index = alphabet.index(key_letter.upper())
    plain_index = alphabet.index(plain_letter.upper())
    cipher_index = (plain_index + key_index) % len(alphabet)
    if plain_letter.isupper():
        return alphabet[cipher_index]
    else:
        return alphabet[cipher_index].lower()

def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:
        print("Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            plain_text = input("Enter the plain text: ")
            key = input("Enter the key: ")
            cipher_text = encrypt_vigenere(key, plain_text, alphabet)
            print("Encrypted text:", cipher_text)
        elif choice == "2":
            cipher_text = input("Enter the cipher text: ")
            key = input("Enter the key: ")
            plain_text = decrypt_vigenere(key, cipher_text, alphabet)
            print("Decrypted text:", plain_text)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
