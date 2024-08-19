# Write a Python program to convert a string s to lowercase, sort the characters 
# of each letter in alphabetical order, and print the resulting string.
# You may assume that the string only contains letters and spaces to separate the words.
# Spaces should be preserved in the final string.

words = "Hello World"

word_list = words.split(" ")
new_word = ''
for word in word_list:
    lowercase_word = word.lower()
    sorted_word = "".join(sorted(lowercase_word))
    new_word += sorted_word + " "



new_word = new_word.rstrip()
print(new_word)



