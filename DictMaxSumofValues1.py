# Write a Python program that prints the maximum sum of the values in a dictionary.
# You may assume that all the values in the dictionary are either lists or tuples.

my_dict = {
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
}

my_list =[]

for values in my_dict.values():
    my_list.append(sum(values))

print(max(my_list))

