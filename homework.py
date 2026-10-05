# ==========================================
# TASK 1: Create a list of students (add, edit, delete)
# ==========================================
print("========== TASK 1: STUDENT LIST ==========\n")

# Initial list of students
student_list = ["Raymond", "James", "Onditi", "Joshua", "Leakey"]
print(f"Initial List: {student_list}")

# 1. Add a new student
student_list.append("Brian")
print(f"After Adding Brian: {student_list}")

# 2. Edit a student (Let's change 'Onditi' to 'Onditi Jr.')
# Onditi is at index 2 (0:Raymond, 1:James, 2:Onditi)
student_list[2] = "Onditi Jr."
print(f"After Editing Onditi: {student_list}")

# 3. Delete a student (Let's remove Leakey)
student_list.remove("Leakey")
print(f"After Deleting Leakey: {student_list}")
print("\n")


# ==========================================
# TASK 2: Calculate age in 2 years
# ==========================================
print("========== TASK 2: AGE IN 2 YEARS ==========\n")

current_age = 20
age_in_two_years = current_age + 2

print(f"Current age: {current_age} years old.")
print(f"Age in 2 years time: {age_in_two_years} years old.")
print("\n")


# ==========================================
# TASK 3: Dictionary with 5 students
# ==========================================
print("========== TASK 3: STUDENT DICTIONARY ==========\n")

# A clean list of dictionaries holding the 5 students' details
student_records = [
    {
        "Name": "Raymond",
        "Phone": "07",
        "Age": 21,
        "Location": "Nairobi",
        "DOB": "12/05/2002"
    },
    {
        "Name": "James",
        "Phone": "0722222222",
        "Age": 22,
        "Location": "Mombasa",
        "DOB": "23/08/2002"
    },
    {
        "Name": "Onditi",
        "Phone": "0733333333",
        "Age": 20,
        "Location": "Kisumu",
        "DOB": "04/11/2004"
    },
    {
        "Name": "Joshua",
        "Phone": "0744444444",
        "Age": 23,
        "Location": "Nakuru",
        "DOB": "19/01/2001"
    },
    {
        "Name": "Leakey",
        "Phone": "0755555555",
        "Age": 21,
        "Location": "Eldoret",
        "DOB": "30/06/2003"
    }
]

# A clean loop to print each student's details neatly
for student in student_records:
    print(f"Name: {student['Name']}")
    print(f"Phone: {student['Phone']}")
    print(f"Age: {student['Age']}")
    print(f"Location: {student['Location']}")
    print(f"DOB: {student['DOB']}")
    print("-" * 30) # Prints a neat dashed line between students

print("\n")


# ==========================================
# TASK 4: Create 3 Arrays (1D, 2D, 3D)
# ==========================================
print("========== TASK 4: ARRAYS ==========\n")

# 1D Array: A single list of numbers
array_1d = [10, 20, 30, 40, 50]
print(f"1D Array: {array_1d}")

# 2D Array: A grid (Rows and Columns)
array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"2D Array: {array_2d}")

# 3D Array: A cube of data (Layers, Rows, Columns)
array_3d = [
    [ # Layer 1
        [1, 2],
        [3, 4]
    ],
    [ # Layer 2
        [5, 6],
        [7, 8]
    ]
]
print(f"3D Array: {array_3d}")
