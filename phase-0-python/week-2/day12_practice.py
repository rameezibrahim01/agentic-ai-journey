# print("•	Safe int input: write a function safe_int_input(prompt) that keeps asking until user enters a valid integer.")

# def safe_int_input(prompt):
#     try:
#         value = int(input(f"{prompt}: "))
#         print(f"You have entered: {value}")
#     except ValueError:
#         print("Not an integer")
#         safe_int_input(prompt)

# safe_int_input("Your age?")

# print("•	Safe file reader: write read_json_safe(filename) that returns the dict, or an empty dict if file doesn't exist OR is invalid JSON.")

# import json

# def read_json_safe(filename):
#     try:
#         with open(filename, "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return {}
#     except json.JSONDecodeError:
#         return {}
    
# print(read_json_safe("random.py"))
# print(read_json_safe("phase-0-python/week-2/output-files/grades.json"))

print("•	Calculator with error handling: prompt for two numbers and an operator (+, -, *, /). Handle ValueError (bad number) and ZeroDivisionError.")

def calculate(first_number: int, operator, second_number: int):
        if operator == "+":
            return first_number + second_number
        elif operator == "-":
            return first_number - second_number
        elif operator == "*":
            return first_number * second_number
        elif operator == "/":
            return first_number / second_number
        else:
            return None

def begin_calculation():
    try:
        first_number = int(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator")
            begin_calculation()
        else:
            second_number = int(input("Enter second number: "))
            res = calculate(first_number, operator, second_number)
            print(f"Result: {res}")
    except ValueError:
        print("Error: Invalid number")
        begin_calculation()
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        begin_calculation()

begin_calculation()