print("•	Build a PromptTemplate for code review: parameters are language, code, focus_area (security/performance/style).")


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
    

CODE_REVIEWER = PromptTemplate(system = "You are an experienced code reviwer. reviews should be in less than 5 bullet points",
                               user_template = "Review this in language {language}, focus on {focus_area}, \n\ncode: {code}")


def code_review(language: str, focus_area:str, code: str):
    messages = CODE_REVIEWER.build_messages(language = language, focus_area = focus_area, code = code)

    response = client.chat.completions.create(
            model = MODEL,
            max_tokens = 1024,
            messages = messages
        )
    return response.choices[0].message.content


result = code_review(language = "python", focus_area = "security", code = """
def say_hi(): 
    return "hi"
""")
print(result)


print("•	Build a PromptTemplate for email drafting: tone (formal/casual), purpose, key_points (list), recipient_name.")

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

result = email_draft_generate(tone = "formal", purpose = "Poc development", key_points = ["native app", "support web", "works on any screen"], recipient_name = "rameez ahmed")
print(result)