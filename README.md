# AI Interviewer Server

A FastAPI-based server for conducting mock interviews powered by AI. This application uses the CrewAI framework along with OpenAI's language models to simulate a technical interviewer who can ask questions and evaluate responses.

## Features

- 🤖 AI-powered mock interviews for technical roles
- 🎭 Custom interviewer personas
- 📋 Tailored questions based on job descriptions
- 📊 Detailed feedback and evaluation
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

### Running the server

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

## Project Structure

```
backend/
├── __init__.py
├── main.py                   # Main application file
├── crew/                     # AI crew implementation
│   ├── __init__.py
│   └── mock_interview.py     # Interview simulation logic
├── models/                   # Database models (for future use)
│   └── __init__.py
├── schemas/                  # Pydantic models
│   ├── __init__.py
│   └── interview.py          # Request/response schemas
├── routers/                  # API routes
│   ├── __init__.py
│   └── interview.py          # Interview endpoints
└── services/                 # Business logic
    ├── __init__.py
    └── interview.py          # Interview service
```

## Technology Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **CrewAI**: Framework for orchestrating role-playing AI agents
- **LangChain**: Framework for building applications with LLMs
- **OpenAI**: Provides the GPT models for interview simulation
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
