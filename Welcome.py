def employee_details():
    try:
        name = input("Enter you Name: ")
        while name == "":
            name = input("Name cannot be empty. Please enter your Name: ")
        if name.isdigit():
            name = input("Name cannot be Numeric. Please enter your Name: ")

        emp_id = int(input(f"{name}, what is your ID?: "))

        if emp_id < 30:
            print(f"Hello {name}, welcome to  dev team")
        else:
            print(f"Hello {name}, Welcome to Ops Team")
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")


employee_details()
