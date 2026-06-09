from openai import OpenAI

MODEL = "qwen2.5:32b"
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")


def get_completion(prompt, model=MODEL):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
            model = model,
            max_tokens = 1024,
            messages = messages
        )
    return response.choices[0].message.content

# prompt = "Classify this review as positive, neutral, or negative: 'The product is okay, nothing special.'"

# prompt = """Classify reviews as positive, neutral, or negative.
 
# Review: "Amazing quality, will buy again!" -> positive
# Review: "It works, but nothing special." -> neutral
# Review: "Complete waste of money." -> negative
 
# Review: "Decent product for the price." ->"""

# prompt = """Solve this step by step:
 
# A store has 120 apples. On Monday, 35% were sold.
# On Tuesday, 40% of the remaining were sold.
# How many remain?
 
# Think step by step:"""


# prompt = """Extract information from this job posting.
# Return ONLY valid JSON. No markdown, no explanation.
 
# Job posting: "Senior Python Engineer. 5+ years required.
# Django and FastAPI. Remote OK. $150K-$200K."
 
# Return exactly:
# {
#   "title": "...",
#   "skills": [...],
#   "years_experience": 0,
#   "remote": true,
#   "salary_min": 0,
#   "salary_max": 0
# }"""

# response = get_completion(prompt)
# print(response)


test_cases = [
    {"input": "This is the best product I have ever bought", "expected": "positive"},
    {"input": "It stopped working after one week", "expected": "negative"},
    {"input": "Does exactly what it says on the box.", "expected": "neutral"},
    {"input": "Absolutely terrible, would not recommend to anyone.", "expected": "negative"},
    {"input": "Pretty good for the price", "expected": "positive"},
    {"input": "Nothing special, just average", "expected": "neutral"},
    {"input": "I am obsessed with this, use it every single day", "expected": "positive"},
    {"input": "Arrived damaged and customer service was unhelpful", "expected": "negative"},
    {"input": "It works but I expected more for this price", "expected": "neutral"},
    {"input": "Decent enough, gets the job done", "expected": "neutral"}
]

def classify(text, examples):

    prompt = "Classify this review as positive, neutral, or negative:"

    for examples_dict in examples:
        prompt += f"\n{examples_dict["input"]} -> {examples_dict["expected"]}"

    prompt += f"\n\nNow classify this: {text}"
    response = get_completion(prompt)
    return response

def check_output_classify():
    for approach_name, examples in [("zero-shot", []), ("3-shot", test_cases[:3]), ("5-shot", test_cases[:5])]:
        correct = 0
        for case in test_cases:
            response = classify(case["input"], examples)
            if case["expected"] in response.lower():
                correct += 1
        print(f"{approach_name}: {correct}/10 = {correct*10}%")




print("•	Build a structured extractor: given text, extract entities (person, company, date, amount) as JSON. Validate result with Pydantic.")

from pydantic import BaseModel
from typing import Optional
import json

class Entities(BaseModel):
    person: Optional[str] = None
    company: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[str] = None


def extract_entities(text: str):
    prompt =  f"Return ONLY valid JSON. No explanation, no markdown! Extract json object of entities with keys person, company, date, amount from the content inside triple quote '''{text}''' "
    result = get_completion(prompt)
    entity_json = json.loads(result)
    model = Entities(**entity_json)
    return model

model1 = extract_entities("John Smith from Apple signed a $5M deal on January 15th")
model2 = extract_entities("Sarah Connor joined Microsoft on March 3rd")
print(model1)
print(model2)


print("•	Test chain-of-thought: same math problem with and without 'think step by step'. Compare on 5 problems.")


def solve(problem: str, use_cot: bool = False):
    prompt = f"{problem}"

    if use_cot:
        prompt += "\nThink step by step before answering"

    result = get_completion(prompt)
    return result

print(f"Without COT: {solve(problem = 'A store has 120 apples. 35% were sold on Monday. On Tuesday store sold 24% of remaining apples.  How many remain?')}")
print(f"\n\nWith COT: {solve(problem = 'A store has 120 apples. 35% were sold on Monday. On Tuesday store sold 24% of remaining apples.  How many remain?', use_cot = True)}")