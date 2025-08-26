import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():

    if len(sys.argv) != 2:
        print("You need to include a prompt!")
        sys.exit(1)
    #llm prompt
    prompt = sys.argv[1]

    response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=prompt
    )
    print(response.text)
    usage = response.usage_metadata

    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")

if __name__ == "__main__":
    main()
