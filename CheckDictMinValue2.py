# Write a Python program that prints the smallest value in a dictionary.
# If the dictionary is empty, print None.
# You may assume that the values are numeric.
# You may print "None" as a string or as the special value None.

##########
# Option 2
##########

my_dict = {}

 
if my_dict:
    min_value = min(set(my_dict.values()))
    print(min_value)
    
else:
    print("None")
    
