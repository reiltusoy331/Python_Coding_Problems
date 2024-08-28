# Write a Python program that finds the intersection of two sets (set1 and set2).
# Create a new set called intersection with their intersection.
# Print the new set as the output.
# If the intersection is empty, print an empty set.

#---------
# Option 1
#---------

set1={1,2,3,4}
set2={3,4,5,6}

intersection= set() 

for element in set1:
    if element in set2:
        intersection.add(element)

print(intersection)
