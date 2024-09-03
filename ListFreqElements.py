# Write a Python program that creates and print a dictionary that maps each element in a list to its 
# corresponding frequency (how many times it occurs in the list).
# The test should be case-sensitive. Therefore, "A" should not be considered the same element as "a".

my_list=["a","d","b","b","d","c","a"]
freq_elem ={}


for elem in my_list:
    if elem not in freq_elem:
        freq_elem[elem] =1
    else:
        freq_elem[elem] += 1

print(freq_elem)