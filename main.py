
import os
from dotenv import load_dotenv

from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
import openai
import langchain



load_dotenv()

my_key = os.environ["OPENAI_API_KEY"] 

llm = OpenAI(temperature=0, openai_api_key = my_key)
text = "what is AI"
print(llm(text))

