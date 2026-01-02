# Use the re module to write a script that searches through a paragraph and extracts all
# words that start with an uppercase letter (e.g., "London", "Python") to identify proper
# nouns or sentence starters.


# import re
# paragraph = input("Enter a paragraph: ")
# words = re.findall(r'\b[A-Z][a-z]+\b', paragraph) # Find all words that start with an uppercase letter
# print("Proper nouns or sentence starters:", words)

import re
paragraph = input("Enter a paragraph: ")
def extract_words(paragraph):
    words = re.findall(r'\b[A-Z][a-z]+\b', paragraph)
    return words
print(extract_words(paragraph))