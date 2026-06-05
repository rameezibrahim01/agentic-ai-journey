
# •	System prompt: 'You are a research assistant. Use tools to answer questions accurately.'
# •	Tools: web_search (mock — return hardcoded data), calculator, save_to_file
# •	Multi-turn: keep full conversation history
# •	Full tool loop: detect tool use → run function → return result → get final answer
# •	Test query: 'Search for Dubai population, calculate how many times it fits into India population, and save the result'

import json
from openai import OpenAI

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

import os

def save_to_file(file_name: str, content: str) -> str:

    try:
        os.makedirs("phase-1-llm/week-4/output-files", exist_ok=True)
        with open(f"phase-1-llm/week-4/output-files/{file_name}", "w") as f:
            f.write(content)
        return f"saved to {file_name}"
    except:
        return "failed"

# main function

def multi_tool_research_assistant():
    print("*** Multi Tool Research Assistant ***")

    tools = [
        {
            "type": "function",
            "function": {
                "name": "web_search",
                "description": "Used to search in web for provided content",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input": {
                            "type": "string",
                            "description": "key to search on web"
                        }
                    },
                    "required": ["input"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "calculator",
                "description": "Used to perform addition, subtraction, multiplication, division. Use symbols for math function",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num1": {
                            "type": "number",
                            "description": "first number"
                        },
                        "num2": {
                            "type": "number",
                            "description": "second number"
                        },
                        "operator": {
                            "type": "string",
                            "description": "operator"
                        }
                    },
                    "required": ["num1", "num2", "operator"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "save_to_file",
                "description": "Used to save the content to file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_name": {
                            "type": "string",
                            "description": "name of the file to save"
                        },
                        "content": {
                            "type": "string",
                            "description": "content to save on the file"
                        }
                    },
                    "required": ["file_name", "content"]
                }
            }
        }
    ]

    MODEL = "qwen2.5:32b"
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    SYSTEM_PROMPT = "You are a research assistant. Use tools to answer questions accurately."
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    
    print("Type 'quit' to exit ")
    while True:

        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Good bye!")
            break

        messages.append({"role": "user", "content": user_input})

        initial_response = client.chat.completions.create(
            model = MODEL,
            max_tokens = 1024,
            messages = messages,
            tools = tools
        )

        response_message = initial_response.choices[0].message

        messages.append(response_message)

        while response_message.tool_calls:
            tool_call = response_message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            print(f"{tool_name} : {tool_args}")

            if tool_name.lower() == "web_search":
                web_search_result = web_search(input = tool_args["input"])

                messages.append(
                     {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": web_search_result
                    }
                    )

            elif tool_name.lower() == "calculator":
                        calculator_result = calculator(num1 = tool_args["num1"], num2 = tool_args["num2"], operator = tool_args["operator"])

                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": str(calculator_result)
                            }
                        )
            elif tool_name.lower() == "save_to_file":
                        save_file_result = save_to_file(file_name = tool_args["file_name"], content = tool_args["content"])

                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tool_call.id,
                                "content": str(save_file_result)
                            }
                        )
        
            final_response = client.chat.completions.create(
                model = MODEL,
                max_tokens = 1024,
                tools = tools,
                messages = messages
            )

            messages.append(final_response.choices[0].message)

            response_message = final_response.choices[0].message

        print(f"Assistant: {response_message.content}")

multi_tool_research_assistant()
