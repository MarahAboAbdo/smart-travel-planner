from crewai import Crew, Process
from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.itinerary_agent import itinerary_agent
from tasks.travel_tasks import (
    create_flight_task,
    create_hotel_task,
    create_itinerary_task
)


def run_trip_planner(origin, destination, budget):
    # Create the three tasks with the user's trip details
    flight_task = create_flight_task(origin, destination, budget)
    hotel_task = create_hotel_task(destination, budget)
    itinerary_task = create_itinerary_task(origin, destination, budget)

    # The itinerary task depends on the outputs of the other two tasks
    itinerary_task.context = [flight_task, hotel_task]

    # Assemble the crew with a sequential process:
    # flight and hotel tasks run first, then the itinerary task combines them
    crew = Crew(
        agents=[flight_agent, hotel_agent, itinerary_agent],
        tasks=[flight_task, hotel_task, itinerary_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    return result


if __name__ == "__main__":
    origin = input("Enter your origin city: ")
    destination = input("Enter your destination city: ")
    budget = input("Enter your total budget (USD): ")

    final_result = run_trip_planner(origin, destination, budget)

    print("\n\n=== FINAL TRAVEL ITINERARY ===\n")
    print(final_result)