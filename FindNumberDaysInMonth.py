# Write a Python program that prints the number of days in a given month.
# The value of the variable month is the name of the month with the first letter capitalized.
# Do not consider leap years for the number of days in February.
# You can add a customized message. For example: "<month> has: <num_days> days."

month = "February"

month_with_31days = ("January","March","May","July","August","October","December")
month_with_30days = ("April","June","September","November") 

if month in month_with_31days:
    print(f"{month} has 31 days.")

elif month in month_with_30days:
    print(f"{month} has 30 days.")

else:    
    print(f"{month} has 28 days.")
