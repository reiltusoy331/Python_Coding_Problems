# Create a custom function that counts how many times a specific element appears in the list.

def count_occurrences(list_numbers, target):
    count = 0
    for num in list_numbers:
        if num == target:
            count += 1
    return count


my_list = [1, 2, 3, 2, 4, 2, 5]
target_element = 2
result = count_occurrences(my_list, target_element)

print(f"These are the list of numbers",*my_list)
print(f"The element {target_element} appears {result} times in the list.")
