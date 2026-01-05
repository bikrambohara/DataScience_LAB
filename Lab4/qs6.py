# Given a list of student names and a list of their corresponding scores, use the zip()
# function to pair them together and then apply the reduce() function from the
# functools module to calculate the total sum of all scores.

from functools import reduce

students = ["Nikhil", "Bikram", "Mandip", "Ayush"]
scores = [85, 92, 78, 90]

student_scores = list(zip(students,scores))

print("Student Score pairs: ", student_scores)

total_score = reduce(lambda x,y:x+y,scores)
print("Total Score of all students: ", total_score)