
grades = {
    "Benson": "F",
    "Taylor": "F",
    "Bruno": "B"
}

name = input("Enter student name: ")

found = False

for student in grades:
    if name == student:
        print("Grade:", grades[student])
        found = True
        break

if found == False:
    print("Student not found.")

