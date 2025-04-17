from fastapi import FastAPI
from backend.routers import interview

app = FastAPI(
    title="AI Mock Interview API",
    description="API for conducting AI-powered mock interviews",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Interview Prep API is running 🚀",
        "usage": "Send a request to /mock-interview to start a mock interview"
    }

# Include all routers
app.include_router(interview.router)

# Add CORS middleware if needed
# from fastapi.middleware.cors import CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
