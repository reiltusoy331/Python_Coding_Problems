sentence = "This is a common interview question."

letter_frequency = {}

for letter in sentence:
    if letter in letter_frequency:
        letter_frequency[letter] +=1
    else:
        letter_frequency[letter] = 1

letter_frequency_sorted = sorted(letter_frequency.items(),key=lambda kv:kv[1],reverse=True)

print(f"Which letter has the most number of occurrence in this sentence \"{sentence}\"")
print(f"The answer is: {letter_frequency_sorted[0]}")
