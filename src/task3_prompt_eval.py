import time
import json
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

PROMPTS = {
    "v1": """
Answer the following student question clearly.

Question: {question}
""",

    "v2": """
You are an academic assistant.
Answer the following student question in a clear, concise, and accurate manner.
Use simple language suitable for undergraduate students.

Question: {question}
""",

    "v3": """
You are an academic assistant.

Answer the student question and return ONLY valid JSON.

Do not include markdown.
Do not include code fences.
Do not include explanations outside JSON.

Use this JSON schema:

{
  "answer": "string",
  "confidence": "high | medium | low",
  "key_points": ["string"]
}

Question: {question}
"""
}

results = []

for version, prompt_template in PROMPTS.items():

    json_valid_count = 0

    total_latency = 0
    total_input_tokens = 0
    total_output_tokens = 0
    total_cost = 0

    for question in questions:

        prompt = prompt_template.replace("{question}",question)


        start = time.perf_counter()

        response = client.responses.create(
            model=MODEL_NAME,
            input=prompt
        )

        latency = time.perf_counter() - start

        output_text = response.output_text

        usage = response.usage

        input_tokens = usage.input_tokens
        output_tokens = usage.output_tokens

        cost = (
            input_tokens / 1_000_000 * INPUT_PRICE_PER_MILLION
        ) + (
            output_tokens / 1_000_000 * OUTPUT_PRICE_PER_MILLION
        )

        total_latency += latency
        total_input_tokens += input_tokens
        total_output_tokens += output_tokens
        total_cost += cost

        if version == "v3":
            try:
                json.loads(output_text)
                json_valid_count += 1
            except:
                pass

    avg_latency = total_latency / len(questions)
    avg_input_tokens = total_input_tokens / len(questions)
    avg_output_tokens = total_output_tokens / len(questions)
    avg_cost = total_cost / len(questions)

    valid_json = (
        json_valid_count / len(questions)
        if version == "v3"
        else None
    )

    results.append({
        "prompt_version": version,
        "avg_latency_seconds": round(avg_latency, 3),
        "avg_input_tokens": round(avg_input_tokens, 2),
        "avg_output_tokens": round(avg_output_tokens, 2),
        "avg_cost_per_request": round(avg_cost, 6),
        "valid_json": valid_json
    })

df = pd.DataFrame(results)

df.to_csv(
    "data/outputs/prompt_evaluation_results.csv",
    index=False
)

print(df)