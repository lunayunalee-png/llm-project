import argparse
import os
import pandas as pd
from openai import OpenAI


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate LLM-assisted marketing insights from a dataset"
    )
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output", required=True, help="Path to output text/markdown file")
    return parser.parse_args()


def compute_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace this with your notebook logic if you want.
    This placeholder keeps things simple and deterministic.
    """
    return df.describe(include="all")


def generate_insights(metrics: pd.DataFrame) -> str:
    prompt = (
        "You are a marketing data analyst.\n"
        "Given the following table, provide:\n"
        "1. A short performance summary\n"
        "2. Key observations\n"
        "3. Suggested next actions\n\n"
        f"{metrics.to_string()}"
    )

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content


def main():
    args = parse_args()

    df = pd.read_csv(args.input)
    metrics = compute_metrics(df)
    insights = generate_insights(metrics)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(insights)

    print(f"Insights written to {args.output}")


if __name__ == "__main__":
    main()
