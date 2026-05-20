from pydantic import BaseModel


# class Address(BaseModel):
#     city: str
#     country: str

# class User(BaseModel):
#     name: str
#     age: int
#     address: Address


# data = {
#     "name": "Alex",
#     "age": 28,
#     "address": {"city": "Dubai", "country": "UAE"}
# }


# user = User(**data)
# print(user.address.city)


# Load JSON, validate with Pydantic
import json
from pydantic import BaseModel
 
class Book(BaseModel):
    title: str
    author: str
    year: int
 
with open("phase-0-python/week-2/output-files/book.json") as f:
    raw = json.load(f)
 
book = Book(**raw)    # validates AND gives you typed access
print(book.title)

print("•	Set up .env with TEST_KEY=hello. Write a script that loads and prints it. Verify .env is in .gitignore by running 'git status' — .env should NOT appear.")

import os
from dotenv import load_dotenv

load_dotenv()

test_key = os.getenv("TEST_KEY")
print(test_key)

print("•	Define a Pydantic model Product with: name (str), price (float), in_stock (bool), tags (list of str). Create 3 product instances and print them.")

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool
    tags: list[str]

prod1 = Product(name = "android-mobile", price = 1000, in_stock = False, tags =["samsung", "android"])
prod2 = Product(name = "iphone", price =2000, in_stock =False, tags =["Apple", "17 pro max"])
prod3 = Product(name = "macbook", price =4000, in_stock =True, tags =["Apple", "mac os"])

print(f"{prod1}\n{prod2}\n{prod3}")


print("•	Define a Pydantic model Movie with: title, year (int), director, genres (list of str). Try creating one with bad data (year as string \"abc\") — catch the ValidationError.")

from pydantic import ValidationError
class Movie(BaseModel):
    title: str
    year: int
    director: str
    genres: list[str]


try:
    movie1 = Movie(title = "one man show", year= "abc", director = "major", genres = ["sample1", "sample2"])
except ValidationError as e:
    print(f"Error: {e}")


print("•	Read library.json (from Day 11). Define a Book Pydantic model. Loop through and create a Book instance for each. Print only books where year > 2000 using a typed comparison")
import json

class Book(BaseModel):
    title: str
    author: str
    year: int
    genre_list: list[str]
    available: bool

with open("phase-0-python/week-2/output-files/library.json", "r") as f:
    books_json = json.load(f)["books"]
    
    books = []
    for book_data in books_json:
        books.append(Book(**book_data))
    
    for book in books:
        if book.year > 2000:
            print(book)
