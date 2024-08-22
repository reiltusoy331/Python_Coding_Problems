# Write a Python program that prints the largest and smallest values in a list
# Print the two values on the same line, separated by a space.
# The largest value should appear first and the smallest value should appear second.
# You may assume that the list only contains numeric values.
# If the list is empty, print None.

#---------- 
# Option 1
#----------

list_numbers=[1,2,3,4,5]

if list_numbers:
    print(f"{max(list_numbers)} {min(list_numbers)}")

else:
    print("None")