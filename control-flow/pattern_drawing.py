size_error = True

while size_error:
    try:
        size = int(input("Enter the size of the pattern: "))
        size_error = False
    except ValueError:
        print("Invalid input.")

for i in range(size):
    
    for j in range(size):
        print("*", end="")

    print()  # Move to the next line after each row
