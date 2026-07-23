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

# Define the Itinerary Agent (acts as the coordinator)
itinerary_agent = Agent(
    role="Trip Itinerary Manager",
    goal=(
        "Combine flight and hotel recommendations into a clear, complete "
        "travel itinerary that fits within the traveler's budget"
    ),
    backstory=(
        "You are a professional trip planner who excels at combining "
        "separate pieces of travel information into one clear, well-organized "
        "plan. You always double-check that the total cost stays within budget."
    ),
    llm=llm,
    verbose=True
)