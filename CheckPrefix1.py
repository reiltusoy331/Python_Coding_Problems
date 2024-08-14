# Write a Python program that checks if the variable word 
# starts with the sequence of characters denoted by the variable prefix.
# If it does, print True. Else, print False.
#---------
# Option 1
#---------

word = "Probono"
Prefix="Pro"

print(word[:len(Prefix)]==Prefix)

