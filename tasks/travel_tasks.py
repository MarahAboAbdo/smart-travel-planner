from crewai import Task
from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.itinerary_agent import itinerary_agent


def create_flight_task(origin, destination, budget):
    return Task(
        description=(
            f"Search for flight options from {origin} to {destination} "
            f"with a budget of {budget} USD. List at least 2 options with "
            f"approximate prices and durations."
        ),
        expected_output="A short list of flight options with prices and durations.",
        agent=flight_agent
    )


def create_hotel_task(destination, budget):
    return Task(
        description=(
            f"Search for hotel options in {destination} with a budget of "
            f"{budget} USD per night. List at least 2 options with "
            f"approximate prices and ratings."
        ),
        expected_output="A short list of hotel options with prices and ratings.",
        agent=hotel_agent
    )


def create_itinerary_task(origin, destination, budget):
    return Task(
        description=(
            f"Combine the flight and hotel recommendations into one clear "
            f"travel itinerary for a trip from {origin} to {destination}, "
            f"making sure the total cost stays within {budget} USD."
        ),
        expected_output="A complete, well-organized travel itinerary within budget.",
        agent=itinerary_agent,
        context=[]  # will be filled in main.py with the previous tasks
    )