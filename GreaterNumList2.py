# Write a Python program that counts the number of elements in a list with value greater than 3.
# You may assume that the list only contains numbers.
# Print the final count.

#---------
# Option 2
#---------
#list comprehension

lists = [1,2,3,4,5,6]

counter = sum(1 for num in lists if num > 3)

print(counter)