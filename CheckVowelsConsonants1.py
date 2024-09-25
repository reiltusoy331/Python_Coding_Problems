# Write a Python program that prints a descriptive message indicating if each character in a string is a vowel
# or a consonant. For example: "<char> is a <consonant | vowel>"
# If the character is a special character, number, or symbol, print "<char> is not a letter".
# If the string is empty, print "Empty String".

##########
# Option 1
##########

my_string = "Python~@"
vowels =['a','e','i','o','u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

for character in my_string:
    char = character.lower()
    if char in vowels:
        print(f"{char} is a vowel")
    elif char in consonants:
        print(f"{char} is a consonant")
    elif char not in consonants:
        print(f"{char} is not a letter")
    else:
        print("Empty String")
        