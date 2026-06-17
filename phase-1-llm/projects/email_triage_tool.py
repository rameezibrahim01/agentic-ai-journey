from pydantic import BaseModel, Field
from typing import Optional
import json
from openai import OpenAI
import asyncio
from openai import AsyncOpenAI
from datetime import datetime

MODEL = "qwen2.5:32b"

def clean_json(raw: str) -> str:
    raw = raw.strip()
    if "```" in raw:
        parts = raw.split("```")
        raw = parts[1] if len(parts) > 1 else raw
        if raw.startswith("json"):
            raw = raw[4:]
    return raw.strip()

class Email(BaseModel):
    id: int
    from_email: str
    subject: str
    body: str
    received_at: str

class EmailEntities(BaseModel):
    sender_name: Optional[str] = None
    company: Optional[str] = None
    deadline: Optional[str] = None
    request_type: Optional[str] = None
    urgency_signals: list[str] = []

class EmailAnalysis(BaseModel):
    email_id: int
    classification: str = Field(pattern="^(urgent|normal|spam)$")
    confidence: int = Field(ge=1, le=10)
    reason: str
    entities: EmailEntities
    suggested_reply: Optional[str] = None

class TriageReport(BaseModel):
    total_emails: int
    urgent_count: int
    normal_count: int
    spam_count: int
    processed_at: str
    analysis: list[EmailAnalysis]


def load_email() -> list[Email]:
    email_list = []
    with open("phase-1-llm/projects/emails.json", "r") as f:
        emails = json.load(f)

        for email in emails:
            email_list.append(Email(**email))
    
    return email_list


async_client = AsyncOpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

async def analyze_email_async(email: Email) -> EmailAnalysis:
    prompt = f"""
    Analyze the email in the quote and identify if the email is urgent , normal or spam! 
    The output should return ONLY JSON representing EmailAnalysis schema.
    If classification is urgent, draft a professional suggested_reply.
    If normal or spam, set suggested_reply to null.
    email: {email}
    schema: {EmailAnalysis.model_json_schema()}
    """

    response = await async_client.chat.completions.create(
    model=MODEL,
    max_tokens=1024,
    temperature=0.0,
    messages=[{"role": "user", "content": prompt}]
    )
    res = response.choices[0].message.content

    dict_data = clean_json(res)
    data = json.loads(dict_data)
    data["email_id"] = email.id
    result = EmailAnalysis(**data)
    return result

async def process_all_emails() -> list[EmailAnalysis]:
    all_emails = load_email()
    email_analysis = await asyncio.gather(*[analyze_email_async(email) for email in all_emails])
    return email_analysis
        
        

def generate_report(email_analysis_list: list[EmailAnalysis]) -> TriageReport:
    urgent = [a for a in email_analysis_list if a.classification == "urgent"]
    normal = [a for a in email_analysis_list if a.classification == "normal"]
    spam = [a for a in email_analysis_list if a.classification == "spam"]
    
    return TriageReport(
        total_emails=len(email_analysis_list),
        urgent_count=len(urgent),
        normal_count=len(normal),
        spam_count=len(spam),
        processed_at=str(datetime.now()),
        analysis=email_analysis_list
    )

processed_emails = asyncio.run(process_all_emails())
report = generate_report(processed_emails)
print(report)


def save_report(report: TriageReport):
    with open("phase-1-llm/projects/triage_results.json", "w") as f:
        json.dump(report.model_dump(mode="json"), f, indent = 2)

def save_urgent_replies(report: TriageReport):
    urgent_replies = []
    for email_analysis in report.analysis:
        if email_analysis.classification == "urgent" and email_analysis.suggested_reply:
            urgent_replies.append(email_analysis.suggested_reply)

    with open("phase-1-llm/projects/urgent_replies.txt", "w") as f:
        for reply in urgent_replies:
            f.write(reply + "\n\n")


save_report(report)
save_urgent_replies(report)