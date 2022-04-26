STUDENTS = ["Mike", "Julia", "Mark", "Lilly", "Hannah", "James"]

print("Are you a student? Let's find out...")

for student_list in STUDENTS:
    print("-" + student_list)
print("\n")

is_student = input("Are you a student?\n(yes/no):")

if is_student.lower()[:1] == "y":
    student_name = input("What is your name?\n")
    if student_name in STUDENTS:
        print("Welcome to class")
    else:
        print("You're not supposed to be here")

elif is_student.lower()[:1] == "n":
    exit()

