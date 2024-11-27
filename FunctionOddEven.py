
def determine_numbers(num1, num2):
    # Check if num1 is odd or even
    if num1 % 2 == 0:
        result1 = "even"
    else:
        result1 = "odd"
    
    # Check if num2 is odd or even
    if num2 % 2 == 0:
        result2 = "even"
    else:
        result2 = "odd"
    
    # Return both classifications as a tuple
    return result1, result2


result = determine_numbers(4, 7)
print(result)  
