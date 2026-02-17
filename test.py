emp_id_input = input(" what is your ID?: ")
print(emp_id_input.isdigit())

while not emp_id_input.isdigit():
    emp_id_input = input("Invalid ID. Please enter a numeric value: ")
print(type(emp_id_input))
