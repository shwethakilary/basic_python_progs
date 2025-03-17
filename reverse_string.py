#reverse string using slicing
word = input("Enter the word: ") # Get user input
reverse_word = word[::-1] # Reverse the string
print(reverse_word)

#revrese string using for loop
word = input("Enter the word: ") # Get user input
reverse_word = ""
for i in range(len(word) - 1, -1, -1): # Loop through the string in reverse order
    reverse_word += word[i] # Add each character to the reverse_word string
print(reverse_word)

#reverse string using while loop
word = input("Enter the word: ") # Get user input
reverse_word = ""
i = len(word) - 1 # Set the index to the last character
while i >= 0: # Loop through the string in reverse order
    reverse_word += word[i] # Add each character to the reverse_word string
    i -= 1 # Decrement the index
print(reverse_word)

#reverse string using recursion
def reverse_string(word):
    if len(word) == 0: # Base case: if the string is empty, return an empty string
        return ""
    else:
        return word[-1] + reverse_string(word[:-1]) # Recursive case: add the last character to the reversed string of the rest of the string   
    print(reverse_string(input("Enter the word: ")))    


#reverse string using built-in function
word = input("Enter the word: ") # Get user input
reverse_word = "".join(reversed(word)) # Reverse the string
print(reverse_word)