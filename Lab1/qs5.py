## Define a function that takes two numbers as arguments, and returns their greatest common divisor (GCD).

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def gcd(a, b):
    while b != 0:
        temp = a % b  # store the remainder of a divided by b
        a = b         # assign b to a
        b = temp  
    return a
    
# Call the function and print the result
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")