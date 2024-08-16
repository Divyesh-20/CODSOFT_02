# Function to perform arithmetic operations
def calculator(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation choice!"

# Main program
def main():
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        # Get user input
        operation = input("Enter the number of the operation (1/2/3/4): ")

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform calculation and display the result
            result = calculator(num1, num2, operation)
            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        # Ask the user if they want to continue
        continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator program
if __name__ == "__main__":
    main()    