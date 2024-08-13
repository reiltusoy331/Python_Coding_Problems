# Write a Python program that prints a copy of the string word without any spaces.
# Words should be connected in the final string.
# If the string doesn't contain spaces, print it intact.

#---------
# Option 1
#---------
word = "World"
SPACE = " "
word_new=''
for letter in word:
    
    if letter==SPACE:
        continue
    word_new+=letter

print(word_new)


