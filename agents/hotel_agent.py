import os
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

# Load environment variables from .env file (includes the API key)
load_dotenv()

# Set up the connection to the Groq model
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Define the Hotel Agent
hotel_agent = Agent(
    role="Hotel Search Specialist",
    goal="Find the best hotel options in a given city within a given budget",
    backstory=(
        "You are a knowledgeable hospitality expert who specializes in "
        "finding comfortable and affordable hotels. You always consider "
        "location, price, guest ratings, and amenities when recommending hotels."
    ),
    llm=llm,
    verbose=True
)git add .