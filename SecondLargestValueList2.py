# Write a Python program that prints the second largest value in a list.
# If the list is empty or only has one element, print None.

#---------
# Option 2
#---------

my_list=[3,2,1]

if len(my_list) > 1:
    no_dups = set(my_list)
    no_dups.remove(max(no_dups))    
    print(max(no_dups))
            
else:
    print("None")

