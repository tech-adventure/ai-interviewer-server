from fastapi import APIRouter, Body
from backend.schemas.interview import InterviewRequest, InterviewResponse
from backend.services.interview import InterviewService

router = APIRouter(
    prefix="/mock-interview",
    tags=["interview"],
    responses={404: {"description": "Not found"}},
)

interview_service = InterviewService()

@router.get("/", response_model=InterviewResponse)
async def get_mock_interview(
    interviewer_name: str = "John", 
    role: str = "Software Engineer", 
    job_description: str = "We are looking for a software engineer with 3 years of experience in Python and FastAPI"
):
    """
    Conduct a mock interview with the specified parameters via GET request
    """
    return interview_service.run_interview(interviewer_name, role, job_description)

@router.post("/", response_model=InterviewResponse)
async def post_mock_interview(request: InterviewRequest = Body(...)):
    """
    Conduct a mock interview with the specified parameters via POST request with JSON body
    """
    return interview_service.run_interview(
        request.interviewer_name,
        request.role, 
        request.job_description
    ) 