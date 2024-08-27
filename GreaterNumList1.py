# Write a Python program that counts the number of elements in a list with value greater than 3.
# You may assume that the list only contains numbers.
# Print the final count.

#---------
# Option 1
#---------

lists = [1,2,3,4,5]

counter = 0

for num in lists:
    if num > 3:
        counter +=1

print(counter)