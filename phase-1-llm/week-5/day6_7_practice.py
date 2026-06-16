
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


print("self critique")


def generate_with_critique(task: str) -> str:
    initial = get_completion(task)
    print(initial)

    critique = get_completion(f"""Review this for accuracy and completeness.
    Task: {task}
    Response: {initial}
    List specific improvements:""")

    print(critique)

    improved = get_completion(f"""Revise based on this critique.
    Original: {initial}
    Critique: {critique}
    Improved version:""")
 
    return improved

res = generate_with_critique("Explain what an AI agent is in 2 sentences")
print(res)