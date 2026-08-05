import configparser
from google import genai

# Load the config
config = configparser.ConfigParser()
config.read("config.ini")

apikey = config["google"]["apikey"]

client = genai.Client(api_key=apikey)

models = client.models.list()

for m in models:
    print(m.name)

