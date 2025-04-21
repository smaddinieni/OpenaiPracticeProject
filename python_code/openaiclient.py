import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Fetch API key and model from environment variables
api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")

if not api_key:
    raise ValueError("API key is not set in the .env file.")
if not model:
    raise ValueError("Model is not set in the .env file.")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)
