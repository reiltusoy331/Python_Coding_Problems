
even_numbers = 0
for number in range(1,10):
    if number % 2 == 0:
        print(number)
        even_numbers += 1

print(f"We have {even_numbers} even numbers.")

