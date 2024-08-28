# Write a Python program that finds the intersection of two sets (set1 and set2).
# Create a new set called intersection with their intersection.
# Print the new set as the output.
# If the intersection is empty, print an empty set.

#---------
# Option 2
#---------
# built-in python method

set1={1,2,3,4}
set2={3,4,5,6}
set3={4,5,6,7}

print(set1.intersection(set2))
print(set1.intersection(set2,set3))

# other method
# print(set1 & set2)