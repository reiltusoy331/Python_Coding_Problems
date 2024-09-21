# Write a Python program that takes the content of a dictionary and converts it into a list of lists.
# Each nested list should contain a key as the first element and its corresponding value as the second element.
# Print the final list of lists.

##########
# Option 2
##########
product_info = {
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
}

my_list =[]

for key, value in product_info.items():
    my_list.append([key,value])
    
print(my_list)