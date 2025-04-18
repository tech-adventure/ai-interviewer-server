import os
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Global variables
openai_api_key = None
llm = None

def initialize_api_keys():
    """Initialize API keys from environment variables or user input"""
    global openai_api_key, llm
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get OpenAI API key
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        print("OPENAI_API_KEY not found in environment variables.")
        print("Please enter your OpenAI API key: ", end='')
        openai_api_key = input().strip()
        
        if not openai_api_key:
            print("No API key provided. Exiting...")
            sys.exit(1)
        else:
            # Save it in environment for this session
            os.environ["OPENAI_API_KEY"] = openai_api_key
    
    # Initialize LLM
    try:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, api_key=openai_api_key)
        print("✅ Successfully initialized OpenAI API")
    except Exception as e:
        print(f"❌ ERROR initializing ChatOpenAI: {e}")
        sys.exit(1)
    
    return openai_api_key, llm

def get_llm():
    """Get the LLM instance, initializing if necessary"""
    global llm
    if llm is None:
        initialize_api_keys()
    return llm 