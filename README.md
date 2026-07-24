# Smart Travel Planner

A multi-agent AI system built with **CrewAI** that plans a complete trip — flights, hotel, and a combined itinerary — from just three inputs: origin city, destination city, and total budget.

Built for **Assignment 3 — Multi-Agent AI Systems**.

## Overview

The system uses three specialized agents that collaborate in a sequential process:

| Agent | Role | Responsibility |
|---|---|---|
| Flight Agent | Flight Search Specialist | Finds flight options within budget |
| Hotel Agent | Hotel Search Specialist | Finds hotel options within budget |
| Itinerary Agent | Trip Itinerary Manager | Combines both into one final itinerary |

See [architecture_diagram.md](./architecture_diagram.md) for the full dependency diagram and handoff protocol.

## Tech Stack

- Python 3.11
- [CrewAI](https://docs.crewai.com) — multi-agent orchestration framework
- [Groq](https://groq.com) (Llama 3.3 70B) — LLM provider, free tier
- LiteLLM — LLM routing layer

## Project Structure

```
smart-travel-planner/
├── agents/
│   ├── flight_agent.py
│   ├── hotel_agent.py
│   └── itinerary_agent.py
├── tasks/
│   └── travel_tasks.py
├── test_screenshots/       # Screenshots from normal/edge/failure test cases
├── architecture_diagram.md
├── main.py
├── requirements.txt
└── .gitignore
```

## Setup

1. Clone the repository:
```
   git clone https://github.com/MarahAboAbdo/smart-travel-planner.git
   cd smart-travel-planner
```

2. Create and activate a virtual environment (Python 3.11 recommended):
```
   py -3.11 -m venv venv
   venv\Scripts\activate
```

3. Install dependencies:
```
   pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Groq API key:
```
   GROQ_API_KEY=your_key_here
```

## Usage

```
python main.py
```

You will be prompted for:
- Origin city
- Destination city
- Total budget (USD)

The three agents will run in sequence and print their reasoning live, ending with a combined `FINAL TRAVEL ITINERARY`.

## Testing

Three test cases were run to validate the system, with full transcripts saved as screenshots in `test_screenshots/`:

1. **Normal case** — Amman → Dubai, budget $900
2. **Edge case** — Amman → Zarqa (very short distance, low budget)
3. **Failure case** — empty inputs, negative budget

## Notes

This project uses a free-tier LLM (Groq), so responses are the model's own estimates rather than live flight/hotel booking data.