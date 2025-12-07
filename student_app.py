students = []

def add_student():
    name = input("Name: ")
    branch = input("Branch: ")
    roll_no = int(input("Roll number: "))
    students.append({"name": name, "roll": roll_no})

def view_students():
    for s in students:
        print(s)

while True:
    print("1. Add 2. View 3. Exit")
    choice = int(input("Enter : "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    else:
        break