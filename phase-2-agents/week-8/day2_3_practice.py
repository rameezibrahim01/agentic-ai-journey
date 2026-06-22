from agents import Agent, Runner, function_tool, handoff, set_default_openai_client, set_tracing_disabled
from openai import AsyncOpenAI
import os

MODEL = "qwen2.5:32b"
set_tracing_disabled(True)

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
    "dubai": "Dubai population is 3.5 million",
    "india": "India population is 1.4 billion",
    "tesla": "Tesla stock price is $250",
    "apple": "Apple stock price is $190",
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



writer_agent = Agent(
    name="Writer",
    instructions="You format results into clear reports and save them to files.",
    tools=[save_to_file],
    model=MODEL
)

math_agent = Agent(
    name="Mathematician",
    instructions="You perform calculations. Show your work. When done, you MUST hand off to Writer to save the results. Always hand off — never answer directly.",
    tools=[calculator],
    handoffs=[writer_agent],
    model=MODEL
)

research_agent = Agent(
    name = "Researcher",
    instructions="You find information using web search. Be concise and factual. Print 'HANDOFF TO RESEARCHER' when you start.",
    tools = [web_search],
    handoffs=[math_agent],
    model = MODEL
)


triage_agent = Agent(
    name="Triage",
    instructions="""You are an orchestrator. You must handoff to ONE specialist at a time.

Step 1: Handoff to Researcher ONLY to get the populations.
Wait for the result, then Step 2: Handoff to Mathematician ONLY to calculate.
Wait for the result, then Step 3: Handoff to Writer ONLY to save.

IMPORTANT: Only one handoff per response. Never handoff to multiple agents at once.""",
    handoffs=[research_agent, math_agent, writer_agent],
    model=MODEL
)

# result = Runner.run_sync(triage_agent, "Find Dubai and India populations, calculate the ratio, save to population_report.txt")
# print(result.final_output)

result = Runner.run_sync(triage_agent, "Find Dubai and India populations, calculate the ratio, save to population_report.txt")
print(f"Final output: {result.final_output}")
print(f"Last agent: {result.last_agent.name}")
print(f"New items: {len(result.new_items)}")
for item in result.new_items:
    print(f"  - {type(item).__name__}: {item}")