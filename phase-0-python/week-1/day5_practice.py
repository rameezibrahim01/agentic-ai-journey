# print("Phone book: create a dict mapping names to phone numbers. Add 3 entries. Ask user for a name and print the phone number (or \"Not found\").")

# phone_book = {"john": 509998822, "james": 509998823, "kelly": 509998824}

# name = input("Please enter a name: ")
# phone = phone_book.get(name)
# if phone is None:
#     print("Not found")
# else:
#     print(f"{phone}")


# print("Word counter: given a sentence, count how many times each word appears. Use a dict. Input \"the cat and the dog\" → {\"the\": 2, \"cat\": 1, \"and\": 1, \"dog\": 1}")

# sentence = "the cat the"
# word_counter = {}
# for word in sentence.split():
#     if word in word_counter:
#         word_counter[word] += 1
#     else:
#         word_counter[word] = 1
# print(word_counter)

# print("Student grade book: dict where key=student name, value=list of test scores. Add 3 students each with 3 scores. Print each student's average.")

# grade_book = {"john": {"Maths": 40, "Science": 60, "English": 80},
#               "james": {"Maths": 34, "Science": 99, "English": 80},
#               "kelly": {"Maths": 77, "Science": 33, "English": 44}}

# for student, subjects in grade_book.items():
#     average = sum(subjects.values()) / len(subjects)
#     print(f"{student} : {average}")


# print("Remove duplicates from a list using set(). Then convert back to a list.")

# numbers = [1, 2, 2, 3, 3, 3, 4]
# unique = list(set(numbers))
# print(unique)

print("Inventory manager (advanced): dict where key=item name, value=quantity. In a loop, allow: add(item, qty), remove(item, qty), show inventory, quit.")

items_dict = {}
options = "1.add 2.remove 3.show inventory 4.quit"

while True:
    print(options)
    selected = int(input("Enter your choice: "))
    if selected == 4:
        break
    elif selected == 1:
        item_name = input("Enter the item name:")
        item_price = input("Enter the item price:")
        items_dict[item_name] = item_price
    elif selected == 2:
        item_name = input("Enter the item name to remove: ")
        if item_name in items_dict:
            items_dict.pop(item_name)
        else:
            print("Item not found")
    elif selected == 3:
        print("List:")
        print(items_dict)
    else:
        print("Invalid choice")

