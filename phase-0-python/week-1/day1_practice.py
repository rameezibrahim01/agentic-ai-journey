print("Create variables for your name, age, favorite city, and whether you like coffee (True/False). Print each.")

name = "Rameez"
age = 70
favorite_city = "New York"
like_coffee = True

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"Do I like coffee? {like_coffee}")
print(f"My favorite city is {favorite_city}.")

print("Ask the user for two numbers, add them, print the result. (Hint: convert input to int)")

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

result = int(first_number) + int(second_number)
print(f"The sum of {first_number} and {second_number} is: {result}")

print("Ask the user for their first and last name separately. Print: \"Hello, [first] [last]! Your name has [N] characters total.\"")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello, {first_name} {last_name}! Your name has {len(first_name) + len(last_name)} characters totally.")
print("Calculate: if you save $250/month, how much do you save in 5 years? Print result.")

monthly_income = 250
print(f"Total income for 5 years: {monthly_income * 12 * 5} $")

print("Ask user for their birth year. Calculate and print their age (assume current year is 2026).")
birth_year = input("Enter your birth year: ")
current_year = 2026
age = current_year - int(birth_year)
print(f"You are {age} years old.")
