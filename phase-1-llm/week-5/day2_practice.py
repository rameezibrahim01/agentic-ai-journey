from pydantic import BaseModel
from openai import OpenAI
import json


client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "qwen2.5:32b"

def clean_json(raw: str) -> str:
    raw = raw.strip()
    if "```" in raw:
        parts = raw.split("```")
        raw = parts[1] if len(parts) > 1 else raw
        if raw.startswith("json"):
            raw = raw[4:]
    return raw.strip()

def get_completion(prompt, model=MODEL):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
            model = model,
            max_tokens = 1024,
            messages = messages
        )
    return response.choices[0].message.content


class JobPosting(BaseModel):
    title: str
    skills: list[str]
    years_experience: int
    remote: bool
    salary_min: int
    salary_max: int

def extract_job_info(posting_text: str) -> JobPosting:
    # Include Pydantic schema in prompt — very reliable
    schema = JobPosting.model_json_schema()
    prompt = f"""Extract job info from this posting.
    Return ONLY valid JSON matching this schema exactly. No other text.
    Schema: {json.dumps(schema, indent=2)}
    Posting: {posting_text}"""
    
    response = client.chat.completions.create(
        model=MODEL,
        max_tokens=1024,
        temperature=0.0,    # deterministic for extraction tasks
        messages=[{"role": "user", "content": prompt}]
    )
 
    raw = response.choices[0].message.content
    raw = clean_json(raw)

    data = json.loads(raw)
    return JobPosting(**data)    


result = extract_job_info("We need a Python dev, 3+ years, $120-$150K, remote.")
print(result.title, result.skills, result.years_experience)

from typing import Optional

print("•	Build a contact extractor: given a paragraph of text, extract name, email, phone, company into a Contact Pydantic model.")

class Contact(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None

def extract_contact(text: str):

    schema = Contact.model_json_schema()

    prompt = f"""extract text, extract name, email, phone, company 
    Return ONLY valid JSON matching this schema exactly. No other text.
    Schema: {json.dumps(schema, indent=2)}
    content: {text}
    """

    result = get_completion(prompt)
    raw = clean_json(result)
    raw_json = json.loads(raw)
    model = Contact(**raw_json)
    return model

# print(f"{extract_contact(text = 'Contact our sales rep Mike Chen at mike.chen@globalsales.com. He\'s based at Global Sales Ltd and his direct line is 044-789-0123.')}")

# print(f"{extract_contact(text = 'No contact info here. Just a regular sentence about nothing important.')}")

print("•	Build a news headline analyzer: given a headline, return {topic, sentiment, entities: list[str], clickbait_score: int 1-10}.")

from pydantic import Field

class News(BaseModel):
    topic: Optional[str] = None
    sentiment: Optional[str] = None
    entities: list[str] = []
    clickbait_score: int = Field(default = 1, ge=1, le=10)

def analyze_headline(text: str):
    schema = News.model_json_schema()
    prompt = f"""Extract topic, sentiment, entities, clickbait_score 
    Return only Json object without any other text, matching exactly the given model schema.
    Schema: {schema} 
    text: {text}
    """

    result = get_completion(prompt)
    raw = clean_json(result)
    raw_json = json.loads(raw)
    model = News(**raw_json)
    return model

answer = analyze_headline("Scientists discover potential cure for Alzheimer's disease")
print(answer)


print("•	Build a code analyzer: given Python code, return -> functions: list[str], imports: list[str], has_error_handling: bool, complexity: str}.")

class Code(BaseModel):
    functions: list[str] = []
    imports: list[str] = []
    has_error_handling: bool
    complexity: str

def python_code_analyzer(code_text: str):
    schema = Code.model_json_schema()
    prompt = f"""Extract functions, imports, has_error_handling, complexity 
    Return only Json object without any other text, matching exactly the given model schema.
    Schema: {schema} 
    text: {code_text}
    """

    result = get_completion(prompt)
    raw = clean_json(result)
    raw_json = json.loads(raw)
    model = Code(**raw_json)
    return model


result = python_code_analyzer("""
import asyncio
import httpx
from pydantic import BaseModel
from typing import Optional

class WeatherResponse(BaseModel):
    temp: float
    city: str

async def fetch_weather(city: str) -> Optional[WeatherResponse]:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"https://api.weather.com//{/city}")
            return WeatherResponse(**response.json())
        except Exception as e:
            return None

async def main():
    result = await fetch_weather("Dubai")
    print(result)
""")


print(result)