from openai import OpenAI

client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "ollama"
)


for temp in [0.0, 0.0, 0.0, 1.0, 1.0, 1.0]:
    response = client.chat.completions.create(
        model = "qwen2.5:32b",
        messages = [{"role": "user", "content": "Write a one-sentence tagline for a Python learning app."}]
    )
    print(f"temp={temp}: {response.choices[0].message.content}")