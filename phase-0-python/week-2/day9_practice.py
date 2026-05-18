print("•	Write a function multiply_all(*nums) that returns the product of all numbers passed. (Edge case: no arguments should return 1.)")

def multiply_all(*nums):
    product = 1
    for num in nums:
        product *= num
    return product

print(multiply_all())
print(multiply_all(5))
print(multiply_all(2,3))
print(multiply_all(2,3,4))
print(multiply_all(0,5,10))
print(multiply_all(-2,3))
print(multiply_all(-2,-3))

print('•	Write make_user(name, **extra) that returns a dict with name and any extra fields. Example: make_user("Alex", age=28, city="Dubai")')


def make_user(name, **extra):
    dic = {"name" : name}
    dic.update(extra)
    return dic

print(make_user("Alex", age=28, city="Dubai"))

print('•	Write describe(*items) that prints "Item 1: ...", "Item 2: ..." for each item.')

def describe(*items):
    for i in range(0,len(items)):
        print(f"Item {i+1}: {items[i]}")

describe("apple", "banana", "cherry")