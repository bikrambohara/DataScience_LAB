# Write a program that takes a list of numbers as input, and returns the largest number in
# the list.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)
