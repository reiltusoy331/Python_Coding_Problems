# Write a Python program that prints the word without the character at index number.
# If the index number is out of range, print the string word intact.
# If the string word is empty, print the string word intact.

word = "Hello"
number = 21


if (len(word)==0) or (number > len(word)):
    print(word)
else:
    word_new=''
    for i in range(0,len(word)):
            if i !=  number:        
                word_new+=word[i]    
    print(word_new)
    
        


