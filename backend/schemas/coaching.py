from pydantic import BaseModel

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
    coaching_result: str 