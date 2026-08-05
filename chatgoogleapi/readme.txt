This folder have 3 files:
1. chatgoogleapi.py - this is the main program to use as an AI chatbot.
2. checkavailAPIservice.py - this is to check the available API services on the gemini account.
3. config.ini - where the API key and gemini model are set.

To setup:
1. Get API keys at Google AI studio (https://aistudio.google.com/prompts/new_chat). You can do this by going to dashboard and click 'Create API key'.
2. Apply the key in config.ini.
for config.ini, i did the following setup:
[google]
apikey = Your_key_here
geminimodel = Your_model_here