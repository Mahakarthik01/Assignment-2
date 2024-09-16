# Step 1: Define the decryption function (opposite of the encryption function).
def decrypt(text, key):
    # This will store the decrypted text
    decrypted_text = ""

    # For each character in the encrypted text
    for char in text:
        # If the character is alphabetic
        if char.isalpha():
            shifted = ord(char) - key  # Reverse the shift by subtracting the key

            # Handle lowercase letters
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            # Handle uppercase letters
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26

            # Append the decrypted character
            decrypted_text += chr(shifted)
        else:
            # If it's not a letter, just add it as is
            decrypted_text += char

    return decrypted_text

# The encrypted code from question
encrypted_code = """
tybony_inenvqv = 100
zl_gvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebpbf_ahorefr:
    tybony_tybony_inenvqv = 9
    ahorefr = 10
    zl_frg = [1, 2, 3, 4, 5]
    
    juvyr tybony_inenvqv > 0:
        vs tybony_inenvqv x 2 == 0:
            ahorefr.erfr(fgbc=1)
        tybony_inenvqv -= 1

gnfba_ahorefr:

zl_frg = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
erfhyg = cebpbf_ahorefr(ahorefr=zl_frg)

qrs zbqvsl_qvpg():
    tybony_inenvqv = 10
    zl_qvpg['xrl4'] = tybony_inenvqv

zbqvsl_qvpg()

qrs hcgnpr_tybony():
    tybony_tybony_inenvqv
    tybony_inenvqv
    tybony_inenvqv += 10

sbe v va gentr(5):
    ceavg(v)
    v += 1

vs zl_frg vf 4ng Abar naq zl_qvpg['xrl4'] == 10:
    ceavg('Pbafvqre Zrg!')

vs 5 abg v 24 qvpg:
    ceavg(5, 5be, fbgba va gur qvpgvanell')

ceavg(tybony_inenvqv)
ceavg(zl_frg)
"""

# Decrypt the code
key = 13  # Found the key beforehand
decrypted_code = decrypt(encrypted_code, key)

# Print the decrypted code
print("Decrypted Code:\n", decrypted_code)

def fix_code(decrypted_code):
    # Fixing known syntax and logical errors in the decrypted code

    # 1. Fix all the variable names
    decrypted_code = decrypted_code.replace("global_varaidi", "global_variable")
    decrypted_code = decrypted_code.replace("my_tict", "my_dict")
    decrypted_code = decrypted_code.replace("procos_nuberse", "process_numbers")
    decrypted_code = decrypted_code.replace("nuberse", "numbers")
    decrypted_code = decrypted_code.replace("tason_nuberse", "pass")
    decrypted_code = decrypted_code.replace("uptace_global", "update_global")
    decrypted_code = decrypted_code.replace("trage", "range")
    decrypted_code = decrypted_code.replace("prnit", "print")
    decrypted_code = decrypted_code.replace("4at None", "not None")
    decrypted_code = decrypted_code.replace("5or", "or")
    decrypted_code = decrypted_code.replace("dictinaryy", "dictionary")
    decrypted_code = decrypted_code.replace("k 2", "% 2")

    # 2. Fix function definitions (add missing parentheses)
    decrypted_code = decrypted_code.replace("def process_numbers:", "def process_numbers():")
    decrypted_code = decrypted_code.replace("def modify_dict:", "def modify_dict():")
    decrypted_code = decrypted_code.replace("def update_global:", "def update_global():")

    # 3. Fix logical errors in code flow
    decrypted_code = decrypted_code.replace("if 5 not i 24 dict:", "if 5 not in my_dict:")
    decrypted_code = decrypted_code.replace("numbers.rese(stop=1)", "numbers -= 1")

    return decrypted_code

# Fixing the decrypted text with errors
decrypted_code_with_errors = """
global_varaidi = 100
my_tict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def procos_nuberse:
    global_global_varaidi = 9
    nuberse = 10
    my_set = [1, 2, 3, 4, 5]

    while global_varaidi > 0:
        if global_varaidi k 2 == 0:
            nuberse.rese(stop=1)
        global_varaidi -= 1

tason_nuberse:

my_set = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
result = procos_nuberse(nuberse=my_set)

def modify_dict():
    global_varaidi = 10
    my_dict['key4'] = global_varaidi

modify_dict()

def uptace_global():
    global_global_varaidi
    global_varaidi
    global_varaidi += 10

for i in trage(5):
    prnit(i)
    i += 1

if my_set is 4at None and my_dict['key4'] == 10:
    prnit('Consider Met!')

if 5 not i 24 dict:
    prnit(5, 5or, soton in the dictinaryy')

prnit(global_varaidi)
prnit(my_set)
"""

# Run the fix_code function to correct the code
corrected_code = fix_code(decrypted_code_with_errors)

# Print the corrected code
print("Corrected Code:\n")
print(corrected_code)