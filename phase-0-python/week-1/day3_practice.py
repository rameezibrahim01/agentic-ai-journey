# print("•	Print all numbers from 1 to 100 using a for loop")
# 
# for i in range(1,101):
#     print(i)

# print("•	Sum of first N numbers: ask for N, print sum of 1+2+...+N. Verify: N=10 → 55, N=100 → 5050")

# n = int(input("Enter the value for N: "))

# total = 0
# for i in range(1,n+1):
#     total = total + i
# print(f"Sum of N number is {total}")

# print("•	Multiplication table: ask for a number, print its multiplication table from 1 to 12. (\"5 x 1 = 5\", \"5 x 2 = 10\"...)")

# number = int(input("Give me a number: "))

# for i in range(1, 13):
#     print(f"{number} x {i} = {number * i}")

# print("•	Guess the number game: hardcode a secret number (e.g., 42). Keep asking the user to guess until correct. Tell them \"too high\" or \"too low\". Track number of attempts.")

# secret_number = 45
# count = 0
# while True:
#     guessed_number = int(input("Guess the number: "))
#     count += 1
#     if guessed_number == secret_number:
#         print(f"That's correct! You got it in {count} tries")
#         break
#     elif guessed_number > secret_number:
#         print("too high")
#     else:
#         print("too low")

# print("	Vowel counter: ask for a word. Count and print how many vowels (a/e/i/o/u) it has. Hint: loop through each letter.")

# word = input("Enter a word: ")
# word_lower = word.lower()
# counter = 0
# for letter in word_lower:
#     if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#         counter += 1

# print(f"Total vowels in {word} = {counter}")

print("•	Average calculator: keep accepting numbers from the user until they type \"done\". Then print the average of all numbers entered.")


total = 0
count = 0
while True:
    number = input("Please enter a number or \"done\":")
    if number == "done":
        if count == 0:
            print("No numbers entered")
        else:
            print(f"Average = {total / count}")
        break
    else:
        parsed_number = int(number)
        count += 1
        total += parsed_number



