# Write a Python program that counts the frequency of each value in a dictionary.
# The program should create a new dictionary to map each value in the original 
# dictionary to its frequency (how many times it occurs).
# If the dictionary is empty, print an empty dictionary.

##########
# Option 1
##########

my_dict = {
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 }

freq_dict =[]
final_freq_dict ={}

for val in my_dict.values():
    freq_dict.append(val)

freq_dict
dict_key = set(freq_dict)


for key in dict_key:
    combo = freq_dict.count(key)
    final_freq_dict.update({key: combo})

print(final_freq_dict)




