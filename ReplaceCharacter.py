# Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
# curr_char and new_char are variables that contain strings with a single character.
# If no match is found, print the initial string.

word = "Python"
curr_char= "P"
new_char="a"
new_word=''

for char in word:
    if char==curr_char:
        new_word+=new_char
    else:
        new_word+=char

print(new_word)



#-----------
# Option 2 / using a built-in method "replace"
#-----------

# word = "Python"
# curr_char = "p"
# new_char="a"
#
# print(word.replace(curr_char,new_char))
#
