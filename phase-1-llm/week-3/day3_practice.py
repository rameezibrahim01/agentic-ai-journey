squares = [x**2 for x in range(10)]
print(squares)

evens = [x for x in range(20) if x % 2 == 0]
print(evens)

odds = [x for x in range(20) if x % 2 != 0]
print(odds)

user_inputs = ["Hello", "What is Python?", "Explain async"]
messages = [{"role": "user", "content": msg} for msg in user_inputs]
print(messages)


word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
print(word_lengths)



import json

print("•	From Phase 0 library.json, create a list of titles using list comprehension.")

with open("phase-0-python/week-2/output-files/library.json", "r") as f_read:
    books_content = json.load(f_read)["books"]
    titles = [book["title"] for book in books_content]
    print(titles)


print("•	Create a dict mapping each word in a sentence to its length using dict comprehension.")

mapped_dict = {word : len(word) for word in "This is a sentence".split()}
print(mapped_dict)


print("•	Filter your Phase 0 task_list to only 'pending' tasks using list comprehension")

with open("phase-0-python/week-2/output-files/tasks.json", "r") as f:
    tasks = json.load(f)
    pending_tasks = [task["title"] for task in tasks if task["status"] == "pending"]
    print(pending_tasks)