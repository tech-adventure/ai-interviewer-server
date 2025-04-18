import os
from crewai import Agent, Task, Crew
from backend.config import get_llm

def run_coaching_session(coach_name: str, skill_area: str, experience_level: str, improvement_goal: str):
    """
    Run a coaching session with the specified parameters.
    
    Args:
        coach_name (str): Name of the coach
        skill_area (str): Technical area to focus on (e.g., "Python", "System Design", "Algorithms")
        experience_level (str): Level of experience (e.g., "Beginner", "Intermediate", "Advanced")
        improvement_goal (str): What the candidate wants to improve
        
    Returns:
        dict: Results of the coaching session
    """
    print(f"Starting coaching session with {coach_name} on {skill_area} for {experience_level} level")
    
    # Get the LLM from the centralized config
    llm = get_llm()
    
    # Create a coach agent:
    coach = Agent(
        role=f"Technical Coach ({coach_name})",
        goal=f"Help the candidate improve their {skill_area} skills for technical interviews",
        backstory=f"""You are {coach_name}, an experienced technical coach with expertise in {skill_area}.
        You have helped hundreds of candidates successfully prepare for technical interviews.
        You specialize in working with {experience_level} level candidates and are excellent at
        breaking down complex concepts into understandable pieces.
        Your coaching style is supportive yet challenging, always pushing candidates to think deeper.""",
        llm=llm,
        verbose=True
    )
    
    # Create a coaching task:
    task = Task(
        description=f"""Provide a personalized coaching session for a {experience_level} level candidate in {skill_area}.
        
        The candidate's goal is: {improvement_goal}
        
        Your coaching session should include:
        
        1. A brief assessment of what skills are needed for {skill_area} interview questions
        2. 3-5 specific techniques or strategies to improve in this area
        3. 2-3 practice exercises tailored to the {experience_level} level
        4. A study plan for the next week to continue improvement
        5. Key concepts to focus on mastering for interview success
        
        Provide constructive feedback throughout and encourage specific actions.
        """,
        expected_output="""A detailed coaching session including:
        - Initial assessment
        - Targeted improvement strategies
        - Custom practice exercises
        - A structured study plan
        - Focus areas for continued learning""",
        agent=coach
    )
    
    # Create and run the crew:
    crew = Crew(
        agents=[coach],
        tasks=[task],
        verbose=True
    )
    
    # Run the coaching session:
    result = crew.kickoff()
    
    # We return the CrewOutput object directly
    return {"coaching_result": result} 