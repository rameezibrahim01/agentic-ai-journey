print("•	Upgrade your Grade Tracker: when loading grades.json, handle the case where it doesn't exist (first run) by starting with an empty dict.")


import json

menu_options = "(1) Add student \n(2) Add score for student \n(3) View student's scores \n(4) View all averages \n(5) Quit"

try:
    with open("phase-0-python/week-2/output-files/grades.json", "r") as f:
        grade_items = json.load(f)
except FileNotFoundError:
    grade_items = {}

while True:
    print("==== Grade Tracker ====")
    print(menu_options)
    choice = int(input("Choose: "))

    if choice == 5:
        with open("phase-0-python/week-2/output-files/grades.json", "w") as f:
            json.dump(grade_items, f, indent = 2)
        print("Good Bye!")
        break;
    elif choice == 1:
        name = input("Student name: ").lower()
        scores = []
        if name in grade_items:
            scores = grade_items[name]
        grade_items[name] = scores
    elif choice == 2:
        name = input("Student name: ").lower()
        if name in grade_items:
            score = int(input("Score: "))
            grade_items[name].append(score)
        else:
            print("Student does not exist. Please add by choosing option 1")
    elif choice == 3:
        for name, scores in grade_items.items():
            print(f"{name} : {scores}")
    elif choice == 4:
        for name, scores in grade_items.items():
            total = sum(scores)
            if len(scores) == 0:
                print(f"{name} : Average = 0")
            else:
                print(f"{name} : Average = {total / len(scores)}")
    else:
        print("Invalid choice! Try again")