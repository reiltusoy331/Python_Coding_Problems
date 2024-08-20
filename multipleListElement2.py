# Write a Python program that multiplies all the items in a list by the value of the 
# variable factor. The program must print the list as the output.
# The program should also allow multiplying the variable factor by a string in case the 
# list contains strings. You may assume that the value of factor will be a positive integer.

#---------- 
# Option 2
#----------

list = [3,4,5,6]
factor = 2

for i in range(len(list)):
    list[i] *=factor
    
print(list)