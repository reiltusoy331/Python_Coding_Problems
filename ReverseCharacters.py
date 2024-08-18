# Write a Python program that reverses the individual words in the string word 
# and changes their capitalization. 
# Uppercase letters should be printed in lowercase and vice versa.
# Assume that the string only contains letters and spaces are used to separate words.

word = "Hello World"
new_word =''

words_list = word.split(" ")

for letter in words_list:
    reversed_word = letter[::-1]
    swapped_case = reversed_word.swapcase()
    new_word += swapped_case + " "

new_word = new_word.rstrip()
print(new_word)