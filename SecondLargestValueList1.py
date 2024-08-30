# Write a Python program that prints the second largest value in a list.
# If the list is empty or only has one element, print None.

#---------
# Option 1
#---------

my_list=[3,5,1]

if len(my_list) > 1:
    list_sorted=sorted(my_list)
    print(list_sorted)
    print(f"The second largest value in the list is \"{list_sorted[-2]}\"")    
        
else:
    print(None)

