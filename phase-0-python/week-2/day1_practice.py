print("•	Write function celsius_to_fahrenheit(c) that returns the Fahrenheit value. Test with 0 (=32), 100 (=212), 36.6 (≈97.88).")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(36.6))


print("•	Write function is_prime(n) that returns True/False. Test: is_prime(7)=True, is_prime(10)=False, is_prime(1)=False.")

def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
            
        return True

print(f"1: {is_prime(1)}")
print(f"2: {is_prime(2)}")
print(f"3: {is_prime(3)}")
print(f"4: {is_prime(4)}")
print(f"5: {is_prime(5)}")
print(f"6: {is_prime(6)}")
print(f"7: {is_prime(7)}")
print(f"8: {is_prime(8)}")
print(f"9: {is_prime(9)}")
print(f"10: {is_prime(10)}")
print(f"11: {is_prime(11)}")

print("•	Write function count_vowels(text) that returns the number of vowels in text.")

def count_vowels(text: str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    
    return count

print(count_vowels("Alex bradman"))

print("•	Refactor your Day 7 grade tracker: extract add_student, add_score, calculate_average, show_menu into separate functions.")

def show_menu():
    menu_options = "(1) Add student \n(2) Add score for student \n(3) View student's scores \n(4) View all averages \n(5) Quit"
    print(menu_options)

def add_student(grade_items):
    name = input("Student name: ").lower()
    scores = []
    if name in grade_items:
        scores = grade_items[name]
    grade_items[name] = scores

def add_score(grade_items):
    name = input("Student name: ").lower()
    if name in grade_items:
        score = int(input("Score: "))
        grade_items[name].append(score)
    else:
        print("Student does not exist. Please add by choosing option 1")

def calculate_average(grade_items):
    for name, scores in grade_items.items():
        total = sum(scores)
        if len(scores) == 0:
            print(f"{name} : Average = 0")
        else:
            print(f"{name} : Average = {total / len(scores)}")

grade_items = {}
while True:
    print("==== Grade Tracker ====")
    show_menu()
    choice = int(input("Choose: "))

    if choice == 5:
        print("Good Bye!")
        break;
    elif choice == 1:
        add_student(grade_items)
    elif choice == 2:
        add_score(grade_items)
    elif choice == 3:
        for name, scores in grade_items.items():
            print(f"{name} : {scores}")
    elif choice == 4:
        calculate_average(grade_items)
    else:
        print("Invalid choice! Try again")

print('•	Write a function that takes a list of numbers and returns a dict: {"min": ..., "max": ..., "sum": ..., "avg": ...}')

def analyze_numbers(numbers):
    if len(numbers) <= 0:
        return {"min": None, "max": None, "sum": 0, "avg": None}
    analyzed_dict = {}
    analyzed_dict["min"] = min(numbers)
    analyzed_dict["max"] = max(numbers)
    analyzed_dict["sum"] = sum(numbers)
    analyzed_dict["avg"] = sum(numbers) / len(numbers)
    return analyzed_dict

print(analyze_numbers([3, 1, 4, 1, 5, 9, 2, 6]))
print(analyze_numbers([]))