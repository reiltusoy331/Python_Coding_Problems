# Write a Python program that prints (as a list) the elements of listA that are not in listB.
# If the lists have the same elements, print an empty list.
# If listA is an empty list, print an empty list.
# Please assume that listA will be smaller than listB (will have fewer elements).

ListA = [1,2,3,4]
ListB = [1,2,3]

diff_list =[]

for elem in ListA:
    if elem not in ListB:
        diff_list.append(elem)
    

print(diff_list)