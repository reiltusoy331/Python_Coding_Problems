# Write a Python program that prints the second smallest value in a list.
# If the list is empty or only has one element, print None.

my_list = [1,5,3,2,4]

#---------
# Option 1
#---------

if len(my_list) >1: 
    sorted_list = sorted(my_list)
    print(sorted_list[1])

else:
    print(None)


    


    
    
