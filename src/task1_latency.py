import os
import time
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

MODEL_NAME = "gpt-5-mini"

questions = [
    "What is machine learning?",
    "Explain supervised learning.",
    "What is overfitting in machine learning?",
    "What is the difference between AI and ML?",
    "Explain cross-validation."
]

prompt_version = "v1"

results = []

for idx, question in enumerate(questions, start=1):

    start_time = datetime.now()
    start_perf = time.perf_counter()

    try:
        response = client.responses.create(
            model=MODEL_NAME,
            input=f"Answer the following student question clearly.\nQuestion: {question}"
        )

        status = "success"

    except Exception as e:
        status = f"error: {str(e)}"

    end_perf = time.perf_counter()
    end_time = datetime.now()

    latency = end_perf - start_perf

    results.append(
        {
            "question_id": idx,
            "prompt_version": prompt_version,
            "model_name": MODEL_NAME,
            "start_time": start_time,
            "end_time": end_time,
            "latency_seconds": round(latency, 3),
            "response_status": status
        }
    )

df = pd.DataFrame(results)

df.to_csv(
    "data/outputs/latency_results.csv",
    index=False
)

print(df)