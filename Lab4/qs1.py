# Write a Python script that takes a list of student marks and sorts them in descending
# order (highest to lowest) using either the sorted() function or the .sort() method.
student = int(input("Enter the number of students: "))
student_marks = []
for i in range(student):
    marks = float(input("Enter the marks of student: "))
    student_marks.append(marks)
def sorted_list(student_marks):
    sorted_list = sorted(student_marks, reverse=True) #reverse=True sorts the list in descending order (highest to lowest).
    return sorted_list
print(sorted_list(student_marks))
