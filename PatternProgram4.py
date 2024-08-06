# Declare a variable name "num_row" 
# The said variable will dictate the number of rows of the triangle pattern
### Target Output ###
#  *
#  * *
#  * * *
#  * * * *

num_row = 4

for i in range(num_row):
    for j in range(i+1):
        print("* ",end='')
    print()