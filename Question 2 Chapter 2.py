# Input string
s = '5wghs7Qys65Nais23ajhy09P'

# Separate the number and letter substrings
numbers = ''.join([char for char in s if char.isdigit()])
letters = ''.join([char for char in s if char.isalpha()])

print(f"Number string: {numbers}")
print(f"Letter string: {letters}")

# Find the even numbers and convert them to ASCII decimal values
even_numbers = [int(char) for char in numbers if int(char) % 2 == 0]
ascii_even_numbers = [ord(str(num)) for num in even_numbers]
print(f"Even numbers: {even_numbers}")
print(f"ASCII values of even numbers: {ascii_even_numbers}")

# Find the upper-case letters and convert them to ASCII decimal values
uppercase_letters = [char for char in letters if char.isupper()]
ascii_uppercase_letters = [ord(char) for char in uppercase_letters]
print(f"Uppercase letters: {uppercase_letters}")
print(f"ASCII values of uppercase letters: {ascii_uppercase_letters}")

# Function to decrypt the ciphered text with a given shift key (s)
def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            # Shift each letter by the given key (s)
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around for uppercase letters
                decrypted_text.append(chr(shifted))
            elif char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around for lowercase letters
                decrypted_text.append(chr(shifted))
        else:
            decrypted_text.append(char)  # Keep non-alphabetic characters as is
    return ''.join(decrypted_text)

# Encrypted cryptogram
ciphertext = """VZ FRYSFU VFZNGVRAG NAQ N VYGGR VARFHPER V ZNXR ZVFGNXRRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PHAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAQ QRFRER ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

# Try different shift keys (s) and print the results
for s in range(1, 26):  # Shift keys from 1 to 25
    decrypted_message = decrypt_caesar_cipher(ciphertext, s)
    print(f"Shift Key {s}:\n{decrypted_message}\n")

# Function to decrypt the ciphered text with a shift key of 13
def decrypt_caesar_cipher(ciphertext):
    shift = 13  # This needs to be inside the function and properly indented
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            # Shift each letter by 13
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26  # Wrap around for uppercase letters
                decrypted_text.append(chr(shifted))
            elif char.islower():
                if shifted < ord('a'):
                    shifted += 26  # Wrap around for lowercase letters
                decrypted_text.append(chr(shifted))
        else:
            decrypted_text.append(char)  # Keep non-alphabetic characters as is
    return ''.join(decrypted_text)

# Encrypted cryptogram
ciphertext = """VZ FRYSFU VFZNGVRAG NAQ N VYGGR VARFHPER V ZNXR ZVFGNXRRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PHAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAQ QRFRER ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

# Decrypt the message using the fixed shift key (13)
decrypted_message = decrypt_caesar_cipher(ciphertext)

# Print the decrypted message
print("Decrypted Message:\n")
print(decrypted_message)

#shift key=25
print ("Question 2 done")