from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY","")
# configure OpenAI service client 
client = OpenAI=(openai_key)
deployment = "gpt-3.5-turbo"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
