print("•	Create a dict representing a book (title, author, year, genres list, available True/False). Save to book.json with indent=2. Open the file in VS Code and verify it looks like JSON.")

import json
book = {"title": "One man show", "author":"Alex", "year": 1999, "genre_list": ["genre-1", "genre-2"], "available": True}

with open("phase-0-python/week-2/output-files/book.json", "w") as f:
    json.dump(book, f,indent = 2)

print("•	Read book.json back into Python. Change the year. Save it back.")
with open("phase-0-python/week-2/output-files/book.json", "r") as f:
    book_json = json.load(f)
    book_json["year"] = 2020
with open("phase-0-python/week-2/output-files/book.json", "w") as f:
    json.dump(book_json, f,indent = 2)

print("•	Create a books library: a list of 5 book dicts. Save as library.json. Then read it back and print just the titles.")
books_lib = {"books":
                [
                  {"title": "One man show", "author":"Alex", "year": 1999, "genre_list": ["genre-1", "genre-2"], "available": True},
                  {"title": "random book", "author":"john", "year": 2020, "genre_list": ["genre-1", "genre-2"], "available": False},
                  {"title": "python", "author":"james", "year": 1998, "genre_list": ["genre-1", "genre-2"], "available": True},
                  {"title": "swift", "author":"kelly", "year": 2012, "genre_list": ["genre-1", "genre-2"], "available": False},
                  {"title": "java", "author":"brad", "year": 2016, "genre_list": ["genre-1", "genre-2"], "available": True},
                ]
            }

with open("phase-0-python/week-2/output-files/library.json", "w") as f:
    json.dump(books_lib, f, indent = 2)
with open("phase-0-python/week-2/output-files/library.json", "r") as f_read:
    books_content = json.load(f_read)["books"]
    for content in books_content:
        print(content["title"])


print("•	Filter and save: read library.json, keep only books with year > 2000, save filtered list as recent_books.json.")

with open("phase-0-python/week-2/output-files/library.json", "r") as f:
    books_library = json.load(f)["books"]
    filtered_books = []
    for book in books_library:
        year = int(book["year"])
        if year > 2000:
            filtered_books.append(book)

with open("phase-0-python/week-2/output-files/library.json", "w") as f:
    json.dump({"books": filtered_books}, f, indent = 2)