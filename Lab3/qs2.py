# 2. File Processing with Exception Handling
# ● Reads numbers from a text file (one number per line)
# ● Ignores invalid entries using exception handling
# ● Calculates and displays the sum and average of valid numbers

try:
    file = open("sample.txt", "r")

    total = 0
    count = 0

    for line in file:
        try:
            num = int(line)
            total += num
            count += 1
            average = total / count
        except ValueError:
            print("please enter only numbers")

    file.close()

    if count >= 0:
        print("Sum of valid numbers:", total)
        print("Average of valid numbers:", average)
    else:
        print("No valid numbers found")

except FileNotFoundError:
    print("File does not exist")
