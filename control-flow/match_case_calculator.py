# match_case_calculator.py

# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user for the type of operation
operation = input("Choose the operation (+, -, *, /): ")
# Perform the calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Invalid operation."
# Output the result
print(f"The result is {result}")
