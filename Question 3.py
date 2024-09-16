def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char) - key  # Reverse the shift
            if char.islower():
                if shifted < ord('a'):  # Ensure it doesn't go before 'a'
                    shifted += 26
                elif shifted > ord('z'):  # Loop it back to 'a'
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):  # Ensure it doesn't go before 'A'
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char  # Non-alphabetical characters remain unchanged
    return decrypted_text
encrypted_code = "tybony_tybnoy_inenvoyr = 100"  # This is a sample from your encrypted text
for key in range(1, 26):
    print(f"Key: {key}")
    print(decrypt(encrypted_code, key))

encrypted_code = """
tybony_tybnoy_inenvoyr = 100
z1_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}
qrs_cebpbf_ahzoref():
tybony_tybnoy_inenvoyr
tybony_inenvoyr = 5
ahzoref = [1, 2, 3, 4, 5]
juvyr ypbnoy_inenvoyr > 0:
vs ypbnoy_inenvoyr % 2 == 0:
ahzoref.erzbir(ypbnoy_inenvoyr)
ypbnoy_inenvoyr -= 1
erghea ahzoref
z1_frg = ([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
erfhvg = cebprff_ahzoref(ahzoref=z1_frg)
qrs_zbqvsl_qvpg():
ypbnoy_inenvoyr = 10
z1_qvpg['xrl4'] = ypbnoy_inenvoyr
zbqvsl_qvpg(5)
qrs_hcagrp_tybnoyr():
tybony_tybnoy_inenvoyr
tybony_inenvoyr += 10
sbe_v va_enatr(s):
cevag(v)
vs z1_frg vf abg abar naq z1_qvpg['xrl4'] != 10:
cevag("Pbagnvaba rgr")
vs s abg va z1_qvpg:
cevag("sbbg sbhaq va gur qvpgvbaner!")
cevag(z1_qvpg)
cevag(z1_frg)
"""
decrypted_code = decrypt(encrypted_code, 13)
print(decrypted_code)

# Modified function to accept 'values' as a parameter
def process_values(values):  # Now it takes 'values' as an argument
    tybony_inventory = 5
    # Loop with logic to remove items from list if condition is met
    while tybony_inventory > 0:
        if tybony_inventory % 2 == 0:
            values.remove(tybony_inventory)
        tybony_inventory -= 1
    return values

# Using the function
z1_set = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
result = process_values(z1_set)  # Correctly passing 'z1_set'
print(result)  # Printing the result to verify

# Step 1: Global variable
global_variable = 100

# Step 2: Dictionary with keys and values
m1_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Step 3: Function to process numbers
def process_numbers(numbers):
    global global_variable
    local_variable = 5
    while local_variable > 0:
        if local_variable % 2 == 0 and local_variable in numbers:
            numbers.remove(local_variable)
        local_variable -= 1
    return numbers

# Step 4: Set of numbers
m1_set = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
result = process_numbers(m1_set)  # Call the function to process the numbers

# Step 5: Modify dictionary function
def modify_dict():
    global global_variable
    local_variable = 10
    m1_dict['key4'] = local_variable  # Add a new key to the dictionary

modify_dict()  # Call the function to modify the dictionary

# Step 6: Update global variable and print values
def update_global():
    global global_variable
    global_variable += 10
    for i in range(5):
        print(i)
    
    # Conditional printing
    if m1_set is not None and m1_dict['key4'] != 10:
        print("Condition met")
    
    if 'f' not in m1_dict:
        print("Key not found in the dictionary!")

    print(m1_dict)
    print(m1_set)

update_global()  # Call the function to update and print values

print("Question 3 done")


