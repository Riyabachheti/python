# 19. Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    
    # Use the translation table to remove punctuation
    return input_string.translate(translator)

# Example usage:
input_string = "Hello, world! How's it going?"
cleaned_string = remove_punctuation(input_string)

print("Original string:", input_string)
print("String without punctuation:", cleaned_string)
