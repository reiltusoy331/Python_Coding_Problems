# Write a Python program that prints a "flattened" version of a list that contains nested lists.
# "Flattened" means that all the elements in the nested lists should be added to a main list such that it doesn't contain any nested lists, just the individual.
# The list could contain other elements that are not lists or other sequences, so you must check the type of each element and act appropriately.
# If the list is empty, print an empty list.

# my_list=[[1,2,3],[4,5,6],[7,8,9]]
my_list=[1,2,3,4,5,6,[7,8,9]]
flat_list=[]


for elem in my_list:
    if isinstance(elem,list):
        for nested_elem in elem:
            flat_list.append(nested_elem)

    else:
        flat_list.append(elem)

print(flat_list)