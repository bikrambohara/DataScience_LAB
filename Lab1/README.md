# Lab 1
- [Question 1](#question-1)
- [Question 2](#question-2)
- [Question 3](#question-3)
- [Question 4](#question-4)
- [Question 5](#question-5)


## Question 1
Write a Python program to add two numbers.

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
    