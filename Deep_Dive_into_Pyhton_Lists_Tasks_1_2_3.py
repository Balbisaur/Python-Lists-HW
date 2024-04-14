students = ["John","Doe","Jane","Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

print('Jane', grades[2], activities[2])

students_approved = []
for index in range(len(grades)):
    if grades[index] > 80:
        students_approved.append(students[index])
print(students_approved)