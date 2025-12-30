# Write a program that takes a temperature in Celsius, and converts it to Fahrenheit and
# Kelvin, based on the choice of user.

# Temperature Conversion Program

celsius = float(input("Enter temperature in Celsius: "))

print("Choose conversion:")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == 2:
    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)

else:
    print("Invalid choice")
