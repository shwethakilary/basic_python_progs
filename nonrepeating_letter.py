sentence = input("Enter the word: ") # Get user input
def nonrepeat(word): # define the function
    for i in range(len(word)): # loop through the word
        if word.count(word[i]) == 1:  # Count occurrences of each character
            return word[i]  # Return the index of the first non-repeating character
    return -1  # If all characters repeat, return -1

result = nonrepeat(sentence) # call the function
print(result) # print the result
