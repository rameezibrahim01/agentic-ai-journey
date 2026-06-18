from openai import OpenAI
import json
import os

mock_data = {
    "dubai population": "Dubai population is 3.5 million",
    "india population": "India population is 1.4 billion",
    "usa gdp": "USA GDP is 27 trillion dollars",
    "china gdp": "China GDP is 18 trillion dollars",
    "tesla stock": "Tesla stock price is $250",
    "apple stock": "Apple stock price is $190",
}

# Tools
def web_search(input: str):

    for key in mock_data:
        if key in input.lower():
            return mock_data[key]
    return "No data found for that query"


def calculator(num1: float, num2: float, operator: str) -> float | None:

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Devide by zero is now allowed")
        return num1 / num2
    else:
        return None


def save_to_file(file_name: str, content: str) -> str:

    try:
        os.makedirs("phase-2-agents/week-7/output-files", exist_ok=True)
        with open(f"phase-2-agents/week-7/output-files/{file_name}", "w") as f:
            f.write(content)
        return f"saved to {file_name}"
    except:
        return "failed"

##########################################


SYSTEM_PROMPT = """You are a helpful research assistant with access to tools.
 
To answer questions, use this format:
 
Thought: [reason about what you need to do]
Action: [tool_name]
Action Input: [the input to the tool as JSON]
 
After receiving an observation:
Observation: [tool result - this will be provided]
 
Repeat Thought/Action/Observation as needed.
When you have enough information:
Final Answer: [your complete answer]
 
Available tools:
- web_search(query): Search for information
- calculator(num1, num2, operator): Perform math
- save_to_file(filename, content): Save text to file
 
Always use the exact format above."""

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
MODEL = "qwen2.5:32b"


def parse_react_response(response: str) -> dict:
    lines = response.strip().split("\n")
    result = {"thought": None, "action": None, "action_input": None, "final_answer": None}

    for line in lines:
        if line.startswith("Thought:"):
            result["thought"] = line[8:].strip()
        elif line.startswith("Action:"):
            result["action"] = line[7:].strip()
        elif line.startswith("Action Input:"):
            result["action_input"] = line[13:].strip()
        elif line.startswith("Final Answer:"):
            result["final_answer"] = line[13:].strip()
    
    return result

def run_agent(user_query: str, max_iterations: int = 10) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
    
    for iteration in range(max_iterations):
        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            messages=messages
        )
        
        text = response.choices[0].message.content
        messages.append({"role": "assistant", "content": text})
        
        parsed = parse_react_response(text)
        
        # Agent is done
        if parsed["final_answer"]:
            return parsed["final_answer"]
        
        # Agent wants to use a tool
        if parsed["action"]:
            tool_name = parsed["action"].lower()
            tool_input = json.loads(parsed["action_input"])
            
            # Run the tool
            observation = safe_tool_call(tool_name, tool_input)

            # Add observation to conversation
            messages.append({
                "role": "user",
                "content": f"Observation: {observation}"
            })
        else:
            # No action and no final answer -- prompt the agent
            messages.append({
                "role": "user",
                "content": "Please continue. Use a tool or provide your Final Answer."
            })
    
    return "Max iterations reached without final answer"
 
def safe_tool_call(tool_name: str, tool_input: dict, max_retries: int = 1) -> str:
    attempts = 0

    while attempts <= max_retries:
        try:
            if tool_name == "web_search":
                result = web_search(tool_input["query"])
            elif tool_name == "calculator":
                result = str(calculator(**tool_input))
            elif tool_name == "save_to_file":
                result = save_to_file(**tool_input)
            else:
                result = f"Unknown tool: {tool_name}"
            
            return result
        except Exception as e:
            result = f"Error executing {tool_name}: {str(e)}"
            attempts += 1
            if attempts > max_retries:
                return f"Error executing {tool_name} after {max_retries + 1} attempts: {str(e)}"

# print( safe_tool_call("calculator", {"num1": 10, "num2": 0, "operator": "/"}) )
# print( safe_tool_call("unknown_tool", {}) )
# print( safe_tool_call("calculator", {"num1": 10})  )


result = run_agent("Search for Dubai population and India population. Calculate how many times Dubai fits into India. Save the result.")
print(result)
