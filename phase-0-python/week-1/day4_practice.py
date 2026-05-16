print("•	Create a list of 5 movies you like. Print each on a separate line with its index.")

movies = ["Inception", "The Matrix", "Interstellar", "Parasite", "Dune"]
for index, movie in enumerate(movies):
    print(f"{index} : {movie}")


print("Ask the user for 5 numbers (one at a time, in a loop). Store them in a list. Print: min, max, sum, average.")

numbers_list = []
for i in range(0,5):
    number = int(input("Enter a number: "))
    numbers_list.append(number)
print(f"min: {min(numbers_list)}")
print(f"max: {max(numbers_list)}")
print(f"sum: {sum(numbers_list)}")
print(f"average: {sum(numbers_list) / len(numbers_list)}")

print("Reverse a list without using reverse() or [::-1]. Loop through it backwards.")

numbers = [10, 20, 30, 40, 50]
reversed_numbers = []
for i in range(len(numbers)-1, -1, -1):
    reversed_numbers.append(numbers[i])
print(f"{reversed_numbers}")

print("Take a sentence from user input. Split into words. Print only words longer than 4 letters.")

sentance = input("Enter a sentance: ")
words = sentance.split()

for word in words:
    if len(word) > 4:
        print(word)

print("Shopping list manager: in a loop, ask user to (1) Add item, (2) Remove item, (3) Show list, (4) Quit. Use a list to track items.")

operations = ["1 - Add item", "2 - Remove item", "3 - Show list", "4 - Quit"]
shopping_list = []
while True:
    for operation in operations:
        print(operation)

    choice = int(input("Please enter your choice: "))
    if choice == 4:
        break
    elif choice == 1:
        item = input("Please enter item to add: ")
        shopping_list.append(item)
    elif choice == 2:
        item = input("Please enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"{item} is not in your list")
    elif choice == 3:
        print(shopping_list)
    else:
        print("Invalid input")


print("Find duplicates: given a list like [1, 2, 3, 2, 4, 5, 1], print which numbers appear more than once.")

numbers = [1, 2, 3, 2, 4, 5, 1]
seen = []
duplicates =[]
for number in numbers:
    if number not in seen:
        seen.append(number)
    elif number not in duplicates:
        duplicates.append(number)

print(duplicates)