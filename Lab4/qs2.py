# Use a list comprehension to create a new list containing only the even numbers between
# 1 and 20, demonstrating a more concise and readable alternative to traditional loops.
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("The even numbers between 1 and 20 are:", even_numbers)