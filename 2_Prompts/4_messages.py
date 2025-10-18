from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

"""
Now its the same application with knowledge, but using messages
"""


model = ChatOpenAI(model="gpt-3.5-turbo")

messages=[
    SystemMessage(content = "you are an helpful, knowledge assistant, you will answer in breif and short")
]

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    messages.append(HumanMessage(content = user_input))
    result = model.invoke(messages)
    print("AI: "+ result.content)
    messages.append(AIMessage(result.content))

print(messages)
