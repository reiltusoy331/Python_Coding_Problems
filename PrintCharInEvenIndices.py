
# Write a Python program that prints the string located at even indices.
# If the string is empty or only has one character, print it without any changes.

print("Option # 1")
# ----------
# Option # 1
# ----------
word1 = "Coding"

if len(word1) == 0:
    print(f"the word is empty, \"{word1}\".")
else:
    new_word=word1[1::2]
    print(new_word)


print("\n Option # 2")

# ----------
# Option # 2
# ----------
word2 = "Coding"
new_word2=''

for i in range(len(word2)):
    if i % 2 != 0:
        new_word2 += word2[i]
print(new_word2)


print("\n Option # 3")

# ----------
# Option # 3
# ----------
word3 = "Python"
new_word3=''

for i in range(1,len(word3),2):
    new_word3 += word3[i]

print(new_word3)