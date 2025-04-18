from fastapi import APIRouter, Body
from backend.schemas.coaching import CoachingRequest, CoachingResponse
from backend.services.coaching import CoachingService

router = APIRouter(
    prefix="/coaching",
    tags=["coaching"],
    responses={404: {"description": "Not found"}},
)

coaching_service = CoachingService()

@router.get("/", response_model=CoachingResponse)
async def get_coaching_session(
    coach_name: str = "Alex", 
    skill_area: str = "Algorithms and Data Structures", 
    experience_level: str = "Intermediate",
    improvement_goal: str = "Improve problem-solving skills for technical coding interviews"
):
    """
    Get a personalized coaching session via GET request
    """
    return coaching_service.run_coaching(coach_name, skill_area, experience_level, improvement_goal)

@router.post("/", response_model=CoachingResponse)
async def post_coaching_session(request: CoachingRequest = Body(...)):
    """
    Get a personalized coaching session via POST request with JSON body
    """
    return coaching_service.run_coaching(
        request.coach_name,
        request.skill_area, 
        request.experience_level,
        request.improvement_goal
    ) 