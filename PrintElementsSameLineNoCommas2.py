# Write a Python program that prints the elements of a list on the same line.
# The elements should be separated only by a space (not by a comma).
# The output should not include the opening and closing square brackets [ ].

#---------------
# Option 2
#---------------
list_alphabet =["a","b","c","d"]
list_numbers=[1,2,3,4,5]


print(*list_alphabet,sep=' ')
print(*list_numbers,sep=' ')


