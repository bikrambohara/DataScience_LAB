# 5. Word Reverser Game
# Ask the user for a list of words. Reverse each word only if its length is even. Print the new list of
# words after processing.

words_input=input("Enter the words seperate by the space:")
words=words_input.split()
reversed_words=[]
for word in words:
    if len(word)%2==0:
        reversed_words.append(word[::-1])
    else:
        reversed_words.append(word)
        

print(" ".join(reversed_words))