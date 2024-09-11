# Write a Python program that checks if all values in a dictionary are equal.
# If they are, print True. Else, print False.
# If the dictionary is empty, print "Empty".

#########
#Option 2
#########

my_dict = {"a":4,"b":7}

if my_dict:
    max_value = max(set(my_dict.values()))
    print(max_value)
       
else:
    print(None)     
    
    












