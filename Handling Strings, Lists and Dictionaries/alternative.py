"""

This script defines two functions:

1. alternate_case_characters: It takes a string input and returns a new string 
where each alternate character is converted to uppercase and each other 
alternate character is converted to lowercase.

2. alternate_case_words: It takes a string input and returns a new string where 
each alternate word is converted to lowercase and each other alternate word is 
converted to uppercase. The main function takes user input, applies both 
functions to the input string, and prints the results.

"""

# Function to make each alternate character into an upper case character
# and each other alternate character a lower case character.
def alternate_case_characters(input_string):
    result = ""
    for i, char in enumerate(input_string):
        if i % 2 == 0:  # If the index is even, make the character uppercase
            result += char.upper()
        else:  # If the index is odd, make the character lowercase
            result += char.lower()
    return result

# Function to make each alternate word lower and upper case.
def alternate_case_words(input_string):
    words = input_string.split()  # Split the input string into words
    result = []
    for i, word in enumerate(words):
        if i % 2 == 0:  # If the index is even, make the word lowercase
            result.append(word.lower())
        else:  # If the index is odd, make the word uppercase
            result.append(word.upper())
    return ' '.join(result)  # Join the modified words into a string with spaces between them

# Main function to take user input and demonstrate the functions
def main():
    input_string = input("Enter a word or sentence: ")

    print("\n----------------------------------")
    print("Alternate Case Characters:", alternate_case_characters(input_string))
    print("Alternate Case Words:", alternate_case_words(input_string))
    print("----------------------------------")

if __name__ == "__main__":
    main()
