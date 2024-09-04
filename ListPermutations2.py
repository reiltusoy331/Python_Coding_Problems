# Write a Python program that generates and prints all the possible permutations of a list.
# A permutation is a possible arrangement of the elements of the list. For example, 
# [2, 1, 3] is a permutation of [1, 2, 3].
# Print each permutation as a list on a separate line. You can print them as lists or tuples.
# Include the list itself as a permutation.
# HINT: The permutations function of the itertools module can be very helpful to solve this exercise. 
# You can import this module with import itertools.

##########
# Option 2
##########

import itertools

my_list = [1,2,3]

for permutation in itertools.permutations(my_list):
    print(list(permutation))
    