def employee_details():
    try:
        name = input("Enter you Name: ")
        while name == "":
            name = input("Name cannot be empty. Please enter your Name: ")
        if name.isdigit():
            name = input("Name cannot be Numeric. Please enter your Name: ")

        emp_id_input = input(f"Hey {name}, what is your ID?: ")

        while not emp_id_input.isdigit():
            emp_id_input = input("Invalid ID. Please enter a numeric value: ")

        emp_id = int(emp_id_input)

        if emp_id < 30:
            print(f"Hello {name}, welcome to  dev team")
        else:
            print(f"Hello {name}, Welcome to Ops Team")
    except ValueError:
        print("check the program execution again")


employee_details()
