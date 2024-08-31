# Write a Python program that prints the second smallest value in a list.
# If the list is empty or only has one element, print None.

my_list = [1,]

#---------
# Option 2
#---------

if len(my_list) >1: 
    no_dups = set(my_list)
    no_dups.remove(min(no_dups))
    print(min(no_dups))

else:
    print(None)


    


    
    
