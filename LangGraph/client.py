from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import asyncio
import os
import warnings

load_dotenv()
warnings.filterwarnings("ignore", category=DeprecationWarning)   # To ignore deprecation warnings


async def main():
    from typing import Dict, Any
    connections: Dict[str, Any] = {
        "math": {
            "command": "python",
            "args": ["c:/Users/patil/OneDrive - South Indian Education Society/Documents/Agentic AI/LangGraph/mathserver.py"],   # Absolute path
            "transport": "stdio"
        },
        "weather": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http"
        }
    }
    client = MultiServerMCPClient(connections)
    
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

    tools = await client.get_tools()
    model = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite"
    )
    agent = create_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        { "messages": [ { "role": "user", "content": "what's (3+5)x12?" } ] }
    )

    weather_response= await agent.ainvoke(
        {
            "messages": [ {"role": "user", "content": "what's the weather like in California?"} ]
        }
    )
    print("--- Math Response ---")
    for msg in math_response['messages']:
        print(f"Role: {msg.type}, Content: {msg.content}")
    print("\n--- Weather Response ---")
    for msg in weather_response['messages']:

        print(f"Role: {msg.type}, Content: {msg.content}")

if __name__ == "__main__":
    asyncio.run(main())

