import chainlit as cl
from litellm import completion
from dotenv import load_dotenv
import os
import json
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
@cl.on_chat_start
async def chat_start():
    """Set up the chat session when a user connects."""
    cl.user_session.set('chat_history',[])
    await cl.Message(content="Welcome to the AI Assistant! How can I help you today?").send()
    print(GEMINI_API_KEY)


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    history = cl.user_session.get('chat_history') or []
    print("history",history)
    msg =  cl.Message(content="Thinking...") 
    await msg.send()
    history.append({"role":"user","content":message.content})
    
    try:
        response = completion(
            model="gemini/gemini-2.5-flash-preview-04-17",
            api_key=GEMINI_API_KEY,
            messages=history
        )
        response_content = response['choices'][0]['message']['content']
        msg.content = response_content
        await msg.update()

        history.append({"role":"assistant","content":response_content})

        cl.user_session.set("chat_history",history)
        #  Optional: Log the interaction
        print(f"User: {message.content}")
        print(f"Assistant: {response_content}")
    except Exception as e:
        msg.content = f"Error {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")
    # Send a response back to the user
    # print(cl)

@cl.on_chat_end
async def chat_end():
    history = cl.user_session.get('chat_history')
    with open("chat_history.json","w") as f:
         json.dump(history, f, indent=2)
    print("Chat history saved.")
if __name__ == "__main__":
    main()
