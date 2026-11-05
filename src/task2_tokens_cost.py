import time
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

MODEL_NAME = "gpt-5-mini"

INPUT_PRICE_PER_MILLION = 0.25
OUTPUT_PRICE_PER_MILLION = 2.00

questions = [
    "What is machine learning?",
    "Explain supervised learning.",
    "What is overfitting in machine learning?",
    "What is the difference between AI and ML?",
    "Explain cross-validation."
]

results = []

for idx, question in enumerate(questions, start=1):

    start_time = datetime.now()
    start_perf = time.perf_counter()

    response = client.responses.create(
        model=MODEL_NAME,
        input=f"Answer the following student question clearly.\nQuestion: {question}"
    )

    end_perf = time.perf_counter()
    end_time = datetime.now()

    latency = end_perf - start_perf

    usage = response.usage

    input_tokens = usage.input_tokens
    output_tokens = usage.output_tokens
    total_tokens = usage.total_tokens

    input_cost = (input_tokens / 1_000_000) * INPUT_PRICE_PER_MILLION
    output_cost = (output_tokens / 1_000_000) * OUTPUT_PRICE_PER_MILLION

    total_cost = input_cost + output_cost

    results.append(
        {
            "question_id": idx,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "latency_seconds": round(latency, 3),
            "cost_per_request": total_cost
        }
    )

df = pd.DataFrame(results)

df.to_csv(
    "data/outputs/latency_tokens_cost.csv",
    index=False
)

avg_cost = df["cost_per_request"].mean()

monthly_projection = avg_cost * 10000

print(f"\nAverage Cost Per Request: ${avg_cost:.6f}")
print(f"Projected Monthly Cost (10,000 requests): ${monthly_projection:.2f}")

print(df)