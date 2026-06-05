from openai import OpenAI
import json


def get_weather(city: str) -> str:
    return f"The weather in {city} is 35 celcius"

MODEL = "qwen2.5:32b"
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

tools = [{
    "type": "function",
    "function": {
        "name" : "get_weather",
        "description" : "Get current weather for a city",
        "parameters": {
            "type" : "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city name e.g. Dubai"
                }
            },
            "required" : ["city"]
        }
    }
}]

def begin_weather_bot():
    messages = [{"role": "system", "content": "You are a weather expert"}]
    print("Please Enter 'quit' to exit")
    while True:
        user_input = input(f"You : ")
        if user_input.lower() == "quit":
            print("Bye Bye! Thank you!")
            return
        
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            tools = tools,
            messages = messages
        )

        message = response.choices[0].message

        messages.append(message)

        if message.tool_calls:
            tool_call = message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            if tool_name == "get_weather":
                weather_result = get_weather(tool_args["city"])

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": weather_result
                })

                # get final response
                final_response = client.chat.completions.create(
                    model=MODEL,
                    max_tokens=1024,
                    tools=tools,
                    messages=messages
                )

                print(f"Assistant: {final_response.choices[0].message.content}")
        else:
            print(f"Assistant: {message.content}")



# begin_weather_bot()




print("•	Add a calculator tool (add, subtract, multiply, divide). Ask math questions and watch the model use the tool.")


def calculate(num1: int, num2: int, operator: str) -> int | None:
    print(f"🔧 calculate() called: {num1} {operator} {num2}")
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Cannot devide by Zero")
        return num1 / num2
    else:
        return None


def calculator_bot():

    print("Please Enter 'quit' to exit")

    messages = [{"role": "system", "content": "You are a math calculator"}]

    tools = [
        {
            "type": "function",
            "function" : {
                "name" : "calculate",
                "description": "Used to perform addition, subtraction, multiplication and division",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num1" : {
                            "description": "First number",
                            "type" : "integer"
                        },
                        "num2" : {
                            "description": "second number",
                            "type" : "integer"
                        },
                        "operator" : {
                            "description": "Operator",
                            "type" : "string"
                        }
                    }
                },
                "required": ["num1", "num2", "operator"]
            }
        }
    ]

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model= MODEL,
            max_tokens = 1024,
            messages = messages,
            tools = tools
        )

        message = response.choices[0].message

        messages.append(message)

        if message.tool_calls:
            tool_call = message.tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            
            if tool_name.lower() == "calculate":
                cal_result = calculate(num1 = tool_args["num1"], num2 = tool_args["num2"], operator = tool_args["operator"])

                messages.append({
                                    "role": "tool",
                                    "tool_call_id": tool_call.id,
                                    "content": str(cal_result)
                                })
                
                final_answer = client.chat.completions.create(
                    model= MODEL,
                    max_tokens = 1024,
                    messages = messages,
                    tools = tools
                )

                print(f"Assistant: {final_answer.choices[0].message.content}")

        else:
            print(f"Assistant: {message.content}")


# calculator_bot()


print("•	Multiple tools: give both calculator AND weather. Ask 'What is the temperature in Dubai minus the temperature in London?' Watch it orchestrate two tool calls.")


def get_weather_for_two_cities(city1: str, city2: str) -> str:
    return f"The weather in {city1} is 35 celcius, {city2} is 40 celcius"

def calculate_weather_difference():
    print("Welcome to weather difference calculator")

    print("type 'quit' to exit")

    tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_weather_for_two_cities",
                    "description": "Get current weather for 2 cities",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city1": {
                                "type": "string",
                                "description": "name of the first city"
                            },
                            "city2": {
                                "type": "string",
                                "description": "name of the second city"
                            }
                        },
                        "required": ["city1", "city2"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "calculate",
                    "description": "Used to perform addition, subtraction, multiplication and division, for these math operations you should use symbols",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "num1": {
                                "type": "integer",
                                "description": "temperature of the first city"
                            },
                            "num2": {
                                "type": "integer",
                                "description": "temperature of the second city"
                            },
                            "operator": {
                                "type": "string",
                                "description": "math operator"
                            }
                        },
                        "required": ["num1", "num2", "operator"]
                    }
                }
            },
        ]
    messages = [{"role": "system", "content": "You are a weather expert and you will ask for 2 cities name and get the weather and find the difference between them"}]




    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Good bye")
            break
        
        messages.append({"role":"user", "content": user_input})

        response = client.chat.completions.create(
            model = MODEL,
            max_tokens = 1024,
            messages = messages,
            tools = tools
        )

        message = response.choices[0].message

        messages.append(message)

        tool_calls = message.tool_calls
        if tool_calls:
            tool_call = tool_calls[0]
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)

            if tool_name.lower() == "get_weather_for_two_cities":
                weathers = get_weather_for_two_cities(city1=tool_args["city1"], city2= tool_args["city2"])

                messages.append({
                                    "role": "tool",
                                    "tool_call_id": tool_call.id,
                                    "content": weathers
                                })
                
                weathers_response = client.chat.completions.create(
                    model = MODEL,
                    max_tokens = 1024,
                    tools = tools,
                    messages = messages
                )

                calculation_tools = weathers_response.choices[0].message.tool_calls
                if calculation_tools:
                    calculation_tool = calculation_tools[0]
                    calculation_tool_name = calculation_tool.function.name
                    calculation_tool_args = json.loads(calculation_tool.function.arguments)

                    if calculation_tool_name.lower() == "calculate":
                        print(f"args: {calculation_tool_args}")
                        calculation_result = calculate(num1 = calculation_tool_args["num1"], num2 = calculation_tool_args["num2"], operator = calculation_tool_args["operator"])
                        print(f"Assistant: {calculation_result}")

                        messages.append({
                            "role": "tool",
                            "tool_call_id": calculation_tool.id,
                            "content": str(calculation_result)
                        })


                        final_response  = client.chat.completions.create(
                            model = MODEL,
                            max_tokens = 1024,
                            tools = tools,
                            messages = messages
                        )

                        final_message = final_response.choices[0].message
                        messages.append({"role": "assistant", "content": final_message.content})
                        print(f"Assistant: {final_message.content}")
                else:
                    print(f"Assistant: {message.content}")
                # print(f"Assistant: {weathers_response.choices[0].message.content}")
        else:
            print(f"Assistant: {message.content}")



calculate_weather_difference()