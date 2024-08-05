# Write a Python program that prints a version of the string variable "word" 
# with all commas replaced by dots.

#-----------
# Option 1
#-----------
word = "3,456,344"
char= ","
replace ="."
new_word=''

for letter in word:
    if letter == char:
        new_word+=replace
    else:
        new_word+=letter

print(new_word)
