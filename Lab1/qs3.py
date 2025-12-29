# Write a program that prints all prime numbers up to a given number ‘n’

try:
    n = int(input("Enter a number: "))

    for num in range(2, n + 1):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print(num, end=" ")

except ValueError:
    print("Error: Please enter a valid number.")
