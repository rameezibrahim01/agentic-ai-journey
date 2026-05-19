# Read file

# with open("phase-0-python/week-2/day10_practice.py", "r") as f:
#     content = f.read()
#     print(content)

# with open("phase-0-python/week-2/day10_practice.py", "r") as f:
#     for line in f:
#         print(line.strip())

# with open("phase-0-python/week-2/day10_practice.py", "r") as f:
#     lines = f.readlines()

# with open("phase-0-python/week-2/output.txt", "w") as f:
#     f.write("Hello, world!\n")
#     f.write("Line 2\n")

# with open("phase-0-python/week-2/output.txt", "a") as f:
#     f.write("New log entry\n")

# from pathlib import Path

# home = Path.home()
# notes_path = home / "Documents" / "Work" / "Research" / "AI-Engineering" / "Learning" / "Code" / "agentic-ai-journey" / "phase-0-python" / "week-2" /"output.txt"

# with open(notes_path, "r") as f:
#     content = f.read()
#     print(content)


print("•	Create a file diary.txt with 5 lines of text. Write a script that reads the file and prints each line with a line number.")

with open("phase-0-python/week-2/diary.txt", "r") as f:
    line_number = 1
    for line in f:
        print(f"{line_number} {line.strip()}")
        line_number += 1

print("•	Word counter from file: read the diary.txt and count total words (split by whitespace).")

with open("phase-0-python/week-2/diary.txt", "r") as f:
    content = f.read().split()
    print(len(content))

print("•	Most common word: read a file, find which word appears most often. (Hint: use a dict to count).")

with open("phase-0-python/week-2/diary.txt", "r") as f:
    word_list = f.read().split()
    word_counts = {}
    for word in word_list:
        count = word_counts.get(word)
        if count is None:
            word_counts[word] = 1
        else:
            word_counts[word] = count + 1
    
    max_word = None
    max_count = 0
    for key, value in word_counts.items():
        if max_count < value:
            max_count = value
            max_word = key
        
    print(f"{max_word} : {max_count}")

print('•	Append timestamps: write a script that appends a line "Logged at [current time]" to log.txt each time you run it. Use \'from datetime import datetime; datetime.now()\'.')

from datetime import datetime
with open("phase-0-python/week-2/log.txt", "a") as f:
    f.write(f"Logged at {datetime.now()}\n")

print("•	Copy a file: read diary.txt and write its contents to diary_capital.txt with all text uppercased.")

with open("phase-0-python/week-2/diary.txt", "r") as f:
    contents = f.read().upper()
    with open("phase-0-python/week-2/diary_capital.txt", "w") as f_write:
        f_write.write(contents)