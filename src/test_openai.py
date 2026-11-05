from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create client
client = OpenAI()

# Test request
response = client.responses.create(
    model="gpt-5-mini",
    input="Say hello in one sentence."
)

print(response.output_text)