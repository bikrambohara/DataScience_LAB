# CSV File Handling
# ● Read data from a CSV file containing student records (roll number, name, marks)
# ● Display all student records
# ● Handle file-related and data conversion errors using try-except

import csv
try:
    
    with open('student.csv', "r")as file:
        csvFile = csv.reader(file)
        csvFile = list(csvFile)
        if len(csvFile) == 0:
            print("No records found")
        else:
            print("Student Records:")
            for lines in csvFile:
                try:
                    roll_number = int(lines[0])
                    name = lines[1]
                    marks = float(lines[2])
                    print(f"Roll Number: {roll_number}, Name: {name}, Marks: {marks}")
                except IndexError:
                    print("Incomplete record:", lines)
        print("Student Records:")
        for lines in csvFile:
            try:
                roll_number = int(lines[0])
                name = lines[1]
                marks = float(lines[2])
                print(f"Roll Number: {roll_number}, Name: {name}, Marks: {marks}")
            except IndexError:
                print("Incomplete record:", lines)
except ValueError:
         print(f"Data conversion error in line: {lines}")