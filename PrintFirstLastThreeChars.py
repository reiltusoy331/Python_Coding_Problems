print("This Python program prints the first and last three characters of a word.")
print("If the entered word is less than six characters, the output is empty.")
print()

word = input("Enter a word: ")


if len(word) < 6:
    print(" ")
else:
    new_word = word[:3] + word[-3:]
    print("The answer is: ",new_word)


