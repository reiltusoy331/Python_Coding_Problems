numbers = []
even_nums = []
odd_nums = []


while True:
    user_input = input("Enter a number, or type 'done' to exit: ")

    if user_input.lower() == 'done':  # Check if the user wants to exit
        break

    # Handle invalid inputs (non-numeric values)
    if user_input.isdigit():  # This ensures only numbers are entered
        numbers.append(int(user_input))
    else:
        print("Invalid input. Please enter a valid number.")

for number in numbers:
    if number % 2 == 0:
        even_nums.append(number)        
    else:
        odd_nums.append(number)

print("All the numbers inputted:",*numbers)        
print("Even numbers:",*even_nums)        
print("Odd numbers:",*odd_nums)        
    
    

    