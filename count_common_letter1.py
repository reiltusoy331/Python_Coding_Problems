sentence = "This is a common interview question."

letters = []
highest_count = 0
highest_letter = ""

for letter in sentence:
    counter = sentence.count(letter)        
    if counter > highest_count:
        highest_count = counter  
        highest_letter = letter         

print("#####################################################################################")
print("#### Count the letter with the most number of occurrence in the sentence below. ####")
print("#####################################################################################\n")

print(sentence)
print(f"The answer is: \"{highest_letter}\"")
print(f"Total occurence of: \"{highest_count}\"")      
    

