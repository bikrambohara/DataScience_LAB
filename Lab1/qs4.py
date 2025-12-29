# Write a python program that prints the Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))
print(f"The Fibonacci is {n}:")
a = 0
b = 1
count = 0
while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1



