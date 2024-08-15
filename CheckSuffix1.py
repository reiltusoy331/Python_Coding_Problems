# Write a Python program that checks if the string s ends with a specific sequence of characters 
# denoted by the variable suffix.
# If it does, print True. Else, print False.
# This test should be case sensitive. Therefore, "A" should not be equivalent to "a".
#---------
# Option 1
#---------

word = "classmate"
suffix = "mate"


if(word[-len(suffix):]==suffix):
   print("True")
else:
    print("False")


