# Write a Python program that prints a list with the elements that listA and listB have in common.
# If they don't have any elements in common, print an empty list.
# The program should not assume that the lists have the same length.
# You may assume that each element will only appear once in each list.

ListA = [3,4,5]
ListB = [1,2,3]

common_elem =[]

for elem in ListA:
    if elem  in ListB:
        common_elem.append(elem)
    

print(common_elem)