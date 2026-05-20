import truststore
truststore.inject_into_ssl()

import requests

try:
    response = requests.get("https://dog.ceo/api/breeds/image/random", timeout=5)
    response.raise_for_status()   # raises an exception if 4xx/5xx
    data = response.json()
    print(f"Random dog: {data['message']}")
except requests.Timeout:
    print("Request timed out")
except requests.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.RequestException as e:
    print(f"Request failed: {e}")


print("•	Age guesser by name: api.agify.io/?name=alex — try in your browser first. Then in Python: ask user for a name, call this API, print the guessed age.")

try:
    response = requests.get("https://api.agify.io/?name=alex", timeout = 5)
    response.raise_for_status()
    data = response.json()
    print(f"Name: {data['name']}\nAge: {data['age']}")
except requests.Timeout:
    print(f"Request timed out")
except requests.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.RequestException as e:
    print(f"Request failed: {e}")

print("•	Random user generator: randomuser.me/api/ — fetch a random user. Print their full name, email, and country.")

try:
    response = requests.get("https://randomuser.me/api/", timeout = 5)
    response.raise_for_status()
    results = response.json()['results'][0]
    full_name = results['name']['first'] + " " + results['name']['last']
    email = results['email']
    country = results['location']['country']
    print(f"Full name: {full_name}\nEmail: {email}\nCountry:{country}")
except requests.Timeout:
    print(f"Request timed out")
except requests.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
except IndexError:
    print("No results in response")

print("•	Cat facts: catfact.ninja/fact — fetch and print 3 random cat facts in a loop.")

try:
    for i in range(0, 3):
        response = requests.get("https://catfact.ninja/fact", timeout= 5)
        facts = response.json()
        print(f"{i} : {facts['fact']}")
except requests.Timeout:
    print("Request time out")
except requests.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.RequestException as e:
    print(f"Request error: {e}")


print("•	Public APIs catalog: github.com/public-apis/public-apis — browse and try one that doesn't need auth")

try:
    response = requests.get("https://api.chucknorris.io/jokes/random", timeout = 5)
    data = response.json()
    print(f"Joke: {data['value']}")
except requests.Timeout:
    print("Requests time out")

print("•	Combine: ask user for name. Call agify.io to guess age AND nationalize.io to guess nationality. Print both.")

name = input("Enter your name:")
try:
    age_response = requests.get(f"https://api.agify.io/?name={name}", timeout = 5)
    national_response = requests.get(f"https://api.nationalize.io/?name={name}", timeout = 5)
    age_data = age_response.json()
    nation_data = national_response.json()['country'][0]
    print(f"Name: {age_data['name']}\nAge: {age_data['age']}\nNation: {nation_data['country_id']}")
except requests.Timeout:
    print(f"Request timed out")
except requests.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.RequestException as e:
    print(f"Request failed: {e}")
except IndexError:
    print(f"Name: {name}")
    print(f"No country data available")
