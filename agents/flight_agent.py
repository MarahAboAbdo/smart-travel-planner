import os
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv
import litellm

litellm.drop_params = True

import crewai.llms.cache as crewai_cache
crewai_cache.mark_cache_breakpoint = lambda msg: msg

# Load environment variables from .env file (includes the API key)
load_dotenv()

# Set up the connection to the Groq model
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Define the Flight Agent
flight_agent = Agent(
    role="Flight Search Specialist",
    goal="Find the best flight options between two cities within a given budget",
    backstory=(
        "You are an experienced travel agent who specializes in finding "
        "affordable and convenient flights. You always consider price, "
        "duration, and number of stops when recommending flights."
    ),
    llm=llm,
    verbose=True
)