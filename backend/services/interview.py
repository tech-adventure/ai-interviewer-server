from backend.crew.mock_interview import run_mock_interview
from backend.schemas.interview import InterviewResponse

class InterviewService:
    """Service for handling mock interviews"""
    
    def run_interview(self, interviewer_name: str, role: str, job_description: str) -> InterviewResponse:
        """
        Run a mock interview with the specified parameters
        
        Args:
            interviewer_name (str): Name of the interviewer
            role (str): Job role being interviewed for
            job_description (str): Detailed job description
            
        Returns:
            InterviewResponse: The interview results
        """
        result = run_mock_interview(interviewer_name, role, job_description)
        return InterviewResponse(interview_result=result["interview_result"]) 