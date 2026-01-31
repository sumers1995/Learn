from transformers import pipeline

sentiment = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)

texts = [
    "Absolutely loved the new update! Battery life finally improved.",
    "Crashes on launch after installing the patch. Unusable.",
    "Works fine, but the onboarding is confusing for new users."
]

sentiment(texts)