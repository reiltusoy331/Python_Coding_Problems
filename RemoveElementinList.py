# Write a Python program that removes all occurrences of the element elem_to_remove from a list.
# The output of the program should be the new list with the element removed.
# If the element is not found in the list, print the message "Not Found".
# If the list is empty, print "Empty List".

my_list =[1,2,3,3,4]
elem_to_remove = 3

if not list:
    print("Empty List") 
        
elif my_list.remove(elem_to_remove) == 0:
    print("Not Found") 
    
else:
    for i in range(my_list.count(elem_to_remove)):
        my_list.remove(elem_to_remove)
        
print(my_list)