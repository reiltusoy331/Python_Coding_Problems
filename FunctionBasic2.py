# Define a simple function
def greet(name):
    return f"Hello, {name}!"

# Assign the function to a variable
greeting_function = greet

# Call the function using the new variable
print(greeting_function("Alice"))

# Pass the function as an argument to another function
def execute_function(func, value):
    return func(value)

print(execute_function(greet, "Bob"))
