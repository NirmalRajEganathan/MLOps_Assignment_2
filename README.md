# MLOps Assignment 2
## LLMOps: API Cost, Latency, and Prompt Version Management

### Student
Nirmal Raj Eganathan

---

## Objective

This assignment demonstrates LLMOps practices using the OpenAI API and MLflow. The project evaluates multiple prompt versions, measures latency, calculates token-based costs, and manages prompt versions through MLflow Prompt Registry.

---

## Environment

### Python Version

```bash
Python 3.12
```

### Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Required Libraries

```bash
pip install openai
pip install python-dotenv
pip install pandas
pip install mlflow
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Do not hardcode API keys in source code.

---

## Project Structure

```text
MLOps_Assignment_2/
│
├── data/
│   └── outputs/
│       ├── latency_results.csv
│       ├── latency_summary.csv
│       ├── latency_tokens_cost.csv
│       └── prompt_evaluation_results.csv
│
├── src/
│   ├── test_openai.py
│   ├── task1_latency.py
│   ├── latency_summary.py
│   ├── task2_tokens_cost.py
│   ├── task3_prompt_eval.py
│   └── task3_mlflow_logging.py
│
├── screenshots/
├── reports/
├── requirements.txt
└── README.md
```

---

## Running the Experiment

### Step 1: Verify OpenAI Connectivity

```bash
python src/test_openai.py
```

---

### Step 2: Measure Latency

```bash
python src/task1_latency.py
```

Output:

```text
data/outputs/latency_results.csv
```

---

### Step 3: Generate Latency Statistics

```bash
python src/latency_summary.py
```

Output:

```text
data/outputs/latency_summary.csv
```

---

### Step 4: Token Usage and Cost Analysis

```bash
python src/task2_tokens_cost.py
```

Output:

```text
data/outputs/latency_tokens_cost.csv
```

---

### Step 5: Prompt Evaluation

```bash
python src/task3_prompt_eval.py
```

Output:

```text
data/outputs/prompt_evaluation_results.csv
```

---

### Step 6: Log Results to MLflow

```bash
python src/task3_mlflow_logging.py
```

---

## Launch MLflow UI

Activate virtual environment first:

```bash
venv\Scripts\activate
```

Run:

```bash
python -m mlflow ui
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Prompt Versions

### Version 1

```text
Answer the following student question clearly.

Question: {{question}}
```

### Version 2

```text
You are an academic assistant.
Answer the following student question in a clear, concise, and accurate manner.
Use simple language suitable for undergraduate students.

Question: {{question}}
```

### Version 3

```text
You are an academic assistant.

Answer the student question and return ONLY valid JSON.

Do not include markdown, explanations outside JSON, or code fences.

Use this exact JSON schema:

{
  "answer": "string",
  "confidence": "high | medium | low",
  "key_points": ["string"]
}

Question: {{question}}
```

---

## Model Information

Model Used:

```text
gpt-5-mini
```

Pricing Assumptions:

```text
Input Tokens: $0.25 per million tokens
Output Tokens: $2.00 per million tokens
```

Currency:

```text
USD
```

---

## Reproducing Results

1. Create virtual environment
2. Install dependencies
3. Configure `.env`
4. Verify OpenAI connection
5. Run Task 1
6. Run Task 2
7. Run Task 3
8. Log metrics to MLflow
9. Launch MLflow UI
10. Capture required screenshots

---