# Write a Python program that creates a dictionary from the values contained in nested lists.
# Each nested list has this format [value1, value2].
# value1 should be the key in the dictionary and value2 should be its corresponding value.
# If there are no nested lists, print an empty dictionary.

nested_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
#nested_list = []

dict_nested_list={}

if nested_list:
    for value in nested_list:    
        dict_nested_list.update({value[0]:value[1]})
    print(dict_nested_list)
else:
    print('Empty')
    






