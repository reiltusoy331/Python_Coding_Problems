# Generator comprehension

import sys
my_list = []

for num in range(5,10):
    my_list.append(num*num)
print(my_list)

print()

print("List comprehension")
my_list_comp = [num*num for num in range(5,20)]    
print(my_list_comp)
print(f"mem size {sys.getsizeof(my_list_comp)}")

print()

print("Generator comprehension")
my_gen_comp = (num*num for num in range(5,20))
print(my_gen_comp)
print(f"mem size {sys.getsizeof(my_gen_comp)}")