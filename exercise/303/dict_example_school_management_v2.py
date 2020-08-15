print("School management system starts")

school = {}
current_class = None

while (True):
    command = input("Command:")

    if command == "exit":
        break;

    # New Class: Tiger
    if command.startswith("New Class: "):
        class_name = command[11:]
        if class_name in school:
            print(f"Error! {class_name} already exists")
        else:
            school[class_name] = {}
            current_class = school[class_name]
            print("Now we have classes", list(school.keys()))
            print("Change class to: ", class_name)

    # New Student: Yinuo
    elif command.startswith("New Student: "):
        student_name = command[13:]
        student_id = len(current_class.keys()) + 1
        current_class[student_id] = student_name
        for (key, value) in current_class.items():
            print(f'Student id {key}, student name {value}')

    # Change Class: Bear
    elif command.startswith("Change Class: "):
        class_name = command[14:]
        if (class_name not in school):
            print(f"Error! {class_name} doesn't exist")
        else:
            current_class = school[class_name]
            print("Change class to:", class_name)

    # List Class
    elif command.startswith("List Class"):
        print(current_class)

    # Student Leaves Class: Alex
    elif command.startswith("Student Leaves Class: "):
        student_name = command[22:]
        for key, value in current_class.items():
            if student_name == value:
                current_class.pop(key)
                break;
        else:
            print(f"{student_name} is not in current class")


    # Student Changes Class: Yinuo Bear
    elif command.startswith("Student Changes Class: "):
        print("Student change class")
        student_name, class_name = command[23:].split()

        # Move student out of current Class - Copy Paste 过来的
        for key, value in current_class.items():
            if student_name == value:
                current_class.pop(key)
                break;
        else:
            print(f"{student_name} is not in current class")

        print(current_class)

        # Change class - Copy Paste 过来的
        if (class_name not in school):
            print(f"Error! {class_name} doesn't exist")
        else:
            current_class = school[class_name]
            print("Change class to:", class_name)

        # Add student to Class - Copy Paste 过来的
        student_id = len(current_class.keys()) + 1
        current_class[student_id] = student_name
        for (key, value) in current_class.items():
            print(f'Student id {key}, student name {value}')

        print(current_class)