# 2. Unique Words Collector
# Take a paragraph input from the user. Split it into words, remove duplicates, sort them
# alphabetically, and count the total number of unique words.

paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

unique_words = set(words)
sorted_words = sorted(unique_words)

count = len(sorted_words)

print("\nUnique words (sorted):")
print("The shortest word is:", sorted_words)
print("Total number of unique words:", count)


