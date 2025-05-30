num_error = False
while not num_error:
    try:
        number = int(input("Enter a number to see its multiplication table:"))
        if number < 0:
            raise ValueError
        num_error = True
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid non-negative integer.")

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")