from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

# Directly giving examples to model
system_prompt = "You are medical first aid expert. Do not answer anything else other than first aid instructions. Be very causis about your answer. as this can go very wrong."

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

response = client.chat.completions.create(model=os.getenv("MODEL"), messages=[
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": "What should I do if someone is bleeding?"
    }
])

print(response.choices[0].message.content)
