from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from crewai import  LLM
from langchain_groq import ChatGroq

load_dotenv()
# Retrieve the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
groq_api_key= os.getenv("GROQ_API_KEY")
openai_api_key= os.getenv("OPENAI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
# Initialize the Gemini 2.0 Flash model
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=gemini_api_key
)
crewai_gemini_llm = LLM(
              model='gemini/gemini-2.5-flash',
              api_key=gemini_api_key
            )


groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=groq_api_key
)

openai_llm = LLM(
    model="openai/gpt-3.5-turbo",  # correct model name
    temperature=0.8,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42,
    api_key=openai_api_key
)