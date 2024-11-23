def display_menu():
    print("\nSimple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def format_number(number):
    """Return the number as an integer if it's a whole number, otherwise as a float."""
    if number == int(number):
        return int(number)
    return number

def format_result(result):
    """Format the result to remove the .0 if it's a whole number."""
    if result == int(result):
        return int(result)
    return result

def main():
    while True:
        display_menu()

        # Get user choice for operation
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            # Addition
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            num1 = format_number(num1)  # Format num1
            num2 = format_number(num2)  # Format num2
            result = num1 + num2
            result = format_result(result)  # Format result
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == '2':
            # Subtraction
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            num1 = format_number(num1)
            num2 = format_number(num2)
            result = num1 - num2
            result = format_result(result)
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == '3':
            # Multiplication
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            num1 = format_number(num1)
            num2 = format_number(num2)
            result = num1 * num2
            result = format_result(result)
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == '4':
            # Division with failsafe for division by zero
            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")
            num1 = format_number(num1)
            num2 = format_number(num2)
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                result = format_result(result)
                print(f"Result: {num1} / {num2} = {result}")

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break  # Exit the program if the user selects '5'

        else:
            print("Invalid choice! Please choose a valid operation.")
            continue  # If invalid choice, prompt again for operation

        # Ask if the user wants to continue after each operation
        while True:
            continue_choice = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if continue_choice in ['yes', 'y', 'yes', 'y', 'no', 'n', 'no']:
                break
            else:
                print("Invalid input! Please type yes, y, YES, no, n, N, NO.")

        if continue_choice in ['no', 'n', 'NO', 'N']:
            print("Exiting the calculator. Goodbye!")
            break  # Exit if the user says no

if __name__ == "__main__":
    main()
