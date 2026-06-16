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
    {"input": "Decent enough, gets the job done", "expected": "neutral"},
    {"input": "Not bad I suppose", "expected": "neutral"},
    {"input": "I mean it's fine I guess", "expected": "neutral"},
    {"input": "Could be worse", "expected": "neutral"},
    {"input": "It's not terrible", "expected": "neutral"},  # double negative
    {"input": "Unexpectedly decent", "expected": "positive"}
]

def evaluate(prompt_fn, test_cases):
    valid_result = 0
    failures = []
    
    for test_case in test_cases:
        result = prompt_fn(test_case["input"], examples=[])
        if test_case["expected"].lower() in result.lower():
            valid_result += 1
        else:
            failures.append({
                "input": test_case["input"],
                "expected": test_case["expected"],
                "got": result
            })
    
    print(f"Result: {valid_result}/{len(test_cases)} = {valid_result/len(test_cases) * 100}%")
    
    if failures:
        print("\nFailed cases:")
        for f in failures:
            print(f"  Input: {f['input']}")
            print(f"  Expected: {f['expected']}, Got: {f['got']}\n")
    else:
        print("No failures!")

def classify(text, examples):

    prompt = "Classify this review as positive, neutral, or negative:"

    for examples_dict in examples:
        prompt += f"\n{examples_dict["input"]} -> {examples_dict["expected"]}"

    prompt += f"\n You should always return only one word positive, neutral, or negative, no other explanation!"

    prompt += f"\n\nNow classify this: {text}"
    response = get_completion(prompt)
    return response

# evaluate(classify, test_cases)



print("Email draft judgement")

from dataclasses import dataclass
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "qwen2.5:32b"

@dataclass
class PromptTemplate():
    system: str
    user_template: str

    def build_messages(self, **kwargs) -> list[dict]:
        return [
            {"role":"system","content": self.system},
            {"role":"user","content": self.user_template.format(**kwargs)}
        ]
    
EMAIL_DRAFTER = PromptTemplate(system = "You are a email drafter, draft email as per the request!",
                               user_template = "Draft email with {tone}, and purpose should be {purpose}, mention all the {key_points} for the recipient {recipient_name}"
)

def email_draft_generate(tone: str, purpose:str, key_points: list[str], recipient_name: str):
    messages = EMAIL_DRAFTER.build_messages(tone = tone, purpose = purpose, key_points = key_points, recipient_name = recipient_name)

    response = client.chat.completions.create(
            model = MODEL,
            max_tokens = 1024,
            messages = messages
        )
    return response.choices[0].message.content



def clean_json(raw: str) -> str:
    raw = raw.strip()
    if "```" in raw:
        parts = raw.split("```")
        raw = parts[1] if len(parts) > 1 else raw
        if raw.startswith("json"):
            raw = raw[4:]
    return raw.strip()

def judge_response(email_content: str) -> str:
    prompt = f"""
    Rate this email on:
    - Tone appropriateness (1-10)
    - Clarity (1-10)  
    - Completeness (1-10)"

    Return ONLY JSON with: "tone": 0, "clarity": 0, "completeness": 0, "reason": ""
    """

    prompt += f"\n{email_content}"

    res = get_completion(prompt, model= MODEL)
    res = clean_json(res)
    return res

result = email_draft_generate(tone = "formal", purpose = "Poc development", key_points = ["native app", "support web", "works on any screen"], recipient_name = "rameez ahmed")
print(result)

judgement = judge_response(result)
print(f"\n\nJudgement: {judgement}")