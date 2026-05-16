print('Palindrome checker: ask for a word. Print whether it reads the same backwards ("racecar" yes, "hello" no). Hint: word == word[::-1]')

word = input("Please enter a word: ")

if word.lower() == word[::-1].lower():
    print("Palindrome")
else:
    print("Not a palindrome")

print('Email validator (simple): ask for an email. Check it contains "@" and ".". Print "valid" or "invalid". This isn\'t real validation, just practice.')

email = input("Please enter your email: ")
if '@' in email and '.' in email and not email.endswith("."):
    print("valid")
else:
    print("invalid")

print('Title case converter: take a sentence, capitalize the first letter of each word. "hello world" → "Hello World". Hint: split, capitalize each, join.')

sentence = input("Enter a sentence: ")

words = sentence.split()

titlecased_words = []
for word in words:
    titlecased_words.append(word.capitalize())
final = " ".join(titlecased_words)
print(final)

print('Pig Latin (silly): take a word. Move first letter to end and add "ay". "python" → "ythonpay".')

word = input("Please enter a word: ")
if len(word) > 1:
    print(word[1:] + word[0]  + "ay")
else:
    print("word has less than 2 characters")

print("Password strength checker: ask for a password. Print whether it's strong: ≥8 chars AND contains both letters and digits. Hint: use any(c.isdigit() for c in password) — we'll learn 'any' more later, but try it.")

password = input("Enter a password: ")

if len(password) >= 8:
    has_digit = False
    has_alphabet = False
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_alphabet = True
        
    if has_digit and has_alphabet:
        print("Strong password!")
    else:
        print("Weak password")
else:
    print("Weak password")

print('Generate a username: ask for first name and last name. Create a username like "alex.smith" (lowercase, dot separator).')
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

username = first_name.lower() + "." + last_name.lower()
print(username)
