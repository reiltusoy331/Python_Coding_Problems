# Write a Python program that prints if a given year was (or will) be a leap year.
# -> This is how you can determine if a year is a leap year or not:
# -> if (year is not divisible by 4) then (it is a common year).
# -> else if (year is not divisible by 100) then (it is a leap year)
# -> else if (year is not divisible by 400) then (it is a common year)
# -> else (it is a leap year)
##########
# Option 1
##########

input_year = 1912

if (input_year %4 != 0) and  (input_year %100 == 0) and (input_year %400 == 0):
    print(f"{input_year} is not a leap year.")

else:
    print(f"{input_year} is a leap year.")
