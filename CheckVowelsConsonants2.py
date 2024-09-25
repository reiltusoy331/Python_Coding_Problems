# Write a Python program that prints a descriptive message indicating if each character in a string is a vowel
# or a consonant. For example: "<char> is a <consonant | vowel>"
# If the character is a special character, number, or symbol, print "<char> is not a letter".
# If the string is empty, print "Empty String".

##########
# Option 2
##########

my_string = "Score: 36"
vowels =['a','e','i','o','u']

if not my_string:
    print('Empty String.')

else:
    for char in my_string.lower():
        if char in vowels:
            print(f"{char} is a vowel.")
        elif char.isalpha():
            print(f"{char} is a consonant.")
        else:
            print(f"{char} is not a letter.")