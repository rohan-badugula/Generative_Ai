from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# so this is the noteboook that menitons why there is a need for the chat model to access the memory, 
# so I have created a plain chatbot intially, it looks and works like chatgpt, but you know what it lacks the context.
# if I ask it somethinh from its previous chat it say I donot now, 
"""
to solve this, we can either
    * Add a chat_history list, which takes in all the chats exchanged between the user and ai, and saves it
    -> problem here is it cannot account for, who sent what message, now we can use dicts and mention that
    * We can already do this directly by using lang chain messages. (look 4_messages.py)
"""


model = ChatOpenAI(model = "gpt-3.5-turbo")

chat_history = []
while True:
    user_inp = input("You: ")
    if user_inp == "exit":
        break
    chat_history.append(user_inp)
    result = model.invoke( chat_history)
    print("AI:  "+str(result.content))

print(chat_history)
