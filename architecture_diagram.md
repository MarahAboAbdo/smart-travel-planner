# System Architecture & Agent Dependencies

## Overview
This diagram shows the three agents in the Smart Travel Planner crew, their execution order, and how data flows between them (the "handoff protocol").

## Architecture Diagram

```mermaid
graph TD
    U[User Input:<br/>origin, destination, budget] --> C[Crew Orchestrator<br/>Process.sequential]

    C --> A1[Flight Agent<br/>Flight Search Specialist]
    C --> A2[Hotel Agent<br/>Hotel Search Specialist]
    C --> A3[Itinerary Agent<br/>Trip Itinerary Manager]

    A1 -->|Flight Task output| CTX[Shared Context]
    A2 -->|Hotel Task output| CTX
    CTX -->|context = flight_task, hotel_task| A3

    A3 --> R[Final Travel Itinerary]

    style A1 fill:#cce5ff
    style A2 fill:#ffe5cc
    style A3 fill:#d5f5d5
    style CTX fill:#f0f0f0
```

## Execution Order (Sequential Process)

1. **Flight Agent** runs first — searches for flight options based on origin, destination, and budget.
2. **Hotel Agent** runs second — searches for hotel options based on destination and budget (runs independently of the Flight Agent).
3. **Itinerary Agent** runs last — receives the outputs of both previous tasks as `context`, and combines them into one final itinerary that respects the total budget.

## Handoff Protocol

The dependency between agents is implemented in `main.py` using CrewAI's `context` parameter:

```python
itinerary_task.context = [flight_task, hotel_task]
```

This means the Itinerary Agent does not repeat the flight/hotel search — it receives the *already completed* outputs of the other two tasks as input, and its only job is to merge and validate them against the budget.