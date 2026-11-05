import pandas as pd

df = pd.read_csv("data/outputs/latency_results.csv")

print("\nLatency Summary\n")

print(f"Mean   : {df['latency_seconds'].mean():.3f}")
print(f"Median : {df['latency_seconds'].median():.3f}")
print(f"Min    : {df['latency_seconds'].min():.3f}")
print(f"Max    : {df['latency_seconds'].max():.3f}")
print(f"Std Dev: {df['latency_seconds'].std():.3f}")

summary = pd.DataFrame({
    "metric": [
        "mean",
        "median",
        "min",
        "max",
        "std"
    ],
    "value": [
        df["latency_seconds"].mean(),
        df["latency_seconds"].median(),
        df["latency_seconds"].min(),
        df["latency_seconds"].max(),
        df["latency_seconds"].std()
    ]
})

summary.to_csv(
    "data/outputs/latency_summary.csv",
    index=False
)