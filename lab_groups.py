# lab_groups.py
# This program calculates the number of full lab groups and remaining students

# Number of PCs per lab
group_size = 24

# List of student numbers
student_counts = [113, 175, 12]

# Calculate and display results for each student count
for students in student_counts:
    full_groups = students // group_size
    leftover_students = students % group_size
    print(f"For {students} students:")
    print(f"  Full groups: {full_groups}")
    print(f"  Leftover students: {leftover_students}\n")
