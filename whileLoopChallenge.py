even_num = []
odd_num = []
numbers = []  # This will collect all the numbers
input_num = ''

while input_num != "done":        
    input_num = input("Enter a number, to exit type \"done\"(w/o quotes): ")

    if input_num != "done":
        try:
            num = int(input_num)  # Convert the input to an integer
            numbers.append(num)  # Add the number to the list of all numbers

            if num % 2 == 0:  # Even number
                even_num.append(num)
                if len(even_num) == 1:  # Only print the first even number
                    print(f"The first even number is {even_num[0]}")
            else:  # Odd number
                odd_num.append(num)
                print(f"Odd number added: {num}")
        except ValueError:
            print("Please enter a valid number.")
    else:
        break

# After the loop ends
if numbers:
    print(f"These are the numbers you inputted: {numbers}")
else:
    print("No numbers were inputted.")
