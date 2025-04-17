from pydantic import BaseModel

class InterviewRequest(BaseModel):
    interviewer_name: str = "John"
    role: str = "Software Engineer"
    job_description: str = "We are looking for a software engineer with 3 years of experience in Python and FastAPI"
    
    class Config:
        schema_extra = {
            "example": {
                "interviewer_name": "Sarah",
                "role": "Full Stack Developer",
                "job_description": "We are looking for a Full Stack Developer with experience in React, Node.js, and AWS."
            }
        }

class InterviewResponse(BaseModel):
    interview_result: str 