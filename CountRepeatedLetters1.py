# Write a Python program to count the number of repeated letters in the string "word".
# The program must print the total number of repeated letters and a message on the 
# next line displaying the repeated characters separated by a space and sorted alphabetically.
# If there are no repeated characters in the string, print 0 as the total count and None on the next line.

#---------
# Option 1
#---------

word = "Corporation"
letters =[]
letter_counter = 0

for letter in word:
    if (word.count(letter) >1 ) and (letter not in letters):
        letter_counter+=1
        letters.append(letter)
    
print(letter_counter)

if len(letters) >0:
    for letter in sorted(letters):
        print(letter,end=' ')
else:
    print(None)
