import os
import configparser
from google import genai

# Load the config
config = configparser.ConfigParser()
config.read("config.ini")

apikey = config["google"]["apikey"]
geminimodel = config["google"]["geminimodel"]

# The client automatically reads the GEMINI_API_KEY environment variable
client = genai.Client(api_key=apikey)

# Initialize a chat session with the set model
chat = client.chats.create(model=geminimodel)

print("AI Chat initialized!\n")

while True:
    print("Enter your enquiry. Type 'exit' or 'quit' to end the conversation.")
    # 1. Get user input
    user_message = input("You: ")
    
    # 2. Check for exit commands
    if user_message.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break
        
    # 3. Skip empty messages
    if not user_message.strip():
        continue
        
    try:
        # 4. Send message and print the response
        response = chat.send_message(user_message)
        print(f"AI: {response.text}\n")
    except Exception as e:
        print(f"Error: {e}")
