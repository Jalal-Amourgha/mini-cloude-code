import os
from dotenv import load_dotenv
from openai import OpenAI
from src.prompts import system_prompt
from src.functions.functions_schemas import functions_schemas
from src.functions.functions_calling import available_functions
from src.agent.agent import Agent

def main():
    """Initialize the environment and launch the AI agent.

    Load environment variables, retrieve the OpenRouter API key, configure
    the API client, and initialize the agent with its system prompt,
    tool schemas, available functions, and iteration limit.

    Raises:
        ValueError: If the required API key is missing, provided that
            the function explicitly validates it.
    """

    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")

    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key,
    )


    Agent(client, system_prompt, functions_schemas, available_functions, 20)


if (__name__ == "__main__"):
    main()
