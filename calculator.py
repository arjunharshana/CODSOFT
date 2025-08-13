def userInput(prompt):
    # Get user input and handle invalid input
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please try again.")

def getOperation():
    # Get the desired operation from the user
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Invalid operation. Please try again.")

def calculate(num1, num2, operation):
    # Perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            # Raise error on division by zero
            raise ValueError("Error: Division by zero is not allowed.")
        result = num1 / num2

    return result


def runAgain():
    # Asks the user if they want to run another calculation.
    while True:
        again = input("Do you want to perform another calculation? (yes/no): ").lower()
        if again == 'yes':
            return True  # Signal to continue
        if again == 'no':
            return False # Signal to stop
        
        # This line only runs if the input was not 'yes' or 'no'
        print("Invalid input. Please enter 'yes' or 'no'.")

def calculator():
    while True:
        print("\nWelcome to the Simple Calculator!\n")
       
        num1 = userInput("Enter the first number: ")
        num2 = userInput("Enter the second number: ")
        operation = getOperation()

        try:
            result = calculate(num1, num2, operation)
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        except ValueError as e:
            # If a ValueError occurs in the try block, print the error message
            print(f"\n{e}")


        if not runAgain():
            print("\nGoodbye!")
            break # Exit the loop
        
        # If we continue, print a newline for spacing
        print("\n" + "-"*25 + "\n")

if __name__ == "__main__":
    calculator()