## Write a program that takes two numbers as input from the user, and print their sum.

try:
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))

    if(a.is_integer()):
        a = int(a)

    if(b.is_integer()):
        b = int(b)

    print(f"The sum of {a} and {b} is {a+b}")
except ValueError:
    print("Invalid input:please enter the valid number.")