# Write a Python program that checks if the variable word 
# starts with the sequence of characters denoted by the variable prefix.
# If it does, print True. Else, print False.
#---------
# Option 2
#---------

word = "Probono"
Prefix="pro"

result=word.startswith(Prefix)
print(f"Does the word: \"{word}\" has the prefix of \"{Prefix}\"?")
print(f"Result: {result}")

