from backend.crew.coach import run_coaching_session
from backend.schemas.coaching import CoachingResponse

class CoachingService:
    """Service for handling coaching sessions"""
    
    def run_coaching(self, coach_name: str, skill_area: str, experience_level: str, improvement_goal: str) -> CoachingResponse:
        """
        Run a coaching session with the specified parameters
        
        Args:
            coach_name (str): Name of the coach
            skill_area (str): Technical area to focus on
            experience_level (str): Level of experience
            improvement_goal (str): What the candidate wants to improve
            
        Returns:
            CoachingResponse: The coaching session results
        """
        result = run_coaching_session(coach_name, skill_area, experience_level, improvement_goal)
        return CoachingResponse(coaching_result=result["coaching_result"]) 