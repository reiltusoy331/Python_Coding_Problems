#Write a Python program that prints a triangular pattern made with letters (as shown below).
# The first row should have one letter A (in uppercase). The second row should have two letters B. 
# The third row should have three letters C and so on.
# The number of rows is determined by the value of n, which is entered by the user.
# The letters must be separated by a space.

n = int(input("Enter the value of \"n\": "))
for i in range(1,n+1):    
    print(chr(i + 64) * i)           
    