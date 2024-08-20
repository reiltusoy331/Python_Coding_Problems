# Write a Python program that multiplies all the items in a list by the value of the 
# variable factor.
# The program must print the list as the output.
# The program should also allow multiplying the variable factor by a string in case the 
# list contains strings.
# You may assume that the value of factor will be a positive integer.

#---------- 
# Option 1
#----------

list = ["a","b","c"]
factor = 3
new_list =[]

for element in list:
    element *=factor
    new_list.append(element)


print(new_list)