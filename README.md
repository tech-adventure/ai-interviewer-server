# AI Interview Preparation API

A FastAPI-based server for AI-powered interview preparation. This application uses the CrewAI framework along with OpenAI's language models to provide mock interviews and personalized coaching for technical roles.

## Features

- 🤖 AI-powered mock interviews for technical roles
- 👨‍🏫 Personalized coaching sessions with tailored advice
- 🎭 Custom interviewer and coach personas
- 📋 Tailored questions based on job descriptions
- 📊 Detailed feedback and improvement plans
- 🔄 Simple REST API for easy integration

## Getting Started

### Prerequisites

- Python 3.11+
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-interviewer-server.git
   cd ai-interviewer-server
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   
   Alternatively, the application will prompt you for the API key at startup if it's not found.

### Running the server

```bash
uvicorn backend.main:app --reload
```

The API will be available at http://localhost:8000

### Docker

You can also run the application using Docker:

```bash
docker-compose up --build
```

## API Usage

### Interactive Swagger Documentation

Access the interactive API documentation at http://localhost:8000/docs

### Mock Interview Endpoints

#### GET /mock-interview

Conduct a mock interview using query parameters:

```
GET /mock-interview?interviewer_name=John&role=Software%20Engineer&job_description=Senior%20Python%20Developer
```

#### POST /mock-interview

Conduct a mock interview using a JSON body:

```bash
curl -X 'POST' \
  'http://localhost:8000/mock-interview/' \
  -H 'Content-Type: application/json' \
  -d '{
  "interviewer_name": "Sarah",
  "role": "Full Stack Developer",
  "job_description": "We are looking for a Full Stack Developer with experience in React, Node.js, and AWS."
}'
```

### Coaching Endpoints

#### GET /coaching

Get personalized coaching using query parameters:

```
GET /coaching?coach_name=Alex&skill_area=Algorithms&experience_level=Intermediate&improvement_goal=Improve%20problem-solving
```

#### POST /coaching

Get personalized coaching using a JSON body:

```bash
curl -X 'POST' \
  'http://localhost:8000/coaching/' \
  -H 'Content-Type: application/json' \
  -d '{
  "coach_name": "Taylor",
  "skill_area": "System Design",
  "experience_level": "Advanced",
  "improvement_goal": "Learn how to design scalable distributed systems for interview questions"
}'
```

## Project Structure

```
backend/
├── __init__.py
├── main.py                   # Main application file
├── config.py                 # Configuration and API key management
├── crew/                     # AI crew implementation
│   ├── __init__.py
│   ├── mock_interview.py     # Interview simulation logic
│   └── coach.py              # Coaching session logic
├── models/                   # Database models (for future use)
│   └── __init__.py
├── schemas/                  # Pydantic models
│   ├── __init__.py
│   ├── interview.py          # Interview request/response schemas
│   └── coaching.py           # Coaching request/response schemas
├── routers/                  # API routes
│   ├── __init__.py
│   ├── interview.py          # Interview endpoints
│   └── coaching.py           # Coaching endpoints
└── services/                 # Business logic
    ├── __init__.py
    ├── interview.py          # Interview service
    └── coaching.py           # Coaching service
```

## Architecture

The application follows a clean, modular architecture:

1. **API Layer** - FastAPI routes and endpoints
2. **Service Layer** - Business logic and orchestration
3. **Schema Layer** - Request/response data validation
4. **Agent Layer** - AI implementation with CrewAI

API keys are managed centrally through the config module, which initializes once at application startup.

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **CrewAI**: Framework for orchestrating role-playing AI agents
- **LangChain**: Framework for building applications with LLMs
- **OpenAI**: Provides the GPT models for interview simulation
- **Pydantic**: Data validation and settings management
- **Docker**: For containerization and easy deployment

## Development

### Adding New Features

1. Create new schemas in the `schemas` directory
2. Implement services in the `services` directory
3. Define new routes in the `routers` directory
4. Register new routers in `main.py`

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [OpenAI](https://openai.com/) for their powerful language models
- [CrewAI](https://crewai.io/) for the agent orchestration framework
- [FastAPI](https://fastapi.tiangolo.com/) for the API framework
