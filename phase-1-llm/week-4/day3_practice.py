# from openai import OpenAI
 
# client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
# MODEL = "qwen2.5:32b"
 
# messages = [
#     {"role": "system", "content": "You are a helpful Python tutor."}
# ]

# def chat_without_stream(): 
#     print("Chat with qwen2.5:32b (type 'quit' to exit)")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "quit":
#             break
    
#         messages.append({"role": "user", "content": user_input})
    
#         response = client.chat.completions.create(
#             model=MODEL,
#             max_tokens=1024,
#             messages=messages
#         )
    
#         reply = response.choices[0].message.content
#         messages.append({"role": "assistant", "content": reply})
#         print(f"qwen: {reply}")


# # chat_without_stream()

# def chat_with_stream():
#     print("Chat with qwen2.5:32b (type 'quit' to exit)")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "quit":
#             break
    
        # messages.append({"role": "user", "content": user_input})
    
        # response = client.chat.completions.create(
        #     model=MODEL,
        #     max_tokens=1024,
        #     stream=True,
        #     messages=messages
        # )
    
#         for chunk in response:
#             delta = chunk.choices[0].delta
#             if delta.content:
#                 print(delta.content, end="", flush=True)
#         print()

# # chat_with_stream()

print("•	Build a simple chatbot: loop asking for input, send to qwen, print response. Store and send full conversation history each time.")

from openai import OpenAI

MODEL = "qwen2.5:32b"
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

def begin_ai_engineer_bot():
    messages = [{"role": "system", "content": "You are an experienced AI Engineer"}]
    print("Please Enter 'quit' to exit")
    while True:
        user_input = input(f"User: ")
        if user_input.lower() == "quit":
            print("Bye Bye! Thank you!")
            return
        
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=1024,
            messages = messages
        )


        reply = response.choices[0].message.content
        print(f"Assistant: {reply}")
        messages.append({"role": "assistant", "content": reply})

# begin_ai_engineer_bot()


print("•	Build a code reviewer: user pastes Python code, qwen reviews it as a senior engineer. System prompt: concise, point out bugs, suggest improvements, max 5 bullet points.")


def code_reviewer_bot():
    messages = [{"role": "system", "content": "You are a senior engineer, concise, point out bugs, suggest improvements, max 5 bullet points."}]
    print("Welcome to code review bot! If you want to exit , please type 'quit' or 'exit'")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            print("Good bye!")
            break
        
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model = MODEL,
            max_tokens = 1024,
            stream=True,
            messages = messages
        )

        complete_reply = ""
        for chunk in response:
            delta = chunk.choices[0].delta
            if delta.content:
                print(delta.content, end="", flush=True)
                complete_reply += delta.content     
        print()

        messages.append({"role": "assistant", "content": complete_reply})


# code_reviewer_bot()



print("•	Build a streaming story generator: user gives a theme, qwen streams a short story. Print tokens as they arrive.")



def streaming_story_generator():
    messages = [{"role": "system", "content": "You are a story teller!. Story should not be more then 100 charecters!"}]
    print("Welcome to story bot! Tell me the story theme (for eg. tiger and forest)\nIf you want to exit , please type 'quit' or 'exit'")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit' or user_input.lower() == 'quit':
            print("Good bye!")
            break
        
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model = MODEL,
            max_tokens = 1024,
            stream=True,
            messages = messages
        )

        complete_reply = ""
        for chunk in response:
            delta = chunk.choices[0].delta
            if delta.content:
                print(delta.content, end="", flush=True)
                complete_reply += delta.content     
        print()

        messages.append({"role": "assistant", "content": complete_reply})


streaming_story_generator()