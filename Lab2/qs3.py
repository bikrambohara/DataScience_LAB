# Student Marks Manager
# Store student names as keys and marks (list of integers) as values in a dictionary. Compute
# each student’s average and grade (A/B/C/D). Print the top 2 students based on average marks.

students = {
    "Bikram": [90, 90, 80, 70, 50],
    "Bohara": [74, 70, 93, 92, 80],
    "Nikhil": [70, 90, 60, 70, 95]
}

# Function to calculate grade based on average marks
def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    elif avg >= 50:
        return 'E'
    else:
        return 'F'

# Calculate average and grade for each student
student_results = {}
for name, marks in students.items():
    avg = sum(marks) / len(marks)
    grade = calculate_grade(avg)
    student_results[name] = {"Average": avg, "Grade": grade}

# Print each student's average and grade
print("Student Results:")
for name, result in student_results.items():
    print(name, "Average:", result["Average"], "Grade:", result["Grade"])

# Find top 2 students based on average
top_students = sorted(student_results.items(), key=lambda x: x[1]["Average"], reverse=True)[:2]

print("\nTop 2 Students:")
for name, result in top_students:
    print(name, "with average marks:", result["Average"])
