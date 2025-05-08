# Question 1: Arithmetic and Assignment Operators
print("\n--- Question 1: Arithmetic and Assignment Operators ---")

# Starting with two numbers
x = 5
y = 4
print(f"Initial values: x = {x}, y = {y}")

# Add 3 to x using the shorthand += operator
x += 3
print(f"After adding 3 to x: x = {x}")

# Double the value of y using *=
y *= 2
print(f"After multiplying y by 2: y = {y}")

# Divide the updated x by y and store the result
result = x / y
print(f"The result of x divided by y: {result}")

# ------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
print("\n--- Question 2: Comparison and Logical Operators ---")

# Let's define three variables
a = 10
b = 6
c = 8
print(f"Variables: a = {a}, b = {b}, c = {c}")

# Check if a is greater than b
condition1 = a > b
print(f"Is a > b? {condition1}")

# Check if b is an even number
condition2 = b % 2 == 0
print(f"Is b even? {condition2}")

# See if c is less than or equal to a
condition3 = c <= a
print(f"Is c <= a? {condition3}")

# Combine all the conditions using logical operators
final_condition = condition1 or (condition2 and condition3)
print(f"Final condition result: {final_condition}")

# ------------------------------------------------------------------------------------
# Question 3: Conditional Statements
print("\n--- Question 3: Conditional Statements ---")

# Ask the user to enter a test score between 0 and 100
while True:
    try:
        score = float(input("Please enter your test score (0-100): "))
        if 0 <= score <= 100:
            break
        else:
            print("Score must be between 0 and 100. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Decide the letter grade based on the score
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"With a score of {score}, your grade is: {grade}")

# ------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals
print("\n--- Question 4: Combining Operators and Conditionals ---")

# Ask the user to input two numbers
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Ask the user to choose a basic arithmetic operation
while True:
    operation = input("Enter the operation (+, -, *, /): ")
    if operation in ['+', '-', '*', '/']:
        break
    else:
        print("Invalid operation. Please choose from +, -, *, /")

# Perform the chosen calculation and handle any errors
try:
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError
        result = num1 / num2

    print(f"{num1} {operation} {num2} = {result:.2f}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
