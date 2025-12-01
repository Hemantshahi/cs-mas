CS-MAS Capstone Project: Women Safety Multi-Agent System
🚀 Project Overview

Women safety is a growing concern, especially in emergency situations where fast communication and decision-making are critical.
This project introduces a Women Safety Multi-Agent System using:

LLM-powered agents

Sequential \& Parallel agent execution

Tools, Memory, and State Management

Autonomous decision logic

Safety alerts and location tracking

The system can process user messages, detect emergency intent, analyze location, and trigger safety workflows automatically.

🔥 Key Features (As Required by Capstone Guidelines)
✔️ 1. Multi-Agent System

Emergency Detection Agent

Location Analyzer Agent

Action Planner Agent

Notification Agent

✔️ 2. Tool Usage

Custom Python tools for:

Location fetching

Emergency contact list

Alert creation

✔️ 3. Memory \& State

Short-term session memory

Long-term memory (Memory Bank Concept)

✔️ 4. Context Engineering

Filters irrelevant details

Compresses conversation history

Extracts emergency cues

✔️ 5. Logging \& Tracing

Tracks each agent’s reasoning

Debug-friendly logs

📁 Project Structure
cs-mas/
│── app/
│   ├── main.py
│   ├── agents/
│   ├── tools/
│   ├── models/
│   └── utils/
│── .env
│── README.md
│── venv/
│── .gitattributes

⚙️ How It Works

User sends a message like:
“I feel unsafe, someone is following me.”

Emergency Detection Agent checks tone, intent, danger level.

Location Analyzer Agent fetches nearest safe zones.

Action Planner Agent prepares steps:

Call emergency contact

Share location

Activate loud alert

Notification Agent sends final structured alert.

▶️ Run the Project Locally
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

🎯 Use Case

This agent reduces emergency-response time,
helps women respond smartly,
and enables autonomous decision-making powered by LLM agents.

📝 Team Details

Hemant Shahi – B.Tech (CSE-AI), Motihari College of Engineering

Semester: 7th

Role: LLM-based multi-agent system developer, Data analyst

