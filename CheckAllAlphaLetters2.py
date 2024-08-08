# Write a Python program that checks if the variable "words" ontains all the letters in the alphabet 
# (case-insensitive, so "A" should be equivalent to "a").
# Before comparing the characters, you should convert the string to lowercase.
# If the string contains spaces, ignore them before finding the result.
# You may assume that the string doesn't contain any other symbols, only spaces (possibly).

import string

words = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in words.lower():
        is_pangram = False

print(is_pangram)