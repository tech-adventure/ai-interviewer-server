import os
import sys
from dotenv import load_dotenv

from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# Load environment variables from .env file:
load_dotenv()

# Get OpenAI API key:
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    print("OPENAI_API_KEY not found in environment variables.")
    print("Please enter your OpenAI API key: ", end='')
    openai_api_key = input().strip()
    
    if not openai_api_key:
        print("No API key provided. Exiting...")
        sys.exit(1)
    else:
        os.environ["OPENAI_API_KEY"] = openai_api_key

# Initialize the LLM:
try:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, api_key=openai_api_key)
except Exception as e:
    print(f"ERROR initializing ChatOpenAI: {e}")
    sys.exit(1)

def run_mock_interview(interviewer_name: str, role: str, job_description: str):
    """
    Run a mock interview with the specified parameters.
    
    Args:
        interviewer_name (str): Name of the interviewer
        role (str): Job role being interviewed for
        job_description (str): Detailed job description
        
    Returns:
        dict: Results of the interview
    """
    print(f"Starting mock interview with {interviewer_name} for {role} role")
    
    # Create a more detailed interviewer agent:
    interviewer = Agent(
        role=f"Technical Interviewer ({interviewer_name})",
        goal=f"Assess the candidate's suitability for the {role} position by asking relevant technical questions and evaluating responses",
        backstory=f"""You are {interviewer_name}, an experienced technical interviewer at a leading tech company.
        With years of industry experience, you excel at identifying top talent for {role} positions.
        You're looking to fill a position with the following job description: {job_description}.
        You need to evaluate if the candidate has the technical skills and experience required for this role.""",
        llm=llm,
        verbose=True
    )
    
    # Create a more detailed interview task:
    task = Task(
        description=f"""Conduct a technical interview for the {role} position.
        
        1. Introduce yourself as {interviewer_name} and explain the interview process.
        2. Ask 3-5 relevant technical questions based on the job description: {job_description}
        3. For each answer, provide constructive feedback before moving to the next question.
        4. After all questions, evaluate the candidate's overall performance.
        5. Provide a final assessment with strengths and areas for improvement.
        """,
        expected_output="""A complete interview transcript including:
        - Introduction
        - Technical questions and answers with feedback
        - Final evaluation with strengths and areas for improvement
        - Hiring recommendation (Yes/No/Maybe)""",
        agent=interviewer
    )
    
    # Create and run the crew:
    crew = Crew(
        agents=[interviewer],
        tasks=[task],
        verbose=True
    )
    
    # Run the interview:
    result = crew.kickoff()
    return {"interview_result": result}

    
    

    
    