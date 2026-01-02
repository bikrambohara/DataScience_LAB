# Write a Python script that takes a list of six student names and uses the
# random.sample() function to randomly select exactly three "Volunteers" for a
# presentation, ensuring that no student is picked more than once in the selection.
import random
def student():
    student_names = []
    for i in range(6):
        student = input("Enter the name of the six student:")
        student_names.append(student)
    volunteer = random.sample(student_names, 3)
    print("The Volunteers are:", volunteer)

student()
