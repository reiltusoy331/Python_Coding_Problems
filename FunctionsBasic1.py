# Global Variable vs Local Variable

number = 12

def PrintNumber():
    number = 3
    return number


num=PrintNumber()
print(num)
print(number)