from pydantic import BaseModel
from typing import Any, Dict, Optional

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
    interview_result: Any
    
    class Config:
        arbitrary_types_allowed = True
        
    def dict(self, *args, **kwargs):
        result = super().dict(*args, **kwargs)
        # Convert the CrewOutput to a string representation if needed
        if hasattr(result['interview_result'], 'raw'):
            result['interview_result'] = result['interview_result'].raw
        return result 