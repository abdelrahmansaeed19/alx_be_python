first_num_error = True
while first_num_error:
    try:
        first_num = int(input("Enter the first number: "))
        first_num_error = False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
second_num_error = True
while second_num_error:
    try:
        second_num = int(input("Enter the second number: "))
        second_num_error = False
    except ValueError:
        print("Invalid input. Please enter a valid number.")
operation_error = True
while operation_error:
    try:
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if operation not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operation. Please enter one of +, -, *, /.")
        operation_error = False
    except ValueError as e:
        print(e)
# This code prompts the user to enter two numbers and an operation, ensuring valid inputs.

def calculate(first_num, second_num, operation):
    res = None
    match operation:
        case '+':
            res = first_num + second_num
        case '-':
            res = first_num - second_num
        case '*':
            res = first_num * second_num
        case '/':
            try:
                res = first_num / second_num
            except ZeroDivisionError:
                res = None
                print("Cannot divide by zero.")
        case _:
            res = None
            print("Error: Invalid operation.")
    
    return res
# This function performs the calculation based on the operation provided.
result = calculate(first_num, second_num, operation)
if isinstance(result, int):
    print(f"The result is {result}.")
