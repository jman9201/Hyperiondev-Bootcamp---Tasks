# prompt the user to enter a sentence
# Save the response in a variable called str_manip
# Calculate and display the variable str_manip
# Find the last letter in str_manip sentence and replace every occurrence of this letter in str_manip with '@'
# Print the last three characters in str_manip backwards
# Create a five-letter words that is made up of the first three characters and the last two characters in str_manip


# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")
str_manip = sentence

# Calculate and display the number of characters in the sentence
count_str = len(str_manip)
print("The number of words in the sentence:", count_str)

# Find the last letter in the string
last_letter = sentence[-1]

# Replace every occurrence of the last letter with '@'
result = sentence.replace(last_letter, '@')
print("Replacing the last letter in the sentence with '@':", result)

# Extract the lst three characters
last_three = str_manip[-3:]

# Reverse the order of characters
last_three_reversed = last_three[::-1]
print("The last 3 letters in the sentence in reversed:", last_three_reversed)

# Create a five letter word using the first three char & last char in the sentence
five_letter_words = str_manip[:3] + str_manip[-2:]
print("A five-letter word made up of the first three characters and the last two characters in the sentence: ", five_letter_words)