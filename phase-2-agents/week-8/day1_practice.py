from agents import Agent, Runner, function_tool, set_default_openai_client
from openai import AsyncOpenAI
import os

MODEL = "qwen2.5:32b"

ollama_client = AsyncOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

# Tell the SDK to use this client
set_default_openai_client(ollama_client)

@function_tool
def web_search(query: str) -> str:
    """Search the web for information about a topic."""
    print(f"🔧 web_search called: {query}") 
    mock_data = {
        "dubai population": "Dubai population is 3.5 million",
        "india population": "India population is 1.4 billion",
        "tesla stock": "Tesla stock price is $250",
        "apple stock": "Apple stock price is $190",
    }
    for key in mock_data:
        if key in query.lower():
            return mock_data[key]
    return "No data found for that query"
 

@function_tool
def calculator(num1: float, num2: float, operator: str) -> str:
    """Perform basic math: +, -, *, /"""
    if operator == "+": return str(num1 + num2)
    elif operator == "-": return str(num1 - num2)
    elif operator == "*": return str(num1 * num2)
    elif operator == "/" and num2 != 0: return str(num1 / num2)
    return "Error: invalid operation"
 
@function_tool
def save_to_file(filename: str, content: str) -> str:

    try:
        os.makedirs("phase-2-agents/week-7/output-files", exist_ok=True)
        with open(f"phase-2-agents/week-7/output-files/{filename}", "w") as f:
            f.write(content)
        return f"saved to {filename}"
    except Exception as e:
        print(f"save_to_file error: {e}")
        return "failed"

@function_tool
def read_file(filename: str) -> str:
    try:
        with open(f"phase-2-agents/week-7/output-files/{filename}", "r") as f:
            return f.read()
    except:
        return "failed"

# Create agent
research_agent = Agent(
    name="Research Assistant",
    instructions="You are a helpful research assistant. Use tools to find information and answer questions accurately.",
    tools=[web_search, calculator, save_to_file, read_file],
    model=MODEL
)
 
# Run the agent
result = Runner.run_sync(research_agent, "Step 1: Search Dubai population using web_search. Step 2: Save the result to dubai.txt using save_to_file. Step 3: Read dubai.txt using read_file and print the exact content you read.")
print(result.final_output)