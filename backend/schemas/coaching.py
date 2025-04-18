from pydantic import BaseModel
from typing import Any, Dict, Optional

class CoachingRequest(BaseModel):
    coach_name: str = "Alex"
    skill_area: str = "Algorithms and Data Structures"
    experience_level: str = "Intermediate"
    improvement_goal: str = "Improve problem-solving skills for technical coding interviews"
    
    class Config:
        schema_extra = {
            "example": {
                "coach_name": "Taylor",
                "skill_area": "System Design",
                "experience_level": "Advanced",
                "improvement_goal": "Learn how to design scalable distributed systems for interview questions"
            }
        }

class CoachingResponse(BaseModel):
    coaching_result: Any
    
    class Config:
        arbitrary_types_allowed = True
        
    def dict(self, *args, **kwargs):
        result = super().dict(*args, **kwargs)
        # Convert the CrewOutput to a string representation if needed
        if hasattr(result['coaching_result'], 'raw'):
            result['coaching_result'] = result['coaching_result'].raw
        return result 