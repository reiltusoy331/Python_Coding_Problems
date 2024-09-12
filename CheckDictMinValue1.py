# Write a Python program that prints the smallest value in a dictionary.
# If the dictionary is empty, print None.
# You may assume that the values are numeric.
# You may print "None" as a string or as the special value None.

##########
# Option 1
##########

my_dict = {"a":4,"b":5,"c":6}

if my_dict=={}:
    print("None")
else:
    print(min(set(my_dict.values())))
