while True:
    try:
        # Attempt to take user input and convert it to an integer
        user_input = int(input("Please enter a number: "))
        print(f"You entered: {user_input}")
        break  # If successful, exit the loop
    except ValueError:
        # Catch the ValueError if the user input is not a valid integer
        print("Invalid input. Please enter a valid number.")
