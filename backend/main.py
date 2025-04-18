from fastapi import FastAPI
from backend.routers import interview, coaching
from backend.config import initialize_api_keys

# Initialize application
app = FastAPI(
    title="AI Interview Preparation API",
    description="API for conducting AI-powered mock interviews and coaching sessions",
    version="1.0.0"
)

# Initialize API keys at startup
@app.on_event("startup")
async def startup_event():
    initialize_api_keys()
    print("✨ API is ready to use!")

@app.get("/")
async def root():
    return {
        "message": "Interview Prep API is running 🚀",
        "usage": "Use /mock-interview for practice interviews or /coaching for personalized coaching"
    }

# Include all routers
app.include_router(interview.router)
app.include_router(coaching.router)

# Add CORS middleware if needed:
# from fastapi.middleware.cors import CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
