print("FizzBuzz starter: ask for a number. If divisible by 3, print \"Fizz\". If by 5, print \"Buzz\". If both, print \"FizzBuzz\". Otherwise print the number.")

number = int(input("Enter a number: "))


if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)


print("Grade calculator: ask for score (0-100), print grade: A (90+), B (80-89), C (70-79), D (60-69), F (<60).")

grade = int(input("Please enter score (0-100)"))

if grade > 90:
    print("A")
elif grade >= 80 and grade < 90:
    print("B")
elif grade >= 70 and grade < 80:
    print("B")
elif grade >= 60 and grade < 70:
    print("D")
else:
    print("F")

print("Login simulator: ask for username and password. Hardcode them. If both match, print \"Access granted\". Otherwise show which field was wrong.")

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "admin123":
    print("Access granted")
elif username != "admin" and password != "admin123":
    print("Both username and password are wrong")
elif username != "admin":
    print("invalid username")
elif password != "admin123":
    print("invalid password")

print("Leap year checker: ask for a year. A leap year is divisible by 4 BUT not 100, UNLESS also divisible by 400. (Hint: use 'and', 'or', 'not')")

year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print("Not a leap year")

print("BMI classifier: ask for weight (kg) and height (m). Calculate BMI = weight / (height ** 2). Print: underweight (<18.5), normal (18.5-24.9), overweight (25-29.9), or obese (30+).")

weight = float(input("Enter your weight(kg): "))
height = float(input("enter your height(m): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("under weight")
elif bmi >= 18.5 and bmi < 25:
    print("normal")
elif bmi >= 25 and bmi < 30:
    print("overweight")
else:
    print("obese")